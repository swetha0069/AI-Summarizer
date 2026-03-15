from transformers import pipeline
import textstat

# Using a distilled model to fit within Render's 512MB RAM limit
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6")

def get_ai_summary(text):
    if not text.strip():
        return "Please enter some text to summarize."
    
    # Calculate readability before summary
    readability_score = textstat.flesch_reading_ease(text)
    
    # Generate summary
    # max_length and min_length help control memory usage
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    summary_text = summary[0]['summary_text']
    
    return {
        "summary": summary_text,
        "readability": f"{readability_score:.2f}"
    }