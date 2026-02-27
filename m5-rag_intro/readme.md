# 📚 Module 5 — Introduction to RAG (Retrieval-Augmented Generation)

## 📌 Overview

This module demonstrates a **simple Retrieval-Augmented Generation (RAG) pipeline** using:

- 🔎 Keyword-based document retrieval
- ⚡ LiteLLM for LLM abstraction
- 🔥 Groq API for generation

Instead of directly asking the LLM, we first retrieve relevant knowledge from local documents and then use that context to generate a more accurate answer.

This is the foundation of modern AI systems like ChatGPT with knowledge bases.

---

## 🎯 Objective

Build a basic RAG pipeline:

```
User Question 
      ↓
Document Retrieval (Keyword-Based)
      ↓
Context Injection
      ↓
LLM Generation
      ↓
Final Answer
```

The goal is to understand how LLMs can be grounded in external knowledge.

---

## 🧠 Concepts Covered

- Retrieval-Augmented Generation (RAG)
- Context injection
- Keyword-based retrieval logic
- LLM abstraction using LiteLLM
- Modular AI pipeline design
- Local knowledge base usage
- Production-style separation of components

---

## 📂 Project Structure

```
Module5_RAG/
│
├── knowledge_base/        # Text files used as retrieval source
│
├── retriever.py           # Loads documents & performs keyword retrieval
├── llm_layer.py           # Handles LiteLLM model interaction
├── rag_pipeline.py        # Connects retrieval + generation
├── main.py                # Interactive CLI for user questions
│
├── requirements.txt       # Dependencies
└── .env.example           # Example environment configuration
```

---

## 🏗 How the RAG Pipeline Works

### 1️⃣ Knowledge Base
Contains `.txt` files with domain-specific information.

---

### 2️⃣ Retriever (`retriever.py`)
- Loads all documents
- Performs simple keyword matching
- Selects relevant text chunks

---

### 3️⃣ LLM Layer (`llm_layer.py`)
- Sends context + question to Groq via LiteLLM
- Handles model configuration
- Returns generated response

---

### 4️⃣ RAG Pipeline (`rag_pipeline.py`)
- Accepts user query
- Retrieves relevant context
- Injects context into prompt
- Calls LLM
- Returns final answer

---

### 5️⃣ Main CLI (`main.py`)
- Interactive interface
- Takes user input
- Displays final AI response

---

## ⚙ Setup Instructions

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the Application

```bash
python main.py
```

You can now ask questions, and the system will:

1. Search the knowledge base  
2. Retrieve relevant content  
3. Inject context into the prompt  
4. Generate grounded answers  

---

## 🧾 Example Flow

If your knowledge base contains AI-related documents:

**User Question:**  
> What is prompt engineering?

**System Process:**
- Finds documents mentioning "prompt engineering"
- Extracts relevant paragraphs
- Sends them to the LLM with the question
- Generates contextual answer

---

## 🎓 Learning Outcomes

After completing this module, you will:

✔ Understand how RAG works  
✔ Build a basic retrieval system  
✔ Combine retrieval + generation  
✔ Ground LLM responses in external knowledge  
✔ Design modular GenAI architectures  

---

## 🚀 Why RAG Matters

Large Language Models:

- Do NOT have real-time knowledge  
- Can hallucinate  
- Cannot access private documents by default  

RAG solves this by:

- Injecting trusted context  
- Reducing hallucinations  
- Enabling domain-specific AI systems  
- Powering enterprise AI assistants  

This is the core architecture behind:

- Chatbots with knowledge bases  
- AI customer support systems  
- Internal enterprise AI tools  

---

## 🔮 Possible Improvements

- Replace keyword retrieval with embeddings
- Add vector database (FAISS / Chroma)
- Add chunking strategy
- Add similarity scoring
- Convert to FastAPI service
- Add web interface
- Add streaming responses
- Add caching layer

---

## 👨‍💻 Author

Chethan Malli  
AI & ML Enthusiast  
Building modular AI systems 🚀  

---

⭐ If this module helped you understand RAG, give the repo a star!
