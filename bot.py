import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN
from utils.learner import learn_pair
from utils.matcher import find_best_reply

logging.basicConfig(level=logging.INFO)

bot_messages = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg or not msg.text or not msg.from_user:
        return

    user_id = msg.from_user.id
    text = msg.text.strip()

    # Learn from replies
    if msg.reply_to_message and msg.reply_to_message.text:
        learn_pair(msg.reply_to_message.text.strip(), text)

    # Respond from memory
    reply = find_best_reply(text)
    if reply:
        await msg.reply_text(reply)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()