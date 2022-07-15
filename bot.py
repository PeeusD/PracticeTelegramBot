from Pos import Adjective,Adverb,Articles,Conditional,Narration, Preposition,Noun,Pronoun,Sub_Agrmt,Tense,verb
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


def adjective_query():   #####  <--------------  CHANGE HERE FOR DEBUGGING  ------>
    for i in range(52):    
            sleep(5)
            ques = Adjective.questions[i][0]
            print(ques)
            sleep(10)
            ans = Adjective.sol[i] 
            print(ans)

def adverb_query():
    for i in range(52): 
        sleep(5)       
        ques = Adverb.questions[i][0]
        # print(ques)
        bot.send_message(chat_id = chat_id, text = ques, parse_mode = ParseMode.HTML)
        sleep(10)
        ans = Adverb.sol[i]
        # print(ans)
        bot.send_message(chat_id = chat_id, text = ans, parse_mode = ParseMode.HTML)
def articles_query():
    for i in range(52):  
        sleep(5)  
        ques = Articles.questions[i][0]
        print(ques)
        sleep(10)
        ans = Articles.sol[i]
        print(ans)
def condtional_query():
    for i in range(52):   
        sleep(5) 
        ques = Conditional.questions[i][0]
        print(ques)
        sleep(10)
        ans = Conditional.sol[i]
        print(ans)
def verb_query():
    for i in range(52):
        sleep(5)
        ques = verb.questions[i][0]
        print(ques)
        sleep(10)
        ans = verb.sol[i]
        print(ans)
def noun_query():
    for i in range(52):
        sleep(5)
        ques = Noun.questions[i][0]
        print(ques)
        sleep(10)
        ans = Noun.sol[i]
        print(ans)
def narr_query():
    for i in range(20):
        sleep(5)
        ques = Narration.questions[i][0]
        print(ques)
        sleep(10)
        ans = Narration.sol[i]
        print(ans)
def preposition_query():
    for i in range(52):
        sleep(5)
        ques = Preposition.questions[i][0]
        print(ques)
        sleep(10)
        ans = Preposition.sol[i]
        print(ans)
def pronoun_query():
    for i in range(52):
        sleep(5)
        ques = Pronoun.questions[i][0]
        print(ques)
        sleep(10)
        ans = Pronoun.sol[i]
        print(ans)
def subAgrmt_query():
    for i in range(52): 
        sleep(5)       
        ques = Sub_Agrmt.questions[i][0]
        print(ques)
        sleep(10)
        ans = Sub_Agrmt.sol[i]
        print(ans)
def tense_query():
    for i in range(52):  
        sleep(5)  
        ques = Tense.questions[i][0]
        print(ques)
        sleep(10)
        ans = Tense.sol[i]
        print(ans)



def schedulling1(update, context):
    
    query = update.callback_query
    message_text =int(query.data)
    query.answer(text="Test has been Started!✔️")

    dct = {
        1: adjective_query,
        2: adverb_query,
        3: articles_query,
        4: condtional_query,
        5: verb_query,
        6: noun_query,
        7: preposition_query,
        8: pronoun_query,
        9: subAgrmt_query,
        10: tense_query,
        11: narr_query
    }
    
    d = dct[message_text]()
    return d


def start(update, context):

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

    update.message.reply_text('*Service is running\! 👍\nPlease choose only one SET at a time:*', reply_markup=reply_markup, parse_mode='MarkdownV2')



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(schedulling1)) # for getting callback data from keyboard
# updater.dispatcher.add_handler(MessageHandler(Filters.chat_type.private, schedulling1)) # for getting data from message
updater.start_polling()
updater.idle()