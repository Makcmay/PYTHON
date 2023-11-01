import telebot
from collections import Counter
from bs4 import BeautifulSoup
import requests
import http.client
from urllib.request import urlopen

TOKEN = '5803452933:AAFp9btc6IWhDag175RexyvkjqBwMMQGIPs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Введите адрес сайта (с https или без):")

@bot.message_handler(func=lambda message: True)
def analyze_website(message):
    url = message.text
    try:
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # text_content = soup.get_text()
    

        
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        text_content = soup.get_text()


        # url = requests.get(url)
        


        # Обработка текста сайта
        cyrillic_chars = [char for char in text_content if char.isalpha() and char.isalpha() and char.isalpha() in 'А-Яа-я']
        words = [word for word in text_content.split() if len(word) >= 5 and word.isalpha() and word.isalpha() in 'А-Яа-я']

        # Количество символов в коде, количество пробелов, самый частый символ
        total_chars = len(text_content)
        spaces_count = text_content.count(' ')
        most_common_char = Counter(text_content).most_common(1)[0][0]

        @bot.callback_query_handler(func=lambda call: True)
        def handle_query(call):
            if call.data == '1':
                # 10 самых часто встречающихся кириллических символов
                top_cyrillic_chars = Counter(cyrillic_chars).most_common(10)
                result = '\n'.join([f'{char}: {count}' for char, count in top_cyrillic_chars])
                bot.send_message(call.message.chat.id, result)
            elif call.data == '2':
                # 10 самых часто встречающихся русских слов (5 и более букв)
                top_words = Counter(words).most_common(10)
                result = '\n'.join([f'{word}: {count}' for word, count in top_words])
                bot.send_message(call.message.chat.id, result)
            elif call.data == '3':
                # Количество символов в коде, количество пробелов, самый частый символ
                result = f"Общее количество символов: {total_chars}\nКоличество пробелов: {spaces_count}\nСамый частый символ: {most_common_char}"
                bot.send_message(call.message.chat.id, result)

        # Показываем кнопки для анализа
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Топ кириллических символов', callback_data='1'),
            telebot.types.InlineKeyboardButton('Топ русских слов', callback_data='2')
        )
        keyboard.row(telebot.types.InlineKeyboardButton('Полный анализ', callback_data='3'))
        bot.send_message(message.chat.id, "Выберите опцию для анализа:", reply_markup=keyboard)

    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
print('server start')
bot.polling()
