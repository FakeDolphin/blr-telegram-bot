import time
import telepot

from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


# https://telepot.readthedocs.io/en/latest/#id8
# your api token
API_TOKEN = ''

bot = telepot.Bot(API_TOKEN)
response = bot.getUpdates()


# При появлении сообщения в чате
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Press me', callback_data='press')],
               ])

    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)


# to react to callback query
def on_callback_query(msg):
    #accept data which we need
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')


def handle(msg):
    print(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)


# MessageLoop(bot, handle).run_as_thread()
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()


while 1:
    time.sleep(10)