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
    if "확인" in text:
        await update.message.reply_text("진위 여부에 주의하세요 USDT-TRC20 주소:---주문은 박사님께 문의하십시오--- 이 안에 있는 이 부분만 복사하여 'TRC20'을 입력하면 주소를 별도로 얻을 수 있습니다")
    elif text == "21":
        await update.message.reply_text("2+1")
    elif text == "ppp":
        await update.message.reply_text("X1X4KING")
    elif text == "5":
        await update.message.reply_text(
            "안녕하세요, 금액 197USDT 입니다. 결제 확인하시겠습니까? '확인'을 입력하면 주문 번호를 제공하기 시작하며, 결제 후 주문 번호를 보관한 뒤 로봇에게 다시 전송하세요.")
    elif text == "10":
        await update.message.reply_text(
            "안녕하세요, 금액 358USDT 입니다. 결제 확인하시겠습니까? '확인'을 입력하면 주문 번호를 제공하기 시작하며, 결제 후 주문 번호를 보관한 뒤 로봇에게 다시 전송하세요.")
    elif text == "20":
        await update.message.reply_text(
            "안녕하세요, 금액 623USDT 입니다. 결제 확인하시겠습니까? '확인'을 입력하면 주문 번호를 제공하기 시작하며, 결제 후 주문 번호를 보관한 뒤 로봇에게 다시 전송하세요.")
    elif text == "50":
        await update.message.reply_text("박사나 대리인에게 연락하여 미리 준비하세요.")
    elif text == "付款":
        await update.message.reply_text("请注意真伪:TRC20地址:---AlaksdjMA---只复制里面这一段输入'TRC20'可单独获取地址")
    elif text == "재고조회":
        await update.message.reply_text("서울/강남/홍대/명동/동대문/광화문/인천/부산/해운대\n'재고 충분' 바로 주문 가능!")
    elif text == "首尔":
        await update.message.reply_text("首尔现在还剩'库存充足'可直接下单!")
    elif text == "大阪":
        await update.message.reply_text("大版现在没有库存!")
    elif text == "吉隆坡":
        await update.message.reply_text("现在没有库存")
    elif text == "TRC20":
        await update.message.reply_text("TLRsCgKxAzho4FNv659n6EjQVUjhW71KAp")
    elif text == "구매":
        await update.message.reply_text(
            "구매할 수량을 입력하세요, 예를 들어 '5'/'10'/'20'/'50'. 구매 수량이 20개를 초과하면 사전에 예약이 필요하니, 예약은 직접 박사에게 연락하세요.")
    elif text == "订单查询":
        await update.message.reply_text("你好尊敬的客户-----!!!请输入你的订单号!!!")
    elif len(text) == 37:
        await update.message.reply_text("해당 주문 번호가 결제되지 않은 것으로 감지되었습니다. 결제 후 시스템이 자동으로 GPS 좌표와 사진을 전송합니다!!")
    elif text == "확인":
        await update.message.reply_text('USDT를 사용하여 결제해 주세요. 결제가 완료되면, 주문 번호를 다시 입력하면 주소를 보낼 수 있습니다 -------귀하의 주문 번호는:ZC420FY' + randdom + '--------')
    elif text == "确认":
        await update.message.reply_text("X1X4KING")
    else:
        await update.message.reply_text(
            "안녕하세요, 이것은 자가 서비스 로봇 v1.1입니다. \n주문 후 자동으로 배송됩니다 -- '구매'를 입력해주세요. \n지역을 조회하려면 -- '재고조회'를 입력하세요. \n문제가 있으면 박사님이나 대리인에게 문의하세요.")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()


if __name__ == "__main__":
    main()
