import os
import telebot
from alert_system import check_moving_average_crossover, check_moneycontrol_news
from data_source import get_latest_prices

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['alerts'])
def send_alerts(message):
    prices = get_latest_prices("NIFTY")
    ma_signal = check_moving_average_crossover(prices)
    if ma_signal:
        bot.send_message(message.chat.id, ma_signal)
    news_alerts = check_moneycontrol_news()
    for alert in news_alerts:
        bot.send_message(message.chat.id, alert)

if __name__ == '__main__':
    bot.infinity_polling()
    print("Bot is running...")
