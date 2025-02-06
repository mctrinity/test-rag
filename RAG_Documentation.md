# Retrieval-Augmented Generation (RAG) Documentation

## Overview

Retrieval-Augmented Generation (RAG) is an AI architecture that combines **information retrieval** with **language generation** to improve the accuracy and reliability of responses. Instead of relying purely on an LLM's internal knowledge, RAG retrieves **real-world documents** to provide factual grounding before generating an answer.

## How RAG Works

RAG operates in two stages:

### 1️⃣ **Retrieval (FAISS Vector Store + Web Search)**

- The system **stores pre-verified documents** in a FAISS (Facebook AI Similarity Search) index.
- When a user asks a question, the system **retrieves the most relevant documents** based on similarity search.
- If FAISS does not return useful results, a **live web search (Bing, Google, etc.)** is triggered.
- FAISS results + web search results are **combined** for a richer context before being passed to the LLM.

#### **Understanding `top_k` Retrieval**

- `top_k` controls **how many relevant documents** FAISS retrieves.
- **Higher `top_k` values** return more context, which can improve response accuracy.
- **Lower `top_k` values** make retrieval faster but may provide less relevant information.
- Example:
  - `top_k=1` → Only the most relevant document is retrieved.
  - `top_k=3` → Three relevant documents are retrieved and combined for a better response.

### 2️⃣ **Generation (LLM - GPT-3.5 or GPT-4)**

- The retrieved documents + web search results are **combined with the user's question** and sent to an LLM.
- The LLM uses its reasoning capabilities to **structure, summarize, and refine** the response.
- This prevents the model from making up facts (hallucinations) and ensures **accuracy and coherence**.

## Handling Missing Information in RAG

### **What Happens When No Relevant Data is Found?**
If FAISS does not contain any matching documents for a query, the LLM needs to handle the situation appropriately to avoid hallucinations. By default, RAG can:

✅ **Trigger a live web search** to fetch up-to-date results.
✅ **Acknowledge the lack of information** rather than fabricate an answer.  
✅ **Provide alternative sources** (e.g., official websites, references).  
✅ **Guide the user on how to find more reliable information.**  

### **Example Behavior When No Data is Found:**

#### **User Query:** "Who is Mary Jones from ABC Company?"

#### **RAG Response:**
```
I'm sorry, but I couldn't find the specific information about Mary Jones from ABC Company in our database. However, I performed a web search and found the following sources:

1. ABC Company website: [ABC Company](https://www.abccompany.com/)
2. LinkedIn profile of Mary Jones: [Mary Jones on LinkedIn](https://www.linkedin.com/)

Please visit these websites for more accurate information regarding Mary Jones and ABC Company.
```

### **How to Improve Handling of Missing Information**

1. **Expand the FAISS Document Store**
   - Add more factual documents related to entities you expect to be queried frequently.

2. **Improve Prompt Engineering**
   - Modify how the LLM handles missing retrievals:
     ```python
     if not retrieved_docs:
         retrieved_docs = web_search(query)  # Trigger web search
         prompt = f"Question: {query}\nRetrieved Information: {' '.join(retrieved_docs)}\nAnswer:"
     ```
   - This ensures the LLM processes real-time information when FAISS retrieval fails.

3. **Use a Hybrid Approach (FAISS + Web Search)**
   - Combine FAISS retrieval with **live web search** (e.g., Bing API, Google Search API) for real-time results.

## Sentence Transformer Model

The **Sentence Transformer model** is responsible for converting text queries and documents into **vector embeddings** that can be efficiently compared in FAISS.

### **How It Works**

1. **Text Input:** The query and documents are fed into a **sentence transformer model** (e.g., `all-MiniLM-L6-v2`).
2. **Vector Embeddings:** The model generates numerical vector representations for the text.
3. **Similarity Search:** FAISS compares the vector representation of the query against stored document vectors to retrieve the most relevant ones.

### **Why Use a Sentence Transformer?**

✅ **Efficient Text Representation** – Converts words into vectors that capture meaning.  
✅ **Improved Retrieval Accuracy** – Finds semantically similar documents, not just keyword matches.  
✅ **Pre-trained and Optimized** – Models like `all-MiniLM-L6-v2` are optimized for fast and accurate retrieval.  

## RAG Engine Workflow

RAG follows a structured process to ensure factual and coherent answers:

1. **User Query Processing**: The user inputs a question.
2. **Embedding Generation**: The query is converted into a vector representation using a sentence transformer model.
3. **Document Retrieval**: FAISS searches for the most relevant stored document embeddings and retrieves them.
4. **Web Search Trigger (if needed)**: If FAISS retrieval is insufficient, a live web search is performed.
5. **Context Combination**: The retrieved documents and web search results are formatted into a structured context for the LLM.
6. **LLM Processing**:
   - The LLM receives both the original query and the retrieved context.
   - It generates a coherent and accurate response based on the retrieved information.
7. **Final Response Output**: The enhanced answer is returned to the user.

## Why Use RAG?

✅ **Combines stored + real-time knowledge** for better accuracy.  
✅ **Reduces hallucination** since the LLM is using external knowledge instead of generating from memory.  
✅ **Provides updated knowledge** by integrating new documents without retraining the model.  
✅ **Enhances responses** by structuring retrieved information into a well-formed answer.  

## Example Workflow

1. **User Query:** "Where is the Eiffel Tower?"
2. **Retrieval Step:** FAISS finds the document: *"The Eiffel Tower is located in Paris, France."*
3. **Generation Step:** The LLM processes the retrieved document and enhances it into:
   > "The Eiffel Tower, located in Paris, France, was designed by Gustave Eiffel and completed in 1889. It stands at 330 meters tall and is one of the most famous landmarks in the world."

## Enhancements & Customization

- **Increase `top_k` retrieval** to fetch multiple documents for more context.
- **Use hybrid retrieval** (FAISS + Web Search) for better accuracy.
- **Improve the prompt** to force the LLM to admit when it doesn’t know the answer.

## Want to See RAG in Action?

Run the Python script that initializes FAISS and queries the LLM using retrieved data. Modify the function to experiment with different retrieval techniques!

---

🚀 **RAG bridges the gap between search and generation, making AI responses more reliable and informed!**

