# TextAI Pro API

Sentiment analysis, keyword extraction and text summarization API.

**RapidAPI:** https://rapidapi.com/adunaev8419/api/textai-pro

## Quick Start

```python
import requests

url = "https://textai-pro.p.rapidapi.com/analyze"
headers = {"X-RapidAPI-Key": "YOUR_KEY", "Content-Type": "application/json"}
r = requests.post(url, json={"text": "This product is absolutely amazing!"}, headers=headers)
print(r.json())
# {"sentiment": "positive", "confidence": 0.92, "keywords": ["product", "amazing"]}
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /analyze | POST | Sentiment + keywords |
| /summarize | POST | Text summarization |

## Pricing

| Plan | Price | Requests/hr |
|------|-------|-------------|
| BASIC | Free | 50 |
| PRO | $9.99/mo | 1,000 |
| ULTRA | $29.99/mo | 10,000 |

See `examples/` for Python, JavaScript, cURL samples.

