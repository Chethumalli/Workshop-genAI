# 🚀 Workshop-genAI  

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi)
![LLM](https://img.shields.io/badge/LLM-Groq%20%7C%20OpenAI-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## 📌 About The Project  

**Workshop-genAI** is a hands-on implementation repository built during a Generative AI Workshop.  

This project demonstrates how to integrate **Large Language Models (LLMs)** into real-world backend systems using **FastAPI** and modern AI APIs like **Groq** and **OpenAI**.

> 🎯 Goal: Learn how modern AI applications like ChatGPT are built — and build one yourself.

---

## 🧠 What This Project Covers  

- 🤖 Understanding Large Language Models (LLMs)  
- ⚡ FastAPI backend development  
- 🔥 Groq / OpenAI API integration  
- 🧠 Prompt engineering basics  
- 🛠 Building AI-powered applications  

---

## 🛠 Tech Stack  

| Technology       | Purpose                      |
|------------------|-----------------------------|
| 🐍 Python        | Core programming             |
| ⚡ FastAPI       | Backend API framework        |
| 🧠 Groq / OpenAI | LLM integration              |
| 🔗 REST APIs     | Communication layer          |
| 🖥 VS Code        | Development environment      |

---

## 📂 Project Structure  

```bash
Workshop-genAI/
│
├── app.py              # Main FastAPI application
├── requirements.txt    # Project dependencies
├── README.md           # Documentation
└── .env                # API keys (not included in repo)
```

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/Chethumalli/Workshop-genAI.git
cd Workshop-genAI
```

### 2️⃣ Create Virtual Environment  

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies  

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key  

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

(or use `OPENAI_API_KEY` if using OpenAI)

### 5️⃣ Run the Application  

```bash
uvicorn app:app --reload
```

Now open:

```
http://127.0.0.1:8000
```

Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 🔄 How It Works  

1. User sends a prompt  
2. FastAPI backend receives the request  
3. Backend calls Groq/OpenAI API  
4. LLM generates response  
5. API returns structured JSON response  

This is the same architecture used in modern AI applications.

---

## 🔮 Future Enhancements  

- 🌐 Cloud deployment (AWS / Render / Railway)  
- 💬 Frontend UI integration  
- 🔐 Authentication system  
- 📊 Logging & analytics  
- 🐳 Docker support  
- 🧠 Fine-tuned models  

---

## 🤝 Contributing  

Contributions are welcome!

1. Fork the repository  
2. Create a feature branch  
3. Commit your changes  
4. Push to GitHub  
5. Open a Pull Request  

---

## 👨‍💻 Author  

**Chethan Malli**  
AI & ML Enthusiast  
Building AI-powered systems  

GitHub: https://github.com/Chethumalli  

---

⭐ If you found this project useful, consider giving it a star!
