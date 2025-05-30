from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello, world! I am your Telegram bot.')

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('This bot  created by Erkin Çak.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/about - About info\n"
        "/help - This help message\n"
        "/fact - Get an interesting fact\n"
    )
    await update.message.reply_text(help_text)

async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    fact_text = "Your brain is constantly eating itself."
    await update.message.reply_text(fact_text)

def main() -> None:
    
    application = ApplicationBuilder().token('7977188537:AAFDtd_5XV8T8rQIQeRai264QuLaLNXw').build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("fact", fact))
    application.run_polling()
if __name__ == '__main__':
    main()
