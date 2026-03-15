from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import textstat

# 1. Use a specific model name that fits in Render's Free Tier memory
model_name = "sshleifer/distilbart-cnn-6-6"

# 2. Explicitly load the tokenizer and model to avoid "Unknown task" errors
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# 3. Create the summarization pipeline using the loaded model
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

def get_ai_summary(text):
    if not text.strip():
        return {"summary": "Please enter some text to summarize.", "readability": "0.00"}
    
    try:
        # Calculate readability using textstat
        readability_score = textstat.flesch_reading_ease(text)
        
        # Generate the summary
        # Setting truncation=True handles long inputs without crashing
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False, truncation=True)
        summary_text = summary[0]['summary_text']
        
        return {
            "summary": summary_text,
            "readability": f"{readability_score:.2f}"
        }
    except Exception as e:
        return {"summary": f"Error: {str(e)}", "readability": "Error"}