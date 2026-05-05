import requests

# TextAI Pro — Sentiment Analysis
# Get your free API key: https://rapidapi.com/adunaev8419/api/textai-pro

API_KEY = "YOUR_RAPIDAPI_KEY"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "Content-Type": "application/json"
}

# Analyze sentiment
def analyze_text(text):
    url = "https://textai-pro.p.rapidapi.com/analyze"
    r = requests.post(url, json={"text": text}, headers=headers)
    return r.json()

# Summarize text
def summarize_text(text):
    url = "https://textai-pro.p.rapidapi.com/summarize"
    r = requests.post(url, json={"text": text}, headers=headers)
    return r.json()

if __name__ == "__main__":
    result = analyze_text("This product is absolutely amazing, I love it!")
    print("Sentiment:", result["sentiment"])
    print("Confidence:", result["confidence"])
    print("Keywords:", result["keywords"])

