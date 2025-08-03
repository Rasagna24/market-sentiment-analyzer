from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return "📈 Bullish"
    elif score <= -0.05:
        return "📉 Bearish"
    else:
        return "📊 Neutral"

print("💬 Welcome to Market Sentiment Analyzer!")
print("Type a financial headline or news and get sentiment. Type 'exit' to quit.\n")

while True:
    user_input = input("📰 Headline: ")
    if user_input.lower() == "exit":
        print("Exiting...")
        break
    print(f"➡ Sentiment: {analyze_sentiment(user_input)}\n")
