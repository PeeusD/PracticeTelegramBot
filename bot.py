from multiprocessing import Condition
from Pos import Adjective,Adverb,Articles,Conditional,Narration, Preposition,Noun,Pronoun,Sub_Agrmt,Tense,verb
from Fillers import Fill_pt1,Fill_pt2,Fill_pt3,Fill_pt4,Fill_pt5,Fill_pt6
from time import sleep
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters, CallbackQueryHandler
from telegram import ChatAction, Bot, ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup
from os import getenv
from dotenv import load_dotenv
load_dotenv()
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)      
TOKEN = getenv('TOKEN')
chat_id = getenv('CHAT_ID')
bot = Bot(token=TOKEN)
updater = Updater(TOKEN)


def questions_func(module_name):   #####  <--------------  CHANGE HERE FOR DEBUGGING  ------>
    if "Narration" in str(module_name): length = 20
    elif "Fill" in str(module_name): length = 30 
    else: length = 52

    for i in range(length):    
        bot.send_chat_action(chat_id = chat_id, action = ChatAction.TYPING)
        sleep(5)
        ques = '<b>' + module_name.questions[i][0] + '</b>'
        
        bot.send_message(chat_id=chat_id, text=ques, parse_mode=ParseMode.HTML)
        sleep(10)
        ans =  '<i>' + module_name.sol[i] + '</i>' 
        bot.send_message(chat_id=chat_id, text=ans, parse_mode=ParseMode.HTML)


def english_func(update, context):
    
    query = update.callback_query
    message_text =int(query.data)
    query.answer(text="Test has been Started!✔️")

    dct = {
        1: Adjective,
        2: Adverb,
        3: Articles,
        4: Conditional,
        5: verb,
        6: Noun,
        7: Preposition,
        8: Pronoun,
        9: Sub_Agrmt,
        10: Tense,
        11: Narration,
        12: Fill_pt1,
        13: Fill_pt2,
        14: Fill_pt3,
        15: Fill_pt4,
        16: Fill_pt5,
        17: Fill_pt6
    }
    questions_func(dct[message_text])
    

def start(update, contest):
    update.message.reply_text(
        '*Service is running\! 👍\nPlease select the test:\n/Errordetec :\- Error Detection 50question Sets\n/Fillers :\- Filler sets*',
        parse_mode='MarkdownV2'
     )


def fillers_kb(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Set-1", callback_data=12),
            InlineKeyboardButton("Set-2", callback_data=13),
        ],
        [
            InlineKeyboardButton("Set-3", callback_data=14),
            InlineKeyboardButton("Set-4", callback_data=15),
        ],
        [
            InlineKeyboardButton("Set-5", callback_data=16),
            InlineKeyboardButton("Set-6", callback_data=17),
        ],
       
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('*Please choose only one SET at a time:*', reply_markup=reply_markup, parse_mode='MarkdownV2')

def english_kb(update, context):

    keyboard = [
        [
            InlineKeyboardButton("Adjective", callback_data=1),
            InlineKeyboardButton("Adverb", callback_data=2),
            InlineKeyboardButton("Articles", callback_data=3),
            InlineKeyboardButton("Condtional", callback_data=4),
        ],
        [
            InlineKeyboardButton("Verb", callback_data=5),
            InlineKeyboardButton("Noun", callback_data=6),
            InlineKeyboardButton("Preposition", callback_data=7),
            InlineKeyboardButton("Pronoun", callback_data=8),
        ],
        [
            InlineKeyboardButton("SubAgrmt", callback_data=9),
            InlineKeyboardButton("Tense", callback_data=10),
            InlineKeyboardButton("Narration ", callback_data=11),
        ],
       
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('*Please choose only one SET at a time:*', reply_markup=reply_markup, parse_mode='MarkdownV2')


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Errordetec', english_kb))
updater.dispatcher.add_handler(CommandHandler('Fillers', fillers_kb))
updater.dispatcher.add_handler(CallbackQueryHandler(english_func)) # for getting callback data from keyboard

# updater.dispatcher.add_handler(MessageHandler(Filters.chat_type.private, schedulling1)) # for getting data from message
updater.start_polling()
updater.idle()