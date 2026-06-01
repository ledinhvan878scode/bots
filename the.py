from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext
import datetime
import os

ADMIN_CHAT_ID = 123456789  # 管理员 chat_id
HISTORY_FILE = "/chat_history.txt"

blocked_users = set()


def write_history(user_id, text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"id:{user_id} > ({timestamp}) {text}\n"

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(line)

    # 自动推送到 GitHub（可选）
    # os.system("cd /root/telegram-chat-history && git add . && git commit -m 'update' && git push")


def handle_user_message(update: Update, context: CallbackContext):
    user = update.effective_user
    msg = update.effective_message

    if user.id in blocked_users:
        return

    # 写入 TXT
    if msg.text:
        write_history(user.id, msg.text)
    else:
        write_history(user.id, "[非文本消息]")

    # 转发给管理员
    context.bot.forward_message(
        chat_id=ADMIN_CHAT_ID,
        from_chat_id=msg.chat_id,
        message_id=msg.message_id
    )


def reply_user(update: Update, context: CallbackContext):
    if update.effective_chat.id != ADMIN_CHAT_ID:
        return

    args = context.args
    if len(args) < 2:
        update.message.reply_text("用法：/reply 用户ID 内容")
        return

    user_id = int(args[0])
    text = " ".join(args[1:])

    context.bot.send_message(chat_id=user_id, text=text)
    update.message.reply_text("已发送")


def reply_photo(update: Update, context: CallbackContext):
    if update.effective_chat.id != ADMIN_CHAT_ID:
        return

    args = context.args
    if len(args) < 1:
        update.message.reply_text("用法：/photo 用户ID")
        return

    user_id = int(args[0])

    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        context.bot.send_photo(chat_id=user_id, photo=file_id)
        update.message.reply_text("图片已发送")
    else:
        update.message.reply_text("请附带一张图片")


def block_user(update: Update, context: CallbackContext):
    if update.effective_chat.id != ADMIN_CHAT_ID:
        return

    user_id = int(context.args[0])
    blocked_users.add(user_id)
    update.message.reply_text(f"已屏蔽用户 {user_id}")


def unblock_user(update: Update, context: CallbackContext):
    if update.effective_chat.id != ADMIN_CHAT_ID:
        return

    user_id = int(context.args[0])
    blocked_users.discard(user_id)
    update.message.reply_text(f"已解除屏蔽用户 {user_id}")


def main():
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_user_message))
    dp.add_handler(MessageHandler(Filters.photo, handle_user_message))

    dp.add_handler(CommandHandler("reply", reply_user))
    dp.add_handler(CommandHandler("photo", reply_photo))
    dp.add_handler(CommandHandler("block", block_user))
    dp.add_handler(CommandHandler("unblock", unblock_user))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
