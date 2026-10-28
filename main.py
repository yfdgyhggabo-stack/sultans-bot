import telebot

TOKEN = "9065541736:AAFdTlRsJCWJvSm9eXZehNDCIL8qWT5iY2w"
WEB_APP_URL = "https://leafy-maamoul-1cd1e7.netlify.app"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton("⚙️ افتح إعدادات قلعة الفاتحون", web_app=telebot.types.WebAppInfo(url=WEB_APP_URL))
    markup.add(btn)
    bot.reply_to(message, "أهلاً بك يا شرف في بوت إدارة قلعة الفاتحون 🏰\nاضغط على الزر بالأسفل لفتح لوحة الإعدادات:", reply_markup=markup)

print("Bot is running...")
bot.infinity_polling()
