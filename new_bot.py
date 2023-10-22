"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""


from telegram import ForceReply, ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"hello {user.mention_html()} Welcome to the udemy course vbj bot i am helping to find the course!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("This bot is help to find the best course on udemy if any query then contact the devloper @Vbj01")

options = [["App Development"], ["Web Development"], ["Ethical Hacking"], ["Web Application"],
           ["Cyber Security"], ["Wifi-Hacking"], ["Computer Networks"], ["Video Editing"],
           ["Chat-gpt"], ["Software Development"], ["Other"]]

async def course_command(update: Update,context:ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = ReplyKeyboardMarkup(options, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("select one option",reply_markup=keyboard)
    

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    msg=update.message.text
    
    print(options)
    
    


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("Token").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("course", course_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
