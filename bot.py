from auxiliar import *
from auxiliar1 import bot_token
import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import pandas as pd

##### config
# formatting the float columns as currency
pd.options.display.float_format = '${:,.2f}'.format

##### files
# read the csv
transactions = pd.read_csv('C:/Users/BI/Desktop/Heryc/Bot-Finanzas-V2/db/movimientos.csv', encoding='utf-8')
accounts_db = pd.read_csv('C:/Users/BI/Desktop/Heryc/Bot-Finanzas-V2/db/cuentas.csv', encoding='utf-8')

##### For logging how the bot it's doing
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

##### Handler functions

# for start command: /start
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm your financial bot, I'll help you keep track of your expenses!")

# for last n instruction: last n
def last_n(update: Update, context: CallbackContext):
    """Generates an image with the last n transactions"""
    msg = update.message.text

    try:
        n = min(int(msg.split()[1]), transactions.shape[0])
        saves_png(transactions.tail(n), 'last_n', 'C:/Users/BI/Desktop/Heryc/Bot-Finanzas-V2/img/')
        update.message.bot.send_photo(chat_id=update.effective_chat.id, photo=open('img/last_n.png', 'rb'))
    except ValueError:
        update.message.reply_text("Sorry, there was a problem with the number of rows")
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="There was an error, we'll work into it")

# function to echo any message that it's not a command
def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# function to handle a command that it's not defined
def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

##### Bot configuration
upd = Updater(token=bot_token, use_context=True)

disp = upd.dispatcher

disp.add_handler(CommandHandler('start', start))

disp.add_handler(MessageHandler(Filters.regex(r'last *') & (~Filters.command), last_n))

disp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

disp.add_handler(MessageHandler(Filters.command, unknown))

upd.start_polling()

print('Bot running')

upd.idle()

print('End')

