# 🎭 AI Concept Explainer

## 📌 Overview

**AI Concept Explainer** is a prompt-based system that explains complex topics in different audience modes.

Instead of changing the model, we change the **prompt style** — demonstrating how prompt engineering can control tone, personality, and explanation complexity.

The system can explain concepts in creative modes such as:

- 🎩 Shakespeare
- 🏴‍☠️ Pirate
- 🤠 Bandit

This project highlights the power of prompt design in shaping AI responses.

---

## 🎯 Objective

Build a flexible explanation system where:

```
User Topic + Selected Style → Prompt Engineering → LLM → Styled Explanation
```

The goal is to demonstrate how system instructions and user instructions influence AI behavior.

---

## 🧠 How It Works

### 1️⃣ System Prompt
Defines:
- AI personality
- Tone and communication style
- Formatting rules
- Explanation depth

Example:
```
You are an expert teacher who explains concepts clearly.
Adapt your tone based on the selected style.
```

---

### 2️⃣ User Prompt
Contains:
- The topic to explain
- The chosen audience mode (Shakespeare / Pirate / Bandit)

Example:
```
Explain "Artificial Intelligence" in Pirate style.
```

---

### 3️⃣ Model Response
The LLM:
- Reads system instructions
- Applies selected style
- Generates explanation accordingly

---

## 🎨 Example Output Modes

### 🎩 Shakespeare Mode
> “Lo! Artificial Intelligence be the craft wherein machines dost mimic the wit of man…”

---

### 🏴‍☠️ Pirate Mode
> “Arrr! AI be the brain o’ the machine, makin’ it think like a clever sea dog…”

---

### 🤠 Bandit Mode
> “Listen here, partner… AI’s like teachin’ a machine to outsmart the wild west…”

---

## 🛠 Tech Stack

- 🐍 Python
- ⚡ LiteLLM (or OpenAI/Groq API)
- 🔥 Prompt Engineering
- 🔐 Environment variable management (.env)

---

## ⚙ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Add API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_key_here
MODEL_NAME=groq/llama-3.1-8b-instant
```

⚠️ Do NOT upload `.env` to GitHub.

---

### 4️⃣ Run the Project

```bash
python main.py
```

---

## 🎓 Key Learning

✔ Prompt engineering controls tone  
✔ System prompt defines AI personality  
✔ User prompt modifies explanation style  
✔ LLM behavior can be shaped without retraining  
✔ Same model, different outputs  

---

## 🚀 Why This Matters

Modern AI applications:

- Customize tone for different users  
- Adapt to children vs professionals  
- Simulate characters  
- Generate brand-specific communication  

This project demonstrates how **prompt engineering alone can reshape AI behavior**.

---

## 🔮 Possible Improvements

- Add more character modes  
- Add difficulty levels (Beginner / Expert)  
- Convert to web interface  
- Add structured JSON output mode  
- Add temperature control  

---

## 👨‍💻 Author

Chethan Malli  
AI & ML Enthusiast  
Exploring prompt-driven AI systems 🚀  

---

⭐ If this project helped you understand prompt engineering, give it a star!
