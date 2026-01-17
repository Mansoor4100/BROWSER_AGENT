📄 RAG-Based Document Question Answering System
<p align="center"> <img src="https://raw.githubusercontent.com/langchain-ai/langchain/master/docs/static/img/langchain_stack.png" width="120" alt="RAG Logo"/> </p> <p align="center"> <b>An end-to-end Retrieval-Augmented Generation (RAG) system for answering questions strictly from uploaded documents.</b> </p> <p align="center"> Built with <b>FastAPI</b>, <b>FAISS</b>, <b>HuggingFace LLMs</b>, and <b>Streamlit</b> — runs fully on CPU. </p>
🚀 Key Features

📂 Upload multiple PDF documents

🔍 Semantic search using FAISS vector database

🤖 Context-aware answers using FLAN-T5

❌ No hallucinations — answers only from documents

🧠 Sentence-transformer based embeddings

🖥️ Clean Streamlit UI

⚙️ FastAPI backend with modular RAG pipeline

💻 CPU-only execution (no GPU required)

🏗️ Tech Stack
Layer	Technology
Backend	FastAPI
Frontend	Streamlit
LLM	google/flan-t5-large (HuggingFace)
Embeddings	sentence-transformers/all-MiniLM-L6-v2
Vector DB	FAISS
PDF Loader	PyPDFLoader
Language	Python 3.10+
📁 Project Structure
rag-doc-qa/
│
├── back/
│   ├── app.py                # FastAPI backend
│   ├── rag_pipeline.py       # Retrieval + Generation logic
│   ├── ingest.py             # PDF ingestion & FAISS indexing
│   ├── faiss_index/          # Vector store
│   └── uploads/              # Uploaded PDFs
│
├── frontend/
│   └── streamlit_app.py      # Streamlit UI
│
├── venv/
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/rag-doc-qa.git
cd rag-doc-qa

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Application
🔹 Start Backend (FastAPI)
cd back
uvicorn app:app --reload


Backend available at:

http://127.0.0.1:8000

🔹 Start Frontend (Streamlit)
cd frontend
streamlit run streamlit_app.py


Frontend available at:

http://localhost:8501

🧪 How It Works

User uploads one or more PDF files

PDFs are split into semantic chunks

Chunks are embedded using sentence-transformers

Embeddings are stored in FAISS

User asks a question

Relevant chunks are retrieved

LLM generates an answer only from retrieved context

🛡️ Hallucination Control

The system is designed to avoid hallucinations by:

Using strict prompt instructions

Restricting answers to retrieved chunks only

Returning “I don’t know” when context is missing

No external knowledge injection

📸 Demo (Add to GitHub)

You can include:

Screenshots of Streamlit UI

PDF upload flow

Question → Answer output

Optional demo GIF

Example:

![Demo](demo.gif)

📌 Future Improvements

Source citations with page numbers

Chat history & conversational memory

React / Next.js frontend

Dockerized deployment

Cloud hosting (HF Spaces / AWS / Render)

RAG evaluation metrics

Multi-document comparison

👨‍💻 Author

Shaik Nabi Mansoor
AI | Machine Learning | Agentic Systems | Full-Stack Development

⭐ Why This Project Matters

This project demonstrates:

Real-world RAG architecture

Strong ML + backend integration

Practical handling of LLM limitations

Clean, scalable, production-ready design

Recruiter-relevant AI system building
