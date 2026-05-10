# E-Commerce Customer Support Chatbot

A RAG-based (Retrieval-Augmented Generation) customer support agent built on top of a demo e-commerce website. The agent answers customer questions about products using semantic search and a Groq LLM.

## Project Structure

```
project/
├── website/              # Downy e-commerce HTML template
├── chatbot/
│   ├── ecommerce_api.py  # Fetches product data from FakeStore API
│   ├── chunker.py        # Splits products into text chunks
│   ├── embedder.py       # Generates embeddings using sentence-transformers
│   ├── vector_store.py   # Stores vectors and searches via cosine similarity
│   └── agent.py          # Core agent logic using Groq LLM
├── server.py             # Flask backend connecting website and chatbot
├── requirements.txt      # Python dependencies
└── .env                  # API keys (not committed)
```

## How It Works

```
FakeStore API → Chunking → Embeddings → Vector Store
                                              ↓
User Question → Embed → Search → Top Chunks → Groq LLM → Reply
```

1. At startup, product data is fetched, chunked into 100 pieces, and embedded using `all-MiniLM-L6-v2`
2. When a user asks a question, it is embedded and compared against all chunks using cosine similarity
3. Top 5 relevant chunks are sent as context to the Groq LLM
4. The LLM generates a natural language reply shown in the chat widget

## Tech Stack

| Component | Technology |
|---|---|
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Search | NumPy cosine similarity |
| LLM | Groq (llama-3.1-8b-instant) |
| Backend | Flask |
| Frontend | HTML/CSS/JavaScript (Downy template) |
| Data Source | FakeStore API |

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your Groq API key
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get a free API key at [console.groq.com](https://console.groq.com)

### 3. Run the Flask server
```bash
python server.py
```

### 4. Open the website
Open `website/index.html` in your browser and click the **💬 Support** button.

## Example Questions

- "Do you have any electronics under $100?"
- "What is the rating of the backpack?"
- "Show me women's clothing products"
- "Tell me about your jewelry collection"
- "What is your return policy?"
