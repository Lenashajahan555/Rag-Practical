# 🧠 Enterprise RAG Pipeline with LangChain

A robust, end-to-end Retrieval-Augmented Generation (RAG) system built using **LangChain** and Python. This pipeline ingests documents, processes them through advanced chunking and embedding strategies, stores them in a vector database, and leverages an LLM to provide context-aware, accurate answers.

---

## 🏗️ How the RAG Pipeline Works

This project follows a standard modular RAG workflow:

1. **Document Loading & Ingestion:** Raw documents (PDFs, Markdown, text, or web pages) are loaded into the pipeline.
2. **Chunking (Text Splitting):** Large documents are broken down into smaller, overlapping chunks (using `RecursiveCharacterTextSplitter`) to preserve semantic context and fit within LLM token windows.
3. **Embedding Generation:** Each text chunk is converted into high-dimensional vector representations using embedding models (e.g., OpenAI Embeddings, Hugging Face).
4. **Vector Storage & Indexing:** Vectors are stored and indexed in a vector database (e.g., Chroma, FAISS, or Pinecone) for ultra-fast similarity search.
5. **Retrieval & Generation:** When a user asks a query, the system retrieves the most relevant chunks, passes them as context to the LLM alongside the prompt, and generates a grounded response.

---

## 🛠️ Tech Stack & Libraries

* **Orchestration:** LangChain 
* **Language:** Python 3.14+
* **Vector Database:** Chroma / FAISS
* **LLM & Embeddings:** OpenAI / Hugging Face
* **Environment Management:** `python-dotenv`

---