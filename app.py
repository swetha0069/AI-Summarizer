from flask import Flask, render_template, request
from engine import get_ai_summary
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        text = request.form.get('data', '')
        if not text:
            return render_template('index.html', error="Please enter some text.")
            
        # This calls your AI model from engine.py
        result = get_ai_summary(text)
        return render_template('index.html', result=result)

if __name__ == '__main__':
    # Render assigns a dynamic port, so we must read it from the environment
    # If it's not found (like on your laptop), it defaults to 10000
    port = int(os.environ.get("PORT", 10000))
    
    # host='0.0.0.0' is required for cloud hosting
    app.run(host='0.0.0.0', port=port)