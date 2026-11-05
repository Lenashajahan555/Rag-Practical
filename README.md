Enterprise PDF RAG System

An end-to-end Retrieval-Augmented Generation (RAG) system built with Azure AI Search and Azure AI Foundry. This application enables users to query uploaded PDF documents (e.g., hotel directory listings) and retrieve grounded, verifiable context via modern AI model endpoints.

🏗️ System Architecture

Document Storage & Ingestion: Raw PDF files are stored in Azure Blob Storage.

Knowledge Base (Search Indexing): Azure AI Search extracts text content, chunks the data, and builds a searchable vector/keyword index.

Retrieval Phase: The Python application queries Azure AI Search for relevant document excerpts based on user input.

Generation Phase: Retrieved text chunks are injected into a system prompt and processed by an Azure AI Foundry deployed model to generate a strict, non-hallucinated response.

🛠️ Prerequisites & Setup

1. Azure Configuration

Azure AI Search Service: Search index created over your uploaded PDF storage container.

Azure AI Foundry: Active deployment of a Chat/Reasoning Model (e.g., o3-mini, gpt-4o).

2. Local Environment Setup

Create and activate a virtual environment:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


Install required dependencies:

pip install openai azure-search-documents python-dotenv


🔑 Environment Variables (.env)

Create a .env file in the project root directory with the following configuration:

# Azure AI Foundry Model Endpoint & Key
FOUNDRY_INFERENCE_ENDPOINT=https://your-model-name.region.models.ai.azure.com/openai/v1/
FOUNDRY_API_KEY=your_foundry_model_api_key

# Azure AI Search Service Credentials
AZURE_SEARCH_ENDPOINT=https://your-search-service-name.search.windows.net
AZURE_SEARCH_KEY=your_search_service_query_or_admin_key
AZURE_SEARCH_INDEX=your-pdf-index-name


🚀 Running the Application

Execute the main script:

python app.py


Example Prompt & Workflow

Run the script and type your prompt (e.g., list of hotels in dubai).

The script queries your Azure AI Search index for relevant PDF paragraphs.

The retrieved content is passed to your Foundry model deployment.

The final answer is displayed along with the cited source document references.

⚙️ Model-Specific Compatibility Notes

When connecting modern reasoning models (such as o1 or o3-mini) via standard OpenAI client integration:

Use max_completion_tokens instead of legacy max_tokens.

Omit custom temperature settings if the deployed model strictly enforces default sampling parameters.