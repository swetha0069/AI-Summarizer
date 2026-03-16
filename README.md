# AI-Summarizer
# 📝 AI Text Summarizer (Local Version)

This is an AI-powered web application built for my Data Science internship project. It takes long articles and condenses them into concise summaries using the **GPT-2** Transformer model.

## 📸 Project Preview
![App Screenshot](./Screenshot_2026-03-16_135658.png)
*Running locally on http://127.0.0.1:5000*

---

## 🚀 Key Features
* **Automated Summarization:** Uses Natural Language Processing (NLP) to extract key points.
* **Real-time Statistics:** Calculates word count reduction (e.g., 207 words down to 220).
* **Readability Assessment:** Provides a quick check on the output quality.
* **Flask Backend:** A robust Python web server managing the AI engine.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Web Framework:** Flask
* **AI Engine:** Hugging Face Transformers (GPT-2)
* **Frontend:** HTML5 & CSS3 (Jinja2 Templates)

## 📂 Project Structure
```text
AI_Summarizer/
├── app.py              # Main Flask application & AI Logic
├── templates/          
│   └── index.html      # Frontend User Interface
└── README.md           # Project Documentation
