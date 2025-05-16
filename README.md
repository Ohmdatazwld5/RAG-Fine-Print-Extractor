# RAG-Fine-Print-Extractor
A lightweight and efficient Retrieval-Augmented Generation (RAG) system that extracts "fine print" clauses from PDF documents and answer user queries using Google's Gemini LLM. Built with FastAPI, FAISS, and SentenceTransformers.

🚀 Features
📄 PDF Parsing: Reads and processes all PDFs in a given folder.

🔍 Chunking & Embedding: Chunks the text with overlap and encodes using all-MiniLM-L6-v2.

📚 Semantic Search: Uses FAISS to retrieve semantically relevant text based on user queries.

🤖 LLM-Powered Responses: Uses Gemini API to extract fine prints and answer questions in context.

🌐 API Endpoints:

/fine-prints: Extracts fine-print clauses from the document.

/chat: Answers a user question using retrieved context.

# 🛠️ Installation

git clone https://github.com/yourusername/RAG-FinePrints.git
cd RAG-FinePrints

Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies
pip install -r requirements.txt

#📁 Project Structure
RAG-FinePrints/
├── app/
│   ├── rag.py                # PDF processing, chunking, embedding, and retrieval
│   ├── gemini_api.py         # Gemini LLM integration via Google API
│   └── data/                 # Folder containing PDF documents
├── main.py                   # FastAPI app with endpoints
├── .env                      # Environment variable with GOOGLE_API_KEY
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation


#🔐 Environment Variables

GOOGLE_API_KEY=your_google_genai_api_key_here

#🧪 Running the App

uvicorn main:app --reload
Visit: http://127.0.0.1:8000/docs for the Swagger UI.

#📦 Requirements

Sample requirements.txt:

fastapi
uvicorn
python-dotenv
google-generativeai
sentence-transformers
faiss-cpu
PyMuPDF

#💡 Use Cases

Legal/contract analysis

Financial document QA

RAG prototypes with Gemini

Context-aware assistants for documents




