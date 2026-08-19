# WikiRAG 📚

A conversational Retrieval-Augmented Generation (RAG) assistant that allows users to load a Wikipedia article and ask questions about its content through a natural-language chat interface.

The system combines dense semantic retrieval, BM25 keyword retrieval, hybrid search, and Cross-Encoder reranking to improve the relevance of information supplied to the LLM.

---

## 🚀 Features

- 📖 Dynamic Wikipedia article loading
- ✂️ Document chunking for efficient retrieval
- 🧠 Dense semantic retrieval using sentence embeddings
- 🔎 BM25 keyword-based retrieval
- 🔀 Hybrid retrieval combining semantic and keyword search
- 🎯 Cross-Encoder reranking of retrieved documents
- 💬 Conversational memory for follow-up questions
- 🤖 Llama-based LLM inference through Groq
- 🗄️ ChromaDB vector storage
- 🌐 Streamlit web interface

---

## 🏗️ Architecture

```text
                    User
                     │
                     ▼
             Streamlit Interface
                     │
                     ▼
            Conversational Memory
                     │
                     ▼
                User Query
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
   Dense Retrieval          BM25 Retrieval
   (Embeddings)             (Keywords)
          │                     │
          └──────────┬──────────┘
                     ▼
              Hybrid Retrieval
                     │
                     ▼
          Cross-Encoder Reranker
                     │
                     ▼
              Top-K Context
                     │
                     ▼
              Prompt Builder
                     │
                     ▼
                 Groq LLM
                     │
                     ▼
                Final Answer
```

---

## 🧠 How It Works

### 1. Wikipedia Loading

The user provides a Wikipedia topic. The application retrieves the corresponding article and extracts its textual content.

### 2. Document Chunking

The article is divided into smaller chunks so that individual sections can be retrieved independently rather than passing the entire article to the LLM.

### 3. Embeddings

Each chunk is converted into a numerical vector representation using a Sentence Transformer embedding model.

### 4. Dense Retrieval

The user's question is converted into an embedding and compared against the stored document embeddings in ChromaDB. The system retrieves chunks that are semantically similar to the query.

### 5. BM25 Retrieval

BM25 performs keyword-based retrieval in parallel. This complements semantic retrieval by handling exact terms, names, numbers, and other lexical matches effectively.

### 6. Hybrid Retrieval

The results from dense retrieval and BM25 are combined to create a broader set of candidate documents.

### 7. Cross-Encoder Reranking

The retrieved candidate chunks are passed through a Cross-Encoder, which evaluates the relevance of each query-document pair. The highest-scoring chunks are selected as the final context.

### 8. Conversational Memory

Previous user questions and assistant responses are maintained within the Streamlit session. This allows the assistant to use previous conversation context when answering follow-up questions.

### 9. Answer Generation

The retrieved context, conversation history, and current question are passed to a Llama-based LLM through Groq. The model generates a grounded response using the retrieved information.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | RAG and LLM application components |
| ChromaDB | Vector storage and similarity search |
| Sentence Transformers | Embeddings and Cross-Encoder reranking |
| BM25 | Keyword-based retrieval |
| Groq | LLM inference |
| Streamlit | Web application interface |
| Wikipedia API | Knowledge source |

---

## 📁 Project Structure

```text
WikiRAG/
│
├── src/
│   ├── bm25_retriever.py
│   ├── dense_retriever.py
│   ├── hybrid_retriever.py
│   ├── rag_pipeline.py
│   ├── reranker.py
│   ├── llm.py
│   ├── prompt.py
│   └── vector_store.py
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Harish-Rajasekar/Wikirag.git
cd Wikirag
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

The `.env` file is included in `.gitignore` and should never be committed to GitHub.

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

### Usage

1. Enter a Wikipedia topic.
2. Click **Load Article**.
3. Ask questions about the article.
4. Continue the conversation using follow-up questions.

---

## 💡 Example

```text
Topic:
Lewis Hamilton

User:
How many championships does he have?

Assistant:
He has 7 World Championship titles.

User:
What teams has he raced for?

Assistant:
He has raced for McLaren and Mercedes.

User:
His current team?

Assistant:
Ferrari.
```

---

## 🎯 Key Learning Outcomes

This project provided practical experience with:

- Retrieval-Augmented Generation (RAG)
- Vector databases
- Dense semantic retrieval
- Sparse keyword retrieval
- BM25
- Hybrid information retrieval
- Cross-Encoder reranking
- Conversational AI
- Prompt construction
- LLM application architecture
- Modular AI system design
- Building an end-to-end RAG application

---

## 🔮 Future Improvements

Potential extensions include:

- History-aware query rewriting
- Reciprocal Rank Fusion (RRF)
- PDF and document ingestion
- Multiple knowledge sources
- Retrieval evaluation using Recall@K and MRR
- Persistent vector storage
- Production deployment

---

## 👨‍💻 Author

**Harish R**

Built as a practical exploration of Retrieval-Augmented Generation, information retrieval, and conversational AI.
