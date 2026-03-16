📝 AI Writer with Text Summarization
📖 Overview
This project is a fully functional web application developed as part of my Data Science Internship (March 2026). The objective was to build an end-to-end NLP tool that can take large articles and generate concise, human-like summaries.

The application uses a Transformer-based Generative AI model connected to a Flask web server, allowing users to paste text into a browser and receive instant summaries along with key text analytics.

✨ Features
AI-Powered Summarization: Utilizes the GPT-2 model from Hugging Face for real-time text processing.

Web Interface: A clean, responsive UI built with Flask and HTML5/CSS3.

Text Analytics & Metrics: Automatically calculates and displays:

Original Word Count: Total words in the source text.

Summary Word Count: Final length after AI processing.

Readability Score: A "High/Medium/Low" assessment of the output.

Local Development: Optimized to run efficiently on a local machine at http://127.0.0.1:5000.

🛠️ Technologies Used
Backend: Python 3.13

Web Framework: Flask

AI/ML Library: Hugging Face transformers

Deep Learning Framework: PyTorch

Frontend: HTML5, CSS3, Jinja2 Templates

🚀 Setup and Run Instructions
1. Prepare the Environment
Ensure you have Python installed, then install the required libraries via your terminal:

Bash
pip install flask transformers torch
2. Project Structure
Ensure your files are organized as follows:

Plaintext
AI_Summarizer/
├── app.py              # Flask Backend & AI Pipeline
├── templates/          
│   └── index.html      # Frontend Interface
└── Screenshot.png      # Project Preview Image
3. Run the Application
Start the server by running:

Bash
python app.py
Note: The first run will take 1-2 minutes to download the AI model weights.

4. View in Browser
Once the terminal shows --- ✅ AI Engine Loaded & Ready! ---, navigate to:
http://127.0.0.1:5000

👣 Step-by-Step Implementation
Environment Setup: Configured a local development environment in VS Code using Python 3.13.

Model Selection: Tested various Hugging Face pipelines, ultimately selecting a text-generation model for its stability in local Windows environments.

Backend Development: Built app.py using Flask to handle POST requests and manage the global AI engine state.

Frontend Design: Created a professional index.html with CSS styling to display the results in a clean "Result Box" format.

Analytics Integration: Wrote Python logic to split text and count words to provide users with data-driven feedback on the summary quality.

⚠️ Errors Faced & Solutions
1. Unknown Task Error (KeyError)
Error: Terminal showed KeyError: "Unknown task summarization".

Reason: The local library version had issues recognizing the specific summarization pipeline for certain models.

Solution: Switched the task to text-generation with a specific prompt prefix (Text: ... Summary: ), which is more robust and widely supported.

2. NameError: 'summarizer' is not defined
Error: The app crashed when clicking the "Summarize" button immediately after startup.

Reason: The AI model was still downloading in the background when the user requested a summary.

Solution: Implemented a Global Loading Check. Added a status message: "AI Engine is still loading. Please refresh in 30 seconds," to prevent the app from crashing during initialization.

✅ Final Output
The final application successfully takes complex articles (like tech news or history paragraphs) and reduces them to their core message. It effectively bridges the gap between deep learning models and a user-friendly interface.

Author: [Swetha]
