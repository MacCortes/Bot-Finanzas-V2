from auxiliar import *
from auxiliar1 import bot_token
import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

# For logging how the bot it's doing
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Handler functions
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Bot configuration
upd = Updater(token=bot_token, use_context=True)

disp = upd.dispatcher

disp.add_handler(CommandHandler('start', start))

disp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

upd.start_polling()

print('Bot running')

upd.idle()

print('End')

