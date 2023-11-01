import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup
from collections import Counter
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# def start(update, context):
#     chat_id = update.message.chat_id
#     text = 'Введите адрес сайта:'
#     context.bot.send_message(chat_id=chat_id, text=text)


def get_html_content(url):
    response = requests.get(url)
    return response.text


def get_top_chars(text):
    cyrillic_chars = [char for char in text if char.isalpha() and char.isalpha() and char.islower()]
    top_chars = Counter(cyrillic_chars).most_common(10)
    return top_chars


def get_top_words(text):
    words = [word.lower() for word in text.split() if word.isalpha() and len(word) >= 5]
    top_words = Counter(words).most_common(10)
    return top_words


def get_code_stats(text):
    num_chars = len(text)
    num_spaces = text.count(' ')
    top_char = Counter(text).most_common(1)[0]
    return num_chars, num_spaces, top_char

def get_token():
    with open('.folder/BOT/CalcBot/token.txt', 'r') as file:
        return file.read()


bot = telebot.TeleBot('5803452933:AAFp9btc6IWhDag175RexyvkjqBwMMQGIPs')

value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton("10 самых часто встречающихся кириллических символов", callback_data='top_chars'))
keyboard.row(telebot.types.InlineKeyboardButton("10 самых часто встречающихся русских слов", callback_data='top_words'))
keyboard.row(telebot.types.InlineKeyboardButton("Количество символов, пробелов, самый частый символ", callback_data='code_stats'))
keyboard.row(telebot.types.InlineKeyboardButton("Полный анализ", callback_data='full_analysis'))
keyboard.add(telebot.types.InlineKeyboardButton('Очистить', callback_data='del'))



@bot.message_handler(commands=['start', 'go'])
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id,
                         'Введи', reply_markup=keyboard)
        value = bot.register_next_step_handler(message.from_user.id)
    else:
        bot.send_message(message.from_user.id,
                         value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data
    if data == '':
        pass
    elif data == 'C':
        value = ''
    elif data == 'top_chars':
        top_chars = get_top_chars(value)
        value = "\n".join([f"{char}: {count}" for char, count in top_chars])
        # value = mc.getHoroscope('capricorn')
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
    elif data == '=':
        value = str(eval(value))
    else:
        value += data
    if value != old_value:
        if value == '':
            bot.edit_message_text(
                chat_id=query.message.chat.id, message_id=query.message.id, text='Введите сайт', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.id, text=value, reply_markup=keyboard)
        old_value = value


print('server start')

bot.polling()
# def analyze_website(update, context):
#     url = update.message.text
#     html_content = get_html_content(url)
    
#     reply_markup = InlineKeyboardMarkup(buttons)
#     update.message.reply_text("Выберите тип анализа:", reply_markup=reply_markup)

#     context.user_data['html_content'] = html_content
#     buttons = [
#         [InlineKeyboardButton("10 самых часто встречающихся кириллических символов", callback_data='top_chars')],
#         [InlineKeyboardButton("10 самых часто встречающихся русских слов", callback_data='top_words')],
#         [InlineKeyboardButton("Количество символов, пробелов, самый частый символ", callback_data='code_stats')],
#         [InlineKeyboardButton("Полный анализ", callback_data='full_analysis')]
#     ]

    # reply_markup = InlineKeyboardMarkup(buttons)
    # update.message.reply_text("Выберите тип анализа:", reply_markup=reply_markup)

    # context.user_data['html_content'] = html_content


# def button_callback(update, context):
#     query = update.callback_query
#     analysis_type = query.data
#     html_content = context.user_data['html_content']

#     if analysis_type == 'top_chars':
#         top_chars = get_top_chars(html_content)
#         text = "\n".join([f"{char}: {count}" for char, count in top_chars])
#     elif analysis_type == 'top_words':
#         top_words = get_top_words(html_content)
#         text = "\n".join([f"{word}: {count}" for word, count in top_words])
#     elif analysis_type == 'code_stats':
#         num_chars, num_spaces, top_char = get_code_stats(html_content)
#         text = f"Количество символов: {num_chars}\nКоличество пробелов: {num_spaces}\nСамый частый символ: {top_char[0]}"
#     else:
#         top_chars = get_top_chars(html_content)
#         top_words = get_top_words(html_content)
#         num_chars, num_spaces, top_char = get_code_stats(html_content)

#         text = "10 самых часто встречающихся кириллических символов:\n"
#         text += "\n".join([f"{char}: {count}" for char, count in top_chars])
#         text += "\n\n10 самых часто встречающихся русских слов:\n"
#         text += "\n".join([f"{word}: {count}" for word, count in top_words])
#         text += f"\n\nКоличество символов: {num_chars}\nКоличество пробелов: {num_spaces}\nСамый частый символ: {top_char[0]}"

#     query.edit_message_text(text=text)


# if __name__ == '__main__':
#     TOKEN = ('5803452933:AAFp9btc6IWhDag175RexyvkjqBwMMQGIPs')
#     updater = Updater(TOKEN, use_context=True)
#     dispatcher = updater.dispatcher

#     start_handler = CommandHandler('start', start)
#     dispatcher.add_handler(start_handler)

#     analyze_handler = CommandHandler('analyze', analyze_website)
#     dispatcher.add_handler(analyze_handler)

#     button_handler = CallbackQueryHandler(button_callback)
#     dispatcher.add_handler(button_handler)

#     print('server start')
#     updater.start_polling()