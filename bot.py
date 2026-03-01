from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import TELEGRAM_TOKEN
from transcript import get_transcript
from summarizer import generate_summary
from qa_engine import build_qa_system

user_sessions = {}
user_transcripts = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "1️⃣ Send a YouTube link\n"
        "2️⃣ Get structured summary\n"
        "3️⃣ Ask questions\n\n"
        "Commands:\n"
        "/summary\n"
        "/deepdive\n"
        "/actionpoints\n"
        "/hindi"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.strip()

    if "youtube.com" in text or "youtu.be" in text:
        try:
            await update.message.reply_text("Downloading & transcribing...")

            transcript = get_transcript(text)
            user_transcripts[user_id] = transcript

            await update.message.reply_text("Generating summary...")
            summary = generate_summary(transcript)

            qa_system = build_qa_system(transcript)
            user_sessions[user_id] = qa_system

            await update.message.reply_text(summary)
            await update.message.reply_text(
                "Ready! Ask me anything about this video."
            )

        except Exception as e:
            await update.message.reply_text(f"Error: {str(e)}")

    else:
        if user_id in user_sessions:
            qa_system = user_sessions[user_id]
            await update.message.reply_text("Thinking...")
            answer = qa_system.run(text)
            await update.message.reply_text(answer)
        else:
            await update.message.reply_text("Please send a YouTube link first.")

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id in user_transcripts:
        summary_text = generate_summary(user_transcripts[user_id])
        await update.message.reply_text(summary_text)
    else:
        await update.message.reply_text("Send a YouTube link first.")

async def deepdive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id in user_transcripts:
        detailed_prompt = (
            "Provide a detailed deep-dive explanation of the following transcript:\n\n"
            + user_transcripts[user_id]
        )
        qa_system = user_sessions[user_id]
        answer = qa_system.run(detailed_prompt)
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text("Send a YouTube link first.")

async def actionpoints(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id in user_transcripts:
        action_prompt = (
            "Extract practical action points from this transcript:\n\n"
            + user_transcripts[user_id]
        )
        qa_system = user_sessions[user_id]
        answer = qa_system.run(action_prompt)
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text("Send a YouTube link first.")

async def hindi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id in user_transcripts:
        hindi_prompt = (
            "Summarize this transcript in Hindi:\n\n"
            + user_transcripts[user_id]
        )
        qa_system = user_sessions[user_id]
        answer = qa_system.run(hindi_prompt)
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text("Send a YouTube link first.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("summary", summary))
    app.add_handler(CommandHandler("deepdive", deepdive))
    app.add_handler(CommandHandler("actionpoints", actionpoints))
    app.add_handler(CommandHandler("hindi", hindi))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()