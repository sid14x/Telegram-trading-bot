import requests
from bs4 import BeautifulSoup

def check_moving_average_crossover(data, short_window=5, long_window=20):
    if len(data) < long_window + 1:
        return None
    short_prev = sum(data[-short_window-1:-1]) / short_window
    long_prev  = sum(data[-long_window-1:-1]) / long_window
    short_now  = sum(data[-short_window:]) / short_window
    long_now   = sum(data[-long_window:]) / long_window
    if short_prev < long_prev and short_now > long_now:
        return "🔼 Bullish Moving Average Crossover!"
    if short_prev > long_prev and short_now < long_now:
        return "🔽 Bearish Moving Average Crossover!"
    return None

def check_moneycontrol_news(keywords=["nifty","crude","sensex","oil"]):
    url = "https://www.moneycontrol.com/news/business/"
    soup = BeautifulSoup(requests.get(url, headers={"User-Agent":"Mozilla/5.0"}).text, "html.parser")
    alerts = []
    for a in soup.select("li.clearfix a")[:10]:
        text = a.get_text(strip=True).lower()
        link = a['href']
        for kw in keywords:
            if kw in text:
                alerts.append(f"📰 News: {text}\n🔗 {link}")
                break
    return alerts
