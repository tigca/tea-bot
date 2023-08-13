import subprocess
import telebot
import logging
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent

# loggin
logging.basicConfig(level=logging.INFO)

# token from config.txt
with open('config.txt', 'r') as file:
    bot_token = file.read().strip()

# login
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('🎛️ Репозитории', callback_data='button1')
    button2 = InlineKeyboardButton('📖 FAQ', callback_data='button2')
    button3 = InlineKeyboardButton('🚫 Закрыть', callback_data='button3')
    keyboard.row(button1, button2)
    keyboard.row(button3)
    welcome_message = '<b>👋 Добро пожаловать в меню\n\n' \
                      '🐯 А тут, <a href="https://t.me/Uteagram">наш канал</a>\n' \
                      '🧑‍💻 И вот тут, <a href="https://t.me/UBteagram">чат</a>\n\n' \
                      '💚 Спасибо <a href="http://VIP_IPru_tw.t.me">VIP*</a>\n\n' \
                      '🤴 Версия бота: 0.1 [Beta] ⚡</b>'
    bot.send_message(message.chat.id, welcome_message, reply_markup=keyboard, parse_mode='HTML',
                     disable_web_page_preview=True, reply_to_message_id=message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == 'button3')
def close_menu(call):
    # delete
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == 'button1':
        repositories = user_repositories.get(call.message.chat.id, [])

        keyboard = types.InlineKeyboardMarkup()

        if repositories:
            for repo in repositories:
                repo_button = types.InlineKeyboardButton(
                    repo, callback_data=f'repo_{repo}')
                keyboard.add(repo_button)
        else:
            bot.send_message(call.message.chat.id,
                             'У вас нет подключенных репозиториев.')

        add_repo_button = types.InlineKeyboardButton(
            'Добавить репозиторий', callback_data='add_repo')
        keyboard.add(add_repo_button)
        bot.send_message(
            call.message.chat.id, 'Выберите репозиторий или добавьте новый:', reply_markup=keyboard)
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, 'soon...')
    elif call.data == 'button3':
        bot.send_message(call.message.chat.id, 'soon...')
    elif call.data == 'add_repo':
        set_state(call.message.chat.id, States.adding_repo)
        bot.send_message(call.message.chat.id, 'Введите URL репозитория:')


# start
if __name__ == "__main__":
    bot.polling()
