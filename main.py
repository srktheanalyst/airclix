import os
import random

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

TOKEN = my_secret = os.environ['YOUR_TELEGRAM_BOT_TOKEN']

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Type /spin to play the roulette!')

def spin(update: Update, context: CallbackContext) -> None:  
    outcomes = ['You missed! Try again!',
                'Congratulations! You won a YouTube coupon!',
                'Lucky spin! You won an Amazon coupon!',
                'Jackpot! You won a Flipkart coupon!']
    outcome = random.choice(outcomes)
    update.message.reply_text(outcome)

def main() -> None:
    from telegram.ext import Updater
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    spin_handler = CommandHandler('spin', spin)
    dispatcher.add_handler(spin_handler)

    updater.start_polling()
    updater.idle()

