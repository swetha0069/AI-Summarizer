from transformers import pipeline
import textstat

# 1. Use 'text-generation' because it is in your 'available tasks' list
print("Loading AI Model (BART)... This may take a minute.")
summarizer = pipeline("text-generation", model="facebook/bart-large-cnn")

def get_ai_summary(text):
    original_word_count = len(text.split())
    readability_score = textstat.flesch_reading_ease(text)
    
    # CHUNKING: Split text into blocks of 500 words
    words = text.split()
    chunks = [" ".join(words[i : i + 500]) for i in range(0, len(words), 500)]
    
    summaries = []
    for chunk in chunks:
        # Note: Using max_new_tokens for the 'text-generation' task
        result = summarizer(chunk, max_new_tokens=150, do_sample=False)
        summaries.append(result[0]['generated_text'])
    
    final_summary = " ".join(summaries)
    
    return {
        "summary": final_summary,
        "original_count": original_word_count,
        "new_count": len(final_summary.split()),
        "readability": readability_score
    }

if __name__ == "__main__":
    sample_text = "AI is transforming the world. Summarization helps condense information."
    output = get_ai_summary(sample_text)
    print(f"\nSummary: {output['summary']}")