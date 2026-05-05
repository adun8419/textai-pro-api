// TextAI Pro — Sentiment Analysis
// Get your free API key: https://rapidapi.com/adunaev8419/api/textai-pro

const API_KEY = 'YOUR_RAPIDAPI_KEY';

async function analyzeText(text) {
  const response = await fetch('https://textai-pro.p.rapidapi.com/analyze', {
    method: 'POST',
    headers: {
      'X-RapidAPI-Key': API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ text })
  });
  return response.json();
}

async function summarizeText(text) {
  const response = await fetch('https://textai-pro.p.rapidapi.com/summarize', {
    method: 'POST',
    headers: {
      'X-RapidAPI-Key': API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ text })
  });
  return response.json();
}

// Example usage
analyzeText('This product is absolutely amazing!').then(console.log);

