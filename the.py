print("Version-3.9)
print("hello words")
python
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = "你的Bot Token"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("")
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    # 精准匹配
    if text == "123":
        await update.message.reply_text("1+2")
        if text == "3":
            await update.message.reply_text("right")
    elif text == "121":
        await update.message.reply_text("2+1")
        if "?" in text:
            await update.message.reply_text("what")
    elif text == "ppp":
        await update.message.reply_text("X1X4KING")
    elif text == "결제":
        await update.message.reply_text("NoLink pls connect the Dr.Mad")
    elif text == "지역":
        await update.message.reply_text("새 사용자로 감지되어 접근 권한이 없습니다. 미친 박사에게 연락해 주세요.")
    elif text == "코어":
        await update.message.reply_text("새 사용자로 감지되어 접근 권한이 없습니다. 미친 박사에게 연락해 주세요.")
    elif text == "보고":
        await update.message.reply_text("NoLink pls connect the Dr.Mad")
    else:
        await update.message.reply_text("비행 콘솔 테스트 버전 v1.0\n입력 '결제' → X 링크가 전송됩니다\n입력 '지역' → 현재 재고 수량을 조회합니다\n입력 '코어' → 문의 내용을 기록하고 피드백합니다\n입력 '보고' → 스크린샷 또는 문자를 남기면 박사님께 전송됩니다")
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
if __name__ == "__main__":
    main()
