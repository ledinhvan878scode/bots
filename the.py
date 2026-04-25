print("Version-3.9)
print("hello words")
python
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = "你的Bot Token"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("机器人已启动，输入点什么试试")
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    # 精准匹配
    if text == "12":
        await update.message.reply_text("1+2")
    elif text == "21":
        await update.message.reply_text("2+1")
    elif text == "ppp":
        await update.message.reply_text("X1X4KING")
    else:
        await update.message.reply_text("请输入123123123")
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
if __name__ == "__main__":
    main()
