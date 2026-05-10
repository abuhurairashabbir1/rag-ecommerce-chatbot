import os
from groq import Groq
from dotenv import load_dotenv

from chatbot.ecommerce_api import get_cleaned_products
from chatbot.chunker import chunk_products
from chatbot.embedder import embed_chunks, embed_query
from chatbot.vector_store import build_store, search

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def initialize():
    print("Loading products from FakeStore API...")
    products = get_cleaned_products()

    print("Chunking products...")
    chunks = chunk_products(products)

    print("Generating embeddings...")
    vectors = embed_chunks(chunks)

    print("Building vector store...")
    build_store(chunks, vectors)

    print("Agent ready!\n")

def build_context(results):
    lines = []
    for i, r in enumerate(results, 1):
        lines.append(f"{i}. {r['text']}")
    return "\n".join(lines)

def ask(question):
    q_vector = embed_query(question)
    results  = search(q_vector, top_k=5)
    context  = build_context(results)

    system_prompt = """You are a helpful and friendly customer support agent for an online shop.
Answer the customer's question using ONLY the context provided below.
If the answer is not in the context, politely say you don't have that information.
Keep your answers short, clear and helpful."""

    user_prompt = f"""Context:
{context}

Customer Question: {question}

Answer:"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt}
        ]
    )

    return response.choices[0].message.content
