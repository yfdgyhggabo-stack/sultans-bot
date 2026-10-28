import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "9065541736:AAFdTlRsJCWJvSm9eXZehNDCIL8qWT5iY2w"
WEB_APP_URL = "https://bespoke-manatee-225de6.netlify.app"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚙️ افتح إعدادات قلعة الفاتحون", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "أهلاً بك يا شرف في بوت إدارة قلعة الفاتحون 🏰\n"
        "اضغط على الزر بالأسفل لفتح لوحة الإعدادات والتحكم بالمهام:",
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
