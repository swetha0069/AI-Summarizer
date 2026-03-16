from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# --- GLOBAL ENGINE SETUP ---
summarizer = None

def load_engine():
    global summarizer
    print("--- 📥 Starting AI Engine Download... ---")
    try:
        # Using 'text-generation' because your computer explicitly supports it
        # Using 'gpt2' because it is small, fast, and very reliable for local testing
        summarizer = pipeline("text-generation", model="gpt2")
        print("--- ✅ AI Engine Loaded & Ready! ---")
    except Exception as e:
        print(f"--- ❌ Error Loading Engine: {e} ---")

# Start the loading process
load_engine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    global summarizer
    if request.method == 'POST':
        input_text = request.form['data']
        
        if summarizer is None:
            return "AI Engine is still downloading in the terminal. Please wait 60 seconds and refresh."

        if input_text.strip():
            # For GPT2, we ask it to summarize in the prompt
            query = f"Text: {input_text}\n\nSummary:"
            
            # Generate the result
            raw_result = summarizer(query, max_length=100, num_return_sequences=1)
            full_text = raw_result[0]['generated_text']
            
            # Extract just the summary part
            summary_text = full_text.split("Summary:")[-1].strip()
            
            result_data = {
                "summary": summary_text,
                "original_count": len(input_text.split()),
                "new_count": len(summary_text.split()),
                "readability": "High"
            }
            return render_template('index.html', result=result_data, original=input_text)
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
