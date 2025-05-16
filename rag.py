import os
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdfs(pdf_dir: str) -> list[str]:
    chunks = []
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            doc = fitz.open(os.path.join(pdf_dir, file))
            for page in doc:
                text = page.get_text()
                chunks.extend(split_text(text))
    return chunks

def split_text(text: str) -> list[str]:
    words = text.split()
    chunks = []
    for i in range(0, len(words), CHUNK_SIZE - CHUNK_OVERLAP):
        chunk = " ".join(words[i:i + CHUNK_SIZE])
        if chunk.strip():
            chunks.append(chunk)
    return chunks

def embed_chunks(chunks: list[str]):
    embeddings = EMBED_MODEL.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, chunks

def retrieve_similar_chunks(query: str, index, chunks, top_k=5):
    query_vector = EMBED_MODEL.encode([query])
    D, I = index.search(np.array(query_vector), top_k)
    return [chunks[i] for i in I[0]]