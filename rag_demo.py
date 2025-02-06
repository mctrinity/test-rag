from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 1: Initialize Embedding Model & FAISS Index
embed_model = SentenceTransformer('all-MiniLM-L6-v2')
faiss_index = faiss.IndexFlatL2(384)  # 384-dimensional embeddings

documents = [
    "The Eiffel Tower is located in Paris, France.",
    "The Great Wall of China is one of the seven wonders of the world.",
    "The Moon landing happened in 1969.",
    "Water boils at 100 degrees Celsius at sea level."
]

# Encode and add documents to FAISS index
embeddings = embed_model.encode(documents)
faiss_index.add(np.array(embeddings, dtype=np.float32))

# Step 2: Function to Perform RAG
def retrieve_and_generate(query, top_k=1):
    query_embedding = embed_model.encode([query])
    distances, indices = faiss_index.search(np.array(query_embedding, dtype=np.float32), top_k)
    retrieved_docs = [documents[idx] for idx in indices[0]]

    prompt = f"Question: {query}\nRetrieved Information: {' '.join(retrieved_docs)}\nAnswer:"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    
    return response.choices[0].message.content.strip()

# Example Usage
query = "Who and why the Eiffel Tower was built"
response = retrieve_and_generate(query)
print(response)
