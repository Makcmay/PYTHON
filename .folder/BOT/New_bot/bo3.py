import telebot
import requests
from bs4 import BeautifulSoup
from collections import Counter

TOKEN = '5803452933:AAFp9btc6IWhDag175RexyvkjqBwMMQGIPs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Пожалуйста, введите адрес сайта:")

@bot.message_handler(func=lambda message: True)
def analyze_website(message):
    try:
        url = message.text
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        # Анализ текста
        symbols_count = len(text)
        spaces_count = text.count(' ')
        most_common_symbol = Counter(text).most_common(1)[0][0]

        # Подсчет кириллических символов
        cyrillic_chars = [char for char in text if char.isalpha() and char.isalpha() and char.isalpha()]
        most_common_cyrillic_chars = Counter(cyrillic_chars).most_common(10)

        # Подсчет русских слов
        words = [word for word in text.split() if word.isalpha() and len(word) >= 5]
        most_common_words = Counter(words).most_common(10)

        analysis_results = {
            "Количество символов в коде": symbols_count,
            "Количество пробелов": spaces_count,
            "Самый частый символ": most_common_symbol,
            "10 самых часто встречающихся кириллических символов": most_common_cyrillic_chars,
            "10 самых часто встречающихся русских слов (5 и более букв)": most_common_words
        }

        bot.send_message(message.chat.id, "Выберите вид анализа:", reply_markup=create_keyboard(analysis_results))
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

def create_keyboard(analysis_results):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for analysis_type, result in analysis_results.items():
        callback_data = f"analyze_{analysis_type}"
        button = telebot.types.InlineKeyboardButton(text=analysis_type, callback_data=callback_data)
        keyboard.add(button)
    return keyboard

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    analysis_type = call.data.split('_')[1]
    result = analysis_results.get(analysis_type, "Неверный запрос")
    bot.send_message(call.message.chat.id, f"{analysis_type}:\n{result}")

bot.polling()
