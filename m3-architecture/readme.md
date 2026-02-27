# 🏗 Module 3 — LLM Application Architecture

## 📌 Overview

This module focuses on designing a **modular LLM application pipeline** using clean software engineering principles.

Instead of writing everything in one script, we separate responsibilities into independent layers — just like real-world AI production systems.

This module teaches you how to architect scalable and maintainable GenAI applications.

---

## 🎯 Objective

Build a structured LLM pipeline:

```
User Input → Prompt Layer → LLM Layer → Post-Processing → Output
```

The goal is to think like an AI system architect, not just a prompt writer.

---

## 🧠 Concepts Covered

- Modular AI system design
- Separation of concerns
- Prompt abstraction layer
- Model invocation layer
- Post-processing layer
- Production-style architecture
- Scalable GenAI design patterns

---

## 📂 Project Structure

```
module3_architecture/
│
├── input_layer.py          # Handles user interaction
├── prompt_layer.py         # Builds structured prompts
├── llm_layer.py            # Sends request to Groq via LiteLLM
├── post_processing.py      # Cleans & formats output
├── pipeline.py             # Orchestrates entire workflow
├── requirements.txt        # Dependencies
└── .env.example            # Example environment file
```

---

## 🏗 Architecture Overview

### 1️⃣ Input Layer
Responsible for:
- Collecting user input
- Basic validation
- Passing data to the pipeline

---

### 2️⃣ Prompt Layer
Responsible for:
- Constructing structured prompts
- Separating system and user instructions
- Applying formatting constraints
- Keeping prompt logic isolated from model logic

---

### 3️⃣ LLM Layer
Responsible for:
- Calling Groq via LiteLLM
- Managing model configuration
- Handling API communication
- Abstracting model provider details

---

### 4️⃣ Post-Processing Layer
Responsible for:
- Cleaning model output
- Formatting structured responses
- Removing unwanted tokens
- Preparing final output

---

### 5️⃣ Pipeline (Orchestrator)
Responsible for:
- Connecting all layers
- Managing data flow
- Handling execution order
- Acting as the application controller

---

## ⚙ Installation

### 1️⃣  Install Dependencies

```bash
pip install -r requirements.txt
```

---

###  Add Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_key_here
MODEL_NAME=groq/llama-3.1-8b-instant
```

⚠️ Important:
- Do NOT upload `.env` to GitHub
- Keep API keys private

---

## ▶ Run the Project

```bash
python pipeline.py
```

The pipeline will:

1. Accept user input  
2. Build a structured prompt  
3. Send it to the LLM  
4. Post-process the response  
5. Display final output  

---

## 🎓 Learning Outcome

After completing this module, you will:

✔ Understand AI workflow design  
✔ Build modular LLM systems  
✔ Separate prompt logic from model logic  
✔ Design scalable GenAI applications  
✔ Think like a production AI engineer  

---

## 🚀 Why This Matters

Real-world AI systems are NOT single scripts.

They are modular pipelines with:

- Input validation  
- Prompt engineering layer  
- Model abstraction layer  
- Output processing layer  
- Error handling & scalability  

This module builds that **engineering mindset**.

---

## 🔮 Possible Improvements

- Add FastAPI wrapper  
- Add logging & monitoring  
- Add retry mechanism  
- Add structured JSON output mode  
- Add unit tests  
- Convert to microservice architecture  

---

## 👨‍💻 Author

Chethan Malli  
AI & ML Enthusiast  
Building production-ready AI systems 🚀  

---

⭐ If this module helped you understand LLM architecture, give the repo a star!
