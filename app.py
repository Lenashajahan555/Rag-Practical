import os
from dotenv import load_dotenv
from openai import OpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

def main():
    try:
        # 1. Load environment variables
        load_dotenv()
        
        foundry_endpoint = os.getenv("FOUNDRY_INFERENCE_ENDPOINT")
        foundry_key = os.getenv("FOUNDRY_API_KEY")
        
        search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        search_key = os.getenv("AZURE_SEARCH_KEY")
        search_index = os.getenv("AZURE_SEARCH_INDEX")

        # 2. Get user query
        user_query = input('\nEnter your search question about the PDF (e.g., list of hotels in dubai):\n')

        # 3. PHASE 1: Query Azure AI Search index
        print("\n[1/2] Searching Azure AI Search index for matching PDF sections...")
        search_client = SearchClient(
            endpoint=search_endpoint,
            index_name=search_index,
            credential=AzureKeyCredential(search_key)
        )
        
        search_results = search_client.search(search_text=user_query, top=3)
        
        retrieved_context = ""
        sources_found = []
        
        for result in search_results:
            # Adjust 'content' or 'chunk' if your index field name is different
            content = result.get("content") or result.get("chunk") or str(result)
            source_file = result.get("metadata_storage_name", "Uploaded PDF")
            retrieved_context += f"- {content}\n"
            sources_found.append(source_file)

        if not retrieved_context:
            print("No matching text found in the PDF index.")
            return

        print(f"-> Successfully retrieved relevant paragraphs from search index.")

        # 4. PHASE 2: Send context + query to Foundry model via OpenAI client
        print("\n[2/2] Generating executive answer using Foundry model...")
        client = OpenAI(
            base_url=foundry_endpoint,
            api_key=foundry_key
        )

        system_prompt = (
            "You are an enterprise AI assistant. Answer the user's question accurately "
            "using ONLY the provided text extracted from the uploaded PDF documents. "
            "If the answer cannot be found in the text, say 'I cannot find this information in the uploaded PDF.'\n\n"
            f"Extracted PDF Context:\n{retrieved_context}"
        )

        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            # temperature=0.2,
            max_completion_tokens=800
        )

        # 5. Output Result
        print("\n" + "="*40)
        print("SEARCH RESULT & GENERATED ANSWER:")
        print("="*40)
        print(response.choices[0].message.content)
        print("\n[Source Document(s):", ", ".join(set(sources_found)), "]")

    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == '__main__':
    main()