from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 1: Function to Use Pure LLM

def generate_answer(query):
    prompt = f"Question: {query}\nAnswer:"
    
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
query = "Who is Ricky Li of Nowcom Corporation?  Can you provide urls for the verfication?"
response = generate_answer(query)
print(response)
