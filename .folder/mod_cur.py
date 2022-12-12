import requests
import datetime
import xmltodict
import telebot
# from main import app

# bot = app

def getCurrency(cur):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    valuteName = data['Valute'][cur]["Name"]
    valuteNominal = data['Valute'][cur]["Nominal"]
    valuteValue = data['Valute'][cur]["Value"]
    return (f' Текущий курс ЦБ РФ: {valuteValue} рублей за {valuteNominal} единиц(у) {valuteName}')

def getWeather(s_city):
    city_id = 0
    appid = '5316e5b35b9025d318bdda146d6e0dda'
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    city= data["name"]
    cur_weather = data['main']['temp']
    descript_weather =  data['weather'][0]['description']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure'] 
    wind =  data['wind']['speed']
    sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
    sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])
    day_time = sunset_time - sunrise_time

    return (f'***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***\n'
            f'Погода в городе: {city}\nТемпература: {cur_weather}C\nЗа окном: {descript_weather}\n'
            f'Влажность: {humidity} %\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n'
            f'Восход солнца: {sunrise_time}\nЗакат: {sunset_time}\nПродолжительность светового дная {day_time}')

def getHoroscope(zodiac):
    response = requests.get('http://img.ignio.com/r/export/utf/xml/daily/com.xml')
    dict_data = xmltodict.parse(response.content)
    value = dict_data['horo'][zodiac]["today"]#[8:]
    #value2 = dict_data['horo'][zodiac]["tomorrow"]#[8:]
    return (f'Гороскоп для {str.title(zodiac)} на сегодня: {value}\n')
           #f'Гороскоп для {str.title(zodiac)} на завтра: {value2}')

def get_act(data):
    if data == 'moscow':
        return getWeather(data)
    elif data == 'USD':
        return getCurrency(data)
    elif data == 'EUR':
        return getCurrency(data)
    else:
        return getHoroscope(data)    

# eng_rus_dict = {
#     'one': 'один',
#     'two': 'два',
#     'three': 'три',
#     'four': 'четыре',
#     'five': 'пять',
#     'six': 'шесть',
#     'seven': 'семь',
#     'eight': 'восемь',
#     'nine': 'девять',
#     'ten': 'десять'
# }


# def num_translate_adv(eng_word):
#     if eng_word[0].isupper():
#         eng_word = eng_word.lower()
#         return eng_rus_dict[eng_word].capitalize()
#     else:
#         return eng_rus_dict[eng_word]


# print(num_translate_adv('seven'))
# print(num_translate_adv('Seven'))


# value = ''
# old_value = ''

# def calc_mod():

#     keyboard = telebot.types.InlineKeyboardMarkup()
#     keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
#                 telebot.types.InlineKeyboardButton('C', callback_data='C'),
#                 telebot.types.InlineKeyboardButton('<=', callback_data='<='),
#                 telebot.types.InlineKeyboardButton('/', callback_data='/'))
#     keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
#                 telebot.types.InlineKeyboardButton('8', callback_data='8'),
#                 telebot.types.InlineKeyboardButton('9', callback_data='9'),
#                 telebot.types.InlineKeyboardButton('*', callback_data='*'))
#     keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
#                 telebot.types.InlineKeyboardButton('5', callback_data='5'),
#                 telebot.types.InlineKeyboardButton('6', callback_data='6'),
#                 telebot.types.InlineKeyboardButton('-', callback_data='-'))
#     keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
#                 telebot.types.InlineKeyboardButton('2', callback_data='2'),
#                 telebot.types.InlineKeyboardButton('3', callback_data='3'),
#                 telebot.types.InlineKeyboardButton('+', callback_data='+'))
#     keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
#                 telebot.types.InlineKeyboardButton('0', callback_data='0'),
#                 telebot.types.InlineKeyboardButton(',', callback_data='.'),
#                 telebot.types.InlineKeyboardButton('=', callback_data='='))


#     @bot.message_handler(commands=['start', 'go'])
#     def getMessage(message):
#         global value
#         if value == '':
#             bot.send_message(message.from_user.id,
#                             '0', reply_markup=keyboard)
#         else:
#             bot.send_message(message.from_user.id,
#                             value, reply_markup=keyboard)


#     @bot.callback_query_handler(func=lambda call: True)
#     def callback_func(query):
#         global value, old_value
#         data = query.data
#         if data == 'no':
#             pass
#         elif data == 'C':
#             value = ''
#         elif data == '<=':
#             if value != '':
#                 value = value[:len(value)-1]
#         elif data == '=':
#             value = str(eval(value))
#         else:
#             value += data
#         if value != old_value:
#             if value == '':
#                 bot.edit_message_text(
#                     chat_id=query.message.chat.id, message_id=query.message.id, text='0', reply_markup=keyboard)
#             else:
#                 bot.edit_message_text(chat_id=query.message.chat.id,
#                                     message_id=query.message.id, text=value, reply_markup=keyboard)
#             old_value = value


