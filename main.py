import telebot

TOKEN = "9065541736:AAFdTlRsJCWJvSm9eXZehNDCIL8qWT5iY2w"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا شرف في بوت إدارة قلعة الفاتحون 🏰")

print("Bot is running...")
bot.infinity_polling()
