import telebot
from telebot import types
import mod_cur as mc
# from transliterate import translit, get_available_language_codes
# from textblob import TextBlob 
# from translate import Translator
import logging
 


def get_token():
    with open('.folder/BOT/CalcBot/token.txt', 'r') as file:
        return file.read()


bot = telebot.TeleBot(get_token())

value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('Козерог', callback_data='capricorn'),
             telebot.types.InlineKeyboardButton('Водолей', callback_data='aquarius'),
             telebot.types.InlineKeyboardButton('Рыбы', callback_data='pisces'),
             telebot.types.InlineKeyboardButton('Овен', callback_data='aries'))
keyboard.row(telebot.types.InlineKeyboardButton('Телец', callback_data='taurus'),
             telebot.types.InlineKeyboardButton('Близнецы', callback_data='gemini'),
             telebot.types.InlineKeyboardButton('Рак', callback_data='cancer'),
             telebot.types.InlineKeyboardButton('Лев', callback_data='leo'))
keyboard.row(telebot.types.InlineKeyboardButton('Дева', callback_data='virgo'),
             telebot.types.InlineKeyboardButton('Весы', callback_data='libra'),
             telebot.types.InlineKeyboardButton('Скорпион', callback_data='scorpio'),
             telebot.types.InlineKeyboardButton('Стрелец', callback_data='sagittarius'))
keyboard.row(telebot.types.InlineKeyboardButton('Погода', callback_data='moscow'),
             telebot.types.InlineKeyboardButton('Курс USD', callback_data='USD'),
             telebot.types.InlineKeyboardButton('Курс EUR', callback_data='EUR'))
keyboard.add(telebot.types.InlineKeyboardButton('Очистить', callback_data='del'))



@bot.message_handler(commands=['start', 'go'])

def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id,
                         'Выбирай', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id,
                         value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    
    global value, old_value
    data = query.data
    if data == '':
        pass
    elif data == 'del':
        value = ''
    elif data == data:
        # translator= Translator(to_lang="Ru")
        # text = translator.translate(data)
        # text = translit(data, 'ru')
        # blob = TextBlob(data) 
        # text = blob.translate(to='fr')
        value = mc.get_act(data)
        
        # text = "Privet"
        # print(translit(text, 'ru'))
    # elif data == '<=':
    #     if value != '':
    #         value = value[:len(value)-1]
    # elif data == '=':
    #     value = str(eval(value))
    # else:
    #     value += data
    if value != old_value:
        if value == '':
            bot.edit_message_text(
                chat_id=query.message.chat.id, message_id=query.message.id, text='Выбирай', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.id, text=value, reply_markup=keyboard)
        old_value = value

print('server start')

bot.polling()
