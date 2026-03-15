import requests
import os

stock_api_key = os.getenv("OWM_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
bot_token = os.getenv("STOCK_BOT")
chat_id=os.getenv("CHAT_STOCK")

STOCK_SYMBOL = "TSLA"
COMPANY_NAME = "Tesla Inc"
telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"


stock_endpoint = "https://www.alphavantage.co/query"
stock_params = {
    "function": "GLOBAL_QUOTE",
    "symbol": STOCK_SYMBOL,
    "apikey": stock_api_key
}

stock_response = requests.get(stock_endpoint, params=stock_params)
stock_data = stock_response.json()

stock_percent_change = stock_data["Global Quote"]["10. change percent"]
percent_value = float(stock_percent_change.strip("%"))


if abs(percent_value) >= 5:
    direction = "🔺" if percent_value > 0 else "🔻"

    
    news_endpoint = "https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "apiKey": news_api_key
    }

    news_response = requests.get(news_endpoint, params=news_params)
    news_data = news_response.json()
    articles = news_data.get("articles", [])

    # Build Telegram message
    message = f"<b>{STOCK_SYMBOL} {direction}{percent_value:.2f}%</b>\n\nTop 3 News:\n"
    for i, article in enumerate(articles[:3], start=1):
        message += f"{i}. {article['title']}\n{article['url']}\n\n"

    # Send Telegram alert
    requests.post(telegram_url, data={"chat_id": chat_id, "text": message, "parse_mode": "HTML"})
    print("Telegram alert sent!")

else:
    print(f"{STOCK_SYMBOL} change is {percent_value:.2f}%, no news alert.")


