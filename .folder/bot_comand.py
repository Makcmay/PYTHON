import model as m
import mod_cur as mc
import re
import json
import requests
import telegram
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext, filters, MessageHandler, CallbackQueryHandler, Updater
import datetime
from spy import*
import logging
import emoji

def get_token():
    with open('.folder/token.txt', 'r') as file:
        return file.read()

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')
    await update.message.reply_text(emoji.emojize(':thumbs_up:'))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/exchange')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def change_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split(', ')
    items[0] = items[0].replace('Список: ', '')
    print(items)
    await update.message.reply_text(', '.join(el.title() for el in items))

# async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     a = int(context.args[0]) + int(context.args[1]) 
#     await update.message.reply_text(f'{int(context.args[0]) + int(context.args[1])} = {a}')

async def currency_comand(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    # items = context.args[1].upper()
    items = msg.split()
    cur = items[1].upper()
    await update.message.reply_text(f'{mc.getCurrency(cur)}')

async def float_calc_comand(update: Update, context: CallbackContext):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    act = items[2]
    y = float(items[3])
    m.init(x, y, act)
    await update.message.reply_text(f'{x}{act}{y} = {m.do_it()}')

async def complex_calc_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    act = items[2]
    y = complex(items[3])
    m.init(x, y, act)
    await update.message.reply_text(f'{x}{act}{y} = {m.do_it()}')

async def weather_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    city = items[1]
    await update.message.reply_text(f'{mc.getWeather(city)}')

async def horoscope_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    # item = context.args
    # x = item[1].lower
    items = msg.split()
    zod = items[1]
    await update.message.reply_text(f'{mc.getHoroscope(zod)}')

async def startComand(update: Update, context: CallbackContext):
    buttonA = telegram.InlineKeyboardButton('Поздороваться', callback_data='buttonA')
    buttonB = telegram.InlineKeyboardButton('Посчитать сумму', callback_data='buttonB')
    buttonC = telegram.InlineKeyboardButton('Поменять список', callback_data='buttonC')
    buttonD = telegram.InlineKeyboardButton('Прогноз погоды', callback_data='buttonD')
    buttonE = telegram.InlineKeyboardButton('Курс валют', callback_data='buttonE')
    buttonF = telegram.InlineKeyboardButton('Комплексные', callback_data='buttonF')
    buttonG = telegram.InlineKeyboardButton('Вещетсвенные', callback_data='buttonG')
    buttonH = telegram.InlineKeyboardButton('Гороскоп', callback_data='buttonH')
    markup = telegram.InlineKeyboardMarkup(inline_keyboard =[[buttonA], [buttonB], [buttonC], [buttonD], [buttonE], [buttonF], [buttonG], [buttonH]])
    
    await update.message.reply_text('Добрый день, для начала жми на кнопу', reply_markup=markup)

    return callback



async def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'buttonA':
        await query.answer()
        await query.edit_message_text(text='Хотите поздороваться? Скажите Привет!')
    if variant == 'buttonB':
        await query.answer()
        await query.edit_message_text(text='Введите "Сумма: 2 числа через пробел"')
    if variant == 'buttonC':
        await query.answer()
        await query.edit_message_text(text='Введите "Список: список через зяпятую"')
    if variant == 'buttonD':
        await query.answer()
        await query.edit_message_text(text='Введите (Moscow, Tokyo, Paris) "Город: Moscow"')
    if variant == 'buttonE':
        await query.answer()
        await query.edit_message_text(text='Ведите (USD, GBF, EUR) "Валюта: USD"')
    if variant == 'buttonF':
        await query.answer()
        await query.edit_message_text(text='Ведите числа в формате "Комплексные: x действие y"')
    if variant == 'buttonG':
        await query.answer()
        await query.edit_message_text(text='Ведите числа в формате "Вещественные: x действие y"')        
    if variant == 'buttonH':
        await query.answer()
        await query.edit_message_text(text='Ведите знак зодиака "Знак: Aquarius"')


start_command_handler = CommandHandler('start', startComand)
# start_calc_command_handler =  CommandHandler('calc', start_calc_comand)
hello_handler = MessageHandler(filters.Regex('Привет'), hi_command)
sum_handler = MessageHandler(filters.Regex('Сумма: '), sum_command)
list_handler = MessageHandler(filters.Regex('Список: '), change_list)
weather_handler = MessageHandler(filters.Regex('Город: '), weather_comand)
currency_handler = MessageHandler(filters.Regex('Валюта: '), currency_comand)
compl_handler =  MessageHandler(filters.Regex('Комплексные: '), complex_calc_comand)
float_handler =  MessageHandler(filters.Regex('Вещественные: '), float_calc_comand)
horoscope_handler =  MessageHandler(filters.Regex('Знак: '), horoscope_comand)
callback_button_handler = CallbackQueryHandler(callback=callback, pattern=None)