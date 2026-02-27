# 🚀 Workshop-genAI

> A Complete Hands-On Generative AI Workshop  
> Learn how to build production-ready LLM applications step-by-step.

---

## 🌟 About This Repository

**Workshop-genAI** is a structured, module-based learning repository designed to teach how modern AI systems (like ChatGPT) are built in real-world architecture.

Instead of just calling an API, this workshop focuses on:

- 🧠 Prompt Engineering
- 🏗 Clean AI System Architecture
- 📊 Evaluation & Validation
- 📚 Retrieval-Augmented Generation (RAG)
- 🤖 AI Agents & Multi-Step Reasoning
- ⚙️ FastAPI Backend Integration

This is not just theory — it’s implementation-focused.

---

# 📦 Workshop Modules

---

## 🧩 Module 1 — AI Concept Explainer

### 🎯 Goal:
Understand how prompt engineering controls AI behavior.

### Features:
- System Prompt + User Prompt separation
- Multiple explanation styles:
  - Shakespeare Mode
  - Pirate Mode
  - Bandit Mode
- Dynamic response control

### Key Learning:
Prompt engineering directly influences structure, tone, and complexity.

---

## 🧩 Module 2 — Structured Answer Generator

### 🎯 Goal:
Build a real FastAPI app integrated with an LLM.

### Features:
- FastAPI backend
- Structured JSON output
- API endpoint handling
- Swagger documentation support

### Example Output:
```json
{
  "topic": "Neural Networks",
  "definition": "...",
  "applications": ["..."],
  "advantages": ["..."]
}
```

---

## 🧩 Module 3 — LLM Application Architecture

### 🎯 Goal:
Design a scalable AI system using clean software engineering principles.

### Architecture Layers:

```
User Input
   ↓
Input Layer
   ↓
Prompt Layer
   ↓
LLM Layer
   ↓
Post Processing
   ↓
Final Output
```

### Files:
- `input_layer.py`
- `prompt_layer.py`
- `llm_layer.py`
- `post_processing.py`
- `pipeline.py`

### Key Learning:
Real AI systems require modular separation of concerns.

---

## 🧩 Module 4 — Evaluation System

### 🎯 Goal:
Evaluate AI outputs for correctness and structure.

### Features:
- Structured validation
- Output scoring
- Quality metrics
- Automated evaluation logic

### Why It Matters:
AI systems must be measured — not blindly trusted.

---

## 🧩 Module 5 — Retrieval-Augmented Generation (RAG)

### 🎯 Goal:
Improve AI accuracy using external knowledge.

### How It Works:

```
User Query
   ↓
Keyword Retrieval
   ↓
Relevant Documents
   ↓
Context Injection
   ↓
LLM Generates Context-Aware Response
```

### Components:
- `knowledge_base/`
- `retriever.py`
- `llm_layer.py`
- `rag_pipeline.py`
- `main.py`

### Key Learning:
RAG reduces hallucination and increases factual accuracy.

---

## 🧩 Module 6 — AI Agents & Automation Thinking

### 🎯 Goal:
Build a multi-step AI Agent with tool orchestration.

### Mini Project:
### 📄 Resume Review AI Agent

Workflow:

```
User Input (Resume + Job Description)
        ↓
Step 1: Extract Skills (Tool)
        ↓
Step 2: Compare Skills (Tool)
        ↓
Step 3: Suggest Improvements (LLM)
        ↓
Step 4: Score Resume (LLM)
        ↓
Final Structured Report
```

### Files:
- `tools.py`
- `agent_brain.py`
- `llm_layer.py`
- `main.py`

### Key Learning:
AI Agents break large problems into smaller logical steps.

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Language |
| FastAPI | Backend API Framework |
| Groq API | High-speed LLM Inference |
| OpenAI API | Model Access |
| LiteLLM | Unified LLM Interface |
| Uvicorn | ASGI Server |
| CLI | Interactive Interface |

---

# 📁 Full Project Structure

```
Workshop-genAI/
│
├── m1-ai-concept-explainer/
├── m2-structured_ans_generator/
├── m3-architecture/
├── m4-evaluation/
├── m5-rag/
│   ├── knowledge_base/
│   ├── retriever.py
│   ├── rag_pipeline.py
│   └── main.py
│
├── m6-agents/
│   ├── tools.py
│   ├── agent_brain.py
│   ├── llm_layer.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Chethumalli/Workshop-genAI.git
cd Workshop-genAI
```

## 2️⃣ Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Setup Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key
```

---

# ▶️ Running The Modules

## FastAPI Modules

```bash
uvicorn app:app --reload
```

Visit:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

---

## RAG Module

```bash
cd m5-rag
python main.py
```

---

## Agents Module

```bash
cd m6-agents
python main.py
```

---

# 🔬 Core Concepts Covered

- Prompt Engineering
- Structured JSON Generation
- API Integration
- Layered AI Architecture
- Evaluation Pipelines
- Retrieval Systems
- Agent-Based Systems
- Multi-Step Reasoning
- Tool Orchestration

---

# 🚀 Why This Repository Is Valuable

This workshop simulates how real AI startups build systems:

✔ Modular  
✔ Scalable  
✔ Structured  
✔ Measurable  
✔ Production-Oriented  

It moves beyond simple API calls into system design thinking.

---

# 📈 Future Roadmap

- 🔗 Vector Database Integration (FAISS / Pinecone)
- 🐳 Docker Support
- 🌐 Frontend UI Integration
- ☁ Cloud Deployment
- ⚡ Streaming LLM Responses
- 📊 Agent Performance Benchmarking
- 🔒 Authentication Layer

---

# 🤝 Contributing

1. Fork the repo  
2. Create feature branch  
3. Commit changes  
4. Push to GitHub  
5. Open Pull Request  

---

# 👨‍💻 Author

**Chethan Malli**  
AI & ML Enthusiast  
Building real-world AI systems 🚀  

GitHub: https://github.com/Chethumalli

---

# ⭐ Support

If this workshop helped you:

👉 Star the repository  
👉 Share with friends  
👉 Build something amazing  

---

**Workshop-genAI — From Prompt to Production.**
