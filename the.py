import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = "你的Bot Token"
randdom = ''.join([str(random.randint(0, 9)) for _ in range(30)])
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("StarT")
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    # 精准匹配
    if text == "12":
        await update.message.reply_text("1+2")
    if text == "확인":
        await update.message.reply_text("USDT를 사용하여 결제해 주세요. 결제가 완료되면, 주문 번호를 다시 입력하면 주소를 보낼 수 있습니다 -------귀하의 주문 번호는:ZC420FY" + randdom + "'--------'주문 상태가 성공하면, 다시 한 번 주문 번호를 '미친 박사'에게 보내거나, 주문 링크를 제공한 보증인 또는 보증금을 낸 대리인에게 전달하십시오.")
    if "확인" in text:
        await update.message.reply_text("결제 수단을 선택해 주세요. 'TRC20'/'ETH'/'BTC'에 회신하시면 통일된 결제 주소를 받을 수 있습니다.")
    elif text == "TRC20":
        await update.message.reply_text("TLRsCgKxAzho4FNv659n6EjQVUjhW71KAp")
    elif text == "trc20":
        await update.message.reply_text("USDT-TRC20/TRX의 출금 주소는:\nTLRsCgKxAzho4FNv659n6EjQVUjhW71KAp")
    elif text == "btc":
        await update.message.reply_text("죄송합니다, 사장님, 현재는 지원되지 않습니다. 다른 결제 수단을 이용해 주시기 바랍니다.")
    elif text == "BTC":
        await update.message.reply_text("⚙️USDT-TRC20 또는 TRX 결제를 선택하십시오")
    elif text == "eth":
        await update.message.reply_text("⚙️죄송합니다, 사장님, 현재는 지원되지 않습니다. 다른 결제 수단을 이용해 주시기 바랍니다.")
    elif text == "ETH":
        await update.message.reply_text("USDT-TRC20 또는 TRX 결제를 선택하십시오")
    elif text == "21":
        await update.message.reply_text("2+1")
    elif text == "ppp":
        await update.message.reply_text("X1X4KING")
    elif text == "5":
        await update.message.reply_text(
            "안녕하세요, 금액 203 USDT 입니다. 결제 확인하시겠습니까? '확인'을 입력하면 주문 번호를 제공하기 시작하며, 결제 후 주문 번호를 보관한 뒤 로봇에게 다시 전송하세요.")
    elif text == "10":
        await update.message.reply_text(
            "안녕하세요, 금액 359 USDT 입니다. 결제 확인하시겠습니까? '확인'을 입력하면 주문 번호를 제공하기 시작하며, 결제 후 주문 번호를 보관한 뒤 로봇에게 다시 전송하세요.")
    elif text == "20":
        await update.message.reply_text(
            "안녕하세요, 금액 624 USDT 입니다. 결제 확인하시겠습니까? '확인'을 입력하면 주문 번호를 제공하기 시작하며, 결제 후 주문 번호를 보관한 뒤 로봇에게 다시 전송하세요.")
    elif text == "50":
        await update.message.reply_text("박사나 대리인에게 연락하여 미리 준비하세요.")
    elif text == "재고조회":
        await update.message.reply_text("서울/강남/홍대/명동/동대문/광화문/인천/부산/해운대\n'재고 충분' 바로 주문 가능!\n주문이 진행 중이면, 서울과 인천 지역을 제외한 대부분의 지역에서는 24시간 내에 자동으로 GPS와 사진 정보가 전송됩니다!")
    elif text == "구매":
        await update.message.reply_text(
            "구매할 수량을 입력하세요, 예를 들어 👽'5'/'10'/'20'/'50'👽. [구매하실 수량을 회신해 주십시오.]\n100 이상일 경우 담당자에게 연락하시거나 직접 Dr.Mad를 찾으십시오.")
    elif len(text) == 37:
        await update.message.reply_text("!해당 주문은 아직 결제가 확인되지 않았습니다!\n해당 주문 번호가 결제되지 않은 것으로 감지되었습니다. 결제 후 시스템이 자동으로 GPS 좌표와 사진을 전송합니다!!")
    else:
        await update.message.reply_text(
            "안녕하세요, 이것은 자가 서비스 로봇 v1.11🤖 └|°ε°|┐ 🤖입니다. \n주문 후 자동으로 배송됩니다 --🛠️ ┗┫￣皿￣┣┛ 🛠️ '구매'를 입력해주세요. \n지역을 조회하려면 --📡 [|/ﾟ∇ﾟ|丿] 📡 '재고조회'를 입력하세요. \n문제가 있으면 박사님이나 대리인에게 문의하세요.")
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
if __name__ == "__main__":
    main()
