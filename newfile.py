import telebot
import os

TOKEN = os.getenv("TOKEN")   # faqat nom!
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom! 🤖\n"
        "24/7 ishlaydigan kalkulyator botman.\n\n"
        "Misol yubor:\n"
        "2+2\n"
        "10-3\n"
        "4*5\n"
        "8/2"
    )

@bot.message_handler(func=lambda message: True)
def calc(message):
    try:
        text = message.text.replace(" ", "")
        natija = eval(text)
        bot.send_message(message.chat.id, f"Natija: {natija}")
    except:
        bot.send_message(message.chat.id, "Xato ❌\nMasalan: 2