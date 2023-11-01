import telebot
import requests
from bs4 import BeautifulSoup
from collections import Counter

# Устанавливаем токен вашего бота
TOKEN = 'YOUR TOKEN'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Введите адрес веб-сайта (с https:// или без):")

@bot.message_handler(func=lambda message: True)
def handle_website_input(message):
    website_url = message.text
    # print(website_url)
    try:
        response = requests.get(website_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        print(soup)
        # html_content = soup.get_text().encode('utf-8')
        html_content = soup.get_text()
        analyze_markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        analyze_markup.add(telebot.types.KeyboardButton("1. Топ-10 символов"),
                          telebot.types.KeyboardButton("2. Топ-10 слов"),
                          telebot.types.KeyboardButton("3. Количество символов, пробелов, самый частый символ"),
                          telebot.types.KeyboardButton("4. Полный анализ"))

        bot.send_message(message.chat.id, "Выберите действие для анализа:", reply_markup=analyze_markup)
        bot.register_next_step_handler(message, handle_analysis_choice, html_content)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
    # print(html_content)
    # print(message)
def handle_analysis_choice(message, html_content):
    choice = message.text.lower()
    if choice == "1. топ-10 символов":
        cyrillic_chars = [char for char in html_content if char.isalpha() and char.isalpha() and char.isalpha()]
        print(html_content)
        char_counts = Counter(cyrillic_chars)
        top_chars = char_counts.most_common(10)
        result = "Топ-10 символов:\n"
        for char, count in top_chars:
            result += f"{char}: {count}\n"
        bot.send_message(message.chat.id, result)
    elif choice == "2. топ-10 слов":
        words = [word for word in html_content.split() if word.isalpha() and len(word) >= 5]
        word_counts = Counter(words)
        top_words = word_counts.most_common(10)
        result = "Топ-10 слов:\n"
        for word, count in top_words:
            result += f"{word}: {count}\n"
        bot.send_message(message.chat.id, result)
    elif choice == "3. количество символов, пробелов, самый частый символ":
        char_count = len(html_content)
        space_count = html_content.count(" ")
        char_counts = Counter(html_content)
        most_common_char = char_counts.most_common(1)[0]
        result = f"Количество символов: {char_count}\nКоличество пробелов: {space_count}\nСамый частый символ: '{most_common_char[0]}' ({most_common_char[1]} раз)"
        bot.send_message(message.chat.id, result)
    elif choice == "4. полный анализ":
        # Выполнить полный анализ здесь, если требуется
        cyrillic_chars = [c for c in html_content if 'А' <= c <= 'я']
        most_common_chars = Counter(cyrillic_chars).most_common(10)
        words = html_content.split()
        russian_words = [word for word in words if all('А' <= c <= 'я' for c in word)]
        most_common_words = Counter(russian_words).most_common(10)
        chars_count = len(html_content)
        spaces_count = html_content.count(' ')
        most_common_char = Counter(html_content).most_common(1)[0][0]
        best_char = Counter(cyrillic_chars).most_common(1)
        
        result = 'Самые часто встречающиеся символы:\n'
        for char, count in most_common_chars:
            result += f'{char}: {count}\n'

        result += '\nСамые часто встречающиеся слова (5 и более букв):\n'
        for word, count in most_common_words:
            if len(word) >= 5:
                result += f'{word}: {count}\n'

        result += f'\nКоличество символов: {chars_count}\nКоличество пробелов: {spaces_count}\nСамый частый символ: {best_char[0]}'
        bot.send_message(message.chat.id, result)

        # bot.send_message(message.chat.id, "Извините, этот функционал еще не реализован.")
    else:
        bot.send_message(message.chat.id, "Неверный выбор. Пожалуйста, выберите одну из предложенных опций.")
        
    bot.send_message(message.chat.id, "Привет! Введите адрес веб-сайта (с https:// или без):")
# Запускаем бота
print('server start')
bot.polling(none_stop=True)
