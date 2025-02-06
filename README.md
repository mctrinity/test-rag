# Retrieval-Augmented Generation (RAG) - Setup & Installation

## 📌 Overview
This repository contains an implementation of **Retrieval-Augmented Generation (RAG)** using:
- **FAISS (Facebook AI Similarity Search)** for document retrieval
- **OpenAI’s GPT-3.5/GPT-4** for response generation
- **SentenceTransformers** for embedding text into vectors

With RAG, we enhance AI responses by retrieving real-world knowledge before generating an answer.

---

## 🛠️ Installation
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/rag-project.git
cd rag-project
```

### 2️⃣ **Create a Virtual Environment (Optional, Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate    # For Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Keys
This project requires an **OpenAI API Key** to generate responses.

### 1️⃣ **Create a `.env` File**
Inside the project directory, create a `.env` file and add your API key:
```ini
OPENAI_API_KEY=your_openai_api_key_here
```

### 2️⃣ **Ensure API Key is Loaded in the Script**
The script automatically loads API keys from the `.env` file using `dotenv`.

If you haven't installed `python-dotenv`, install it:
```bash
pip install python-dotenv
```

---

## 🚀 Running the RAG System
To test the retrieval-augmented generation system, run:
```bash
python rag_demo.py
```
Example:
```bash
$ python rag_demo.py
Where is the Eiffel Tower?
The Eiffel Tower is located in Paris, France, and was designed by Gustave Eiffel.
```

---

## ⚙️ How It Works
1. **FAISS stores and retrieves** relevant documents based on the user query.
2. **The LLM (GPT-3.5/GPT-4) processes the retrieved text** to refine the response.
3. **A final answer is generated** that is more accurate and well-structured.

---

## ✅ Features
- 🔍 **Accurate information retrieval with FAISS**
- 🤖 **Enhanced response generation using GPT-3.5/GPT-4**
- ⚡ **Efficient text embeddings with SentenceTransformers**
- 🔧 **Customizable retrieval settings (`top_k`, hybrid search)**

---

## 📌 Customization
### **Modify Retrieval Settings**
In `rag_demo.py`, you can change:
```python
def retrieve_and_generate(query, top_k=3):
```
Increasing `top_k` retrieves more documents for better context.

---

## 📚 References
- [FAISS Documentation](https://faiss.ai/)
- [OpenAI API](https://platform.openai.com/docs/)
- [SentenceTransformers](https://www.sbert.net/)

---

🚀 **Now you’re ready to use RAG!** Modify and experiment with retrieval methods to improve AI-generated responses!

