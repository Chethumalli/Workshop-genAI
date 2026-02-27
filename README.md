# 🚀 Workshop-genAI

A hands-on Generative AI Workshop project demonstrating how to build real-world LLM applications using FastAPI, Groq/OpenAI APIs, and structured AI pipelines.

---

## 📌 Overview

Workshop-genAI is a practical implementation project designed to teach:

- Large Language Model (LLM) integration
- Prompt engineering
- FastAPI backend development
- Modular AI architecture
- Retrieval-Augmented Generation (RAG)
- AI evaluation techniques

This repository is structured as workshop modules, each building on the previous one.

---

## 🧠 Workshop Modules

### 📦 Module 1 – AI Concept Explainer
- Prompt-based system
- Multiple explanation modes (Shakespeare, Pirate, Bandit)
- Demonstrates system + user prompt control

### 📦 Module 2 – Structured Answer Generator
- FastAPI application
- Returns structured JSON responses
- Basic LLM integration

### 📦 Module 3 – LLM Application Architecture
- Clean layered architecture
- input_layer.py
- prompt_layer.py
- llm_layer.py
- post_processing.py
- pipeline.py
- Separation of concerns (real-world AI system design)

### 📦 Module 4 – Evaluation System
- Output validation
- Structured scoring
- Basic AI response evaluation methods

### 📦 Module 5 – RAG (Retrieval-Augmented Generation)
- Keyword-based retrieval
- knowledge_base/ folder
- retriever.py
- rag_pipeline.py
- LiteLLM integration
- CLI-based interactive Q&A

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Groq API
- OpenAI API
- LiteLLM
- Uvicorn
- VS Code

---

## 📁 Project Structure

```
Workshop-genAI/
│
├── m1-ai-concept-explainer/
├── m2-structured_ans_generator/
├── m3-architecture/
├── m4-evalution/
├── m5-rag/
│   ├── knowledge_base/
│   ├── retriever.py
│   ├── llm_layer.py
│   ├── rag_pipeline.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```
git clone https://github.com/Chethumalli/Workshop-genAI.git
cd Workshop-genAI
```

### 2️⃣ Create Virtual Environment

Windows:
```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file in root directory:

```
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

---

## ▶️ Running Applications

### For FastAPI modules:

```
uvicorn app:app --reload
```

Open:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

### For RAG CLI module:

```
python main.py
```

---

## 🔍 How It Works

1. User enters prompt
2. Input layer validates data
3. Prompt layer constructs structured prompt
4. LLM layer calls Groq/OpenAI
5. Post-processing formats output
6. Final structured response is returned

For RAG:
1. Query entered
2. Retriever searches knowledge base
3. Retrieved context injected into prompt
4. LLM generates context-aware answer

---

## 🚀 Key Learnings

- Prompt engineering controls output
- Architecture matters in AI systems
- RAG improves factual accuracy
- Modular design makes AI scalable
- Clean separation of layers prevents chaos

---

## 🌟 Future Improvements

- Vector database integration (FAISS / Pinecone)
- Docker support
- Frontend UI
- Cloud deployment
- Streaming responses
- Authentication system
- Fine-tuned custom models

---

## 🤝 Contribution

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

## 👨‍💻 Author

Chethan Malli  
AI & ML Enthusiast  
GitHub: https://github.com/Chethumalli

---

⭐ If this workshop helped you, please star the repository!
