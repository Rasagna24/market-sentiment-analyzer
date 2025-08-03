# Market Sentiment Analyzer
A lightweight Python-based command-line tool to analyze the sentiment of financial news headlines using natural language processing (NLP).

# What It Does
This tool takes in real-time user input (headlines, tweets, or financial news snippets) and returns whether the sentiment is:
📈 Bullish (positive)
📉 Bearish (negative)
🟰 Neutral (neutral)

# Tech Stack & Tools
Python 3
vaderSentiment – rule-based sentiment analysis tool optimized for social media and short texts
Command-line interface (CLI) with emoji-enhanced responses

# Why It Matters
In financial markets, sentiment plays a massive role in asset movement.
This tool helps simulate how one might quantify news sentiment — a skill relevant to roles in:
Market research
Trading and investing
Fintech and algorithmic trading
Quantitative analytics

# How to Run
1. Install the required package:
pip install vaderSentiment
2. Clone the repository and run the script:
python sentiment_analyzer.py
3. Start entering financial headlines. Type exit to quit.

# Example Usage
💬 Headline: Inflation at all-time high  
→ Sentiment: 📉 Bearish
💬 Headline: Tech stocks rally after strong earnings  
→ Sentiment: 📈 Bullish
💬 Headline: Markets remain flat amid global uncertainty  
→ Sentiment: 🟰 Neutral

# Future Improvements
Add batch sentiment analysis from CSVs
Integrate with financial APIs (Yahoo Finance, News APIs)
Deploy as a web app using Flask or Streamlit
