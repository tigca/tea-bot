import telebot
import logging
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent

# loggin
logging.basicConfig(level=logging.INFO)

# login
bot = telebot.TeleBot('6644438998:AAGbN3fC7PyLSS1O9K_OjugUvoisn5cakKc')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    info = InlineKeyboardButton('🧑‍💻 Добавить/удалить модуль', url='https://t.me/UBteagram')
    close = InlineKeyboardButton('🚫 Закрыть', callback_data='close')
    keyboard.row(info)
    keyboard.row(close)
    welcome_message = '<b>👋 Добро пожаловать в меню\n\n' \
                      '🍵 А тут, <a href="https://t.me/UBteagram">наш чат</a>\n' \
                      '💚 Работает на <a href="http://TriggerEarth.t.me">TriggerEarth Cloud</a>\n\n' \
                      '🤴 Версия бота: 0.1 [Beta] ⚡</b>'
    bot.send_message(message.chat.id, welcome_message, reply_markup=keyboard, parse_mode='HTML',
                     disable_web_page_preview=True, reply_to_message_id=message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == 'close')
def close_menu(call):
    # delete
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.answer_callback_query(call.id)
    
@bot.message_handler(func=lambda message: True)
def search_word(message):
    word = message.text.lower()
    with open('modules.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if word in line.lower():
                bot.send_message(message.chat.id, line)
                break


# start
if __name__ == "__main__":
    bot.polling()
