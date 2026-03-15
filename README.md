<h1 align="center">Telegram Stock & News Alert Bot 📈📰</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Requests-2CA5E0?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Alpha_Vantage-005C00?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/NewsAPI-FF4B4B?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Telegram_API-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
</div>

---

## 📌 Overview
The Telegram Stock & News Alert Bot is an automated financial monitoring script. It tracks daily stock price fluctuations for a specified company (e.g., Tesla). If a significant market swing occurs (a price jump or drop of 5% or more), the bot automatically aggregates the top breaking news headlines for that company and delivers a formatted alert directly to your phone via Telegram.

---

## ⚙️ Core Features
* **Financial Data Integration:** Utilizes the **Alpha Vantage API** to fetch real-time global stock quotes and calculate daily percentage changes.
* **Automated News Aggregation:** Leverages **NewsAPI** to instantly fetch the top 3 most relevant and recent news articles when a stock anomaly is detected.
* **Instant Telegram Notifications:** Integrates with the **Telegram Bot API** to push formatted HTML messages (including trend emojis 🔺/🔻 and article links) directly to a personal chat or channel.
* **Secure Environment:** Uses environment variables to securely store sensitive API keys and Bot tokens.

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/baldyachty/stock-news-bot.git](https://github.com/baldyachty/stock-news-bot.git)
cd stock-news-bot
```

### 2. Set Up Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory and add your API keys:
```env
# API Keys
OWM_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_newsapi_key

# Telegram Setup
STOCK_BOT=your_telegram_bot_token
CHAT_STOCK=your_telegram_chat_id
```

### 4. Run the Bot
```bash
python main.py
```

---

## 💡 Automation Recommendation
This script is designed to run automatically! For best results, set this up on a cron job (Linux/macOS) or Windows Task Scheduler to run daily at the market close (e.g., 4:30 PM EST). 

---

**Maintained by [baldyachty](https://github.com/baldyachty)**
