from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import extract_text_from_pdfs, embed_chunks, retrieve_similar_chunks
from app.gemini_api import generate_response

app = FastAPI()
chunks = extract_text_from_pdfs(r"D:\AI Agent Task\RAG PDF\ragpdf\app\data")
index, all_chunks = embed_chunks(chunks)

class QueryRequest(BaseModel):
    query: str

@app.get("/fine-prints")
def get_fine_prints():
    prompt = (
        "From the following content, extract only critical 'fine-print' clauses relevant to legal, financial, or project requirements:\n\n"
        + "\n\n".join(chunks[:10])
    )
    response = generate_response(prompt)
    with open("fine_prints.txt", "w") as f:
        f.write(response)
    return {"fine_prints": response}

@app.post("/chat")
def chat(request: QueryRequest):
    # Retrieve relevant chunks (context)
    context_chunks = retrieve_similar_chunks(request.query, index, all_chunks)
    context = "\n".join(context_chunks)

    # Build prompt
    prompt = (
        f"You are a helpful assistant answering questions from project documents.\n"
        f"Context:\n{context}\n\n"
        f"Question: {request.query}\nAnswer:"
    )

    # Generate response from LLM
    response = generate_response(prompt)

    # Return both response and the retrieved context for evaluation/debugging
    return {
        "response": response,
        "retrieved_context": context
    }