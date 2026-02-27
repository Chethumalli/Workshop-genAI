# 🧩 Module 2 – Structured Answer Generator

## 📌 Overview

This module builds a **Structured Response Generator** using:

- ⚡ LiteLLM
- 🔥 Groq API
- 🧠 Prompt Engineering
- 🎯 Deterministic prompting
- 📦 Controlled output formatting

The goal of this module is to generate **clean, structured, production-style AI responses** instead of raw unformatted text.

This simulates how real-world AI systems generate predictable, consistent outputs.

---

## 🚀 What This Module Demonstrates

✔ Separation of system and user prompts  
✔ Controlled output format (headings, bullets, JSON-style structure)  
✔ Deterministic prompting for consistent responses  
✔ Production-ready prompt design  
✔ Secure API key management using `.env`  

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Core programming |
| ⚡ LiteLLM | Model abstraction layer |
| 🔥 Groq API | LLM provider |
| 📦 python-dotenv | Environment variable management |

---

## 📂 File Structure

```
Module-2/
│
├── structured_generator.py   # Main structured response generator
├── requirements.txt          # Project dependencies
├── .env                      # API keys (not pushed to GitHub)
└── README.md                 # Documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

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

⚠️ Never push your `.env` file to GitHub.

---

###  Run the Generator

```bash
python app.py
```

---

## 🧠 How It Works

1. A user question is passed to the script.
2. A **system prompt** defines strict formatting rules.
3. The model generates output in a structured format.
4. The script prints a clean, controlled response.

---

## 🧾 Example Output Format

Instead of random paragraphs, the output follows a structured format like:

```
Title: Topic Name

Definition:
Short explanation

Key Points:
- Point 1
- Point 2
- Point 3

Conclusion:
Short summary
```

This ensures:
- Predictable results  
- Clean formatting  
- Production-ready AI output  

---

## 🎯 Why Structured Prompting Matters

In real AI systems:

- Unstructured outputs are hard to parse
- Structured outputs are easier to store in databases
- Deterministic prompting improves reliability
- Consistent formatting improves user experience

This module demonstrates how production AI systems control LLM behavior.

---

## 🔮 Possible Improvements

- Add JSON response mode  
- Convert to FastAPI endpoint  
- Add logging  
- Add temperature control  
- Deploy as microservice  
- Add retry & error handling  

---

## 👨‍💻 Author

Chethan Malli  
AI & ML Enthusiast  
Building production-ready AI systems 🚀

---

⭐ If this module helped you understand structured prompting, give the repo a star!
