from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

OWNER_ID = 7294913764  # Replace with your actual Telegram ID
TOKEN = "8031248332:AAFkWRXZKkF4usbYFZi8F6OAv3NABYYgWa8"

total = 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to ShopBot!\nUse /add, /minus, /total, /reset")

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    global total
    try:
        amount = int(context.args[0])
        if amount < 0:
            await update.message.reply_text("🚫 Negative amounts are not allowed in /add. Use /minus instead.")
            return
        total += amount
        await update.message.reply_text(f"✅ Added ${amount}.")
    except:
        await update.message.reply_text("❌ Usage: /add <amount> (e.g., /add 500)")


async def minus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global total
    try:
        amount = int(context.args[0])
        total -= amount
        await update.message.reply_text(f"➖ Subtracted ${amount}.")
    except:
        await update.message.reply_text("❌ Usage: /minus <amount> (e.g., /minus 200)")

async def total_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💰 Current total is ${total}.")

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global total
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("🚫 You are not authorized to reset.")
        return
    total = 0
    await update.message.reply_text("🔄 Total has been reset to ₹0.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("minus", minus))
    app.add_handler(CommandHandler("total", total_cmd))
    app.add_handler(CommandHandler("reset", reset))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
