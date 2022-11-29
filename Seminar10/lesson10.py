import requests

# делаем запрос по адресу
response = requests.get('https://geekbrains.ru/')
print(response) # 200 - значит успешно, по кодам запроса можно узнать на вике
print('*' * 50)
print(dir(response))
print('*' * 50)
print(type(response))

print(response.status_code)
#
if response:
    print('Ok')

if response.status_code == 200:
    print('Ok')


'''
Р°С‚СЂРёР±СѓС‚ headers вЂ” СЃР»РѕРІР°СЂСЊ СЃ Р·Р°РіРѕР»РѕРІРєР°РјРё РѕС‚РІРµС‚Р° СЃРµСЂРІРµСЂР°;
Р°С‚СЂРёР±СѓС‚ status_code вЂ” С‡РёСЃР»Рѕ, РєРѕРґ РѕС‚РІРµС‚Р° СЃРµСЂРІРµСЂР°;
Р°С‚СЂРёР±СѓС‚ content вЂ” СЃРѕРґРµСЂР¶РёРјРѕРµ РѕС‚РІРµС‚Р° РІ Р±Р°Р№С‚Р°С…;
РјРµС‚РѕРґ close() вЂ” РѕСЃРІРѕР±РѕР¶РґР°РµС‚ (Р·Р°РєСЂС‹РІР°РµС‚) СЃРѕРµРґРёРЅРµРЅРёРµ.
'''

'''
Response.apparent_encoding РІРѕР·РІСЂР°С‰Р°РµС‚ РєРѕРґРёСЂРѕРІРєСѓ, СѓРіР°РґР°РЅРЅСѓСЋ chardet,
Response.close() РѕСЃРІРѕР±РѕР¶РґР°РµС‚ СЃРѕРµРґРёРЅРµРЅРёРµ СЃ РїСѓР»РѕРј,
Response.cookies РІРѕР·РІСЂР°С‰Р°РµС‚ cookies, СѓСЃС‚Р°РЅРѕРІР»РµРЅРЅС‹Рµ СЃРµСЂРІРµСЂРѕРј,
Response.elapsed РІРѕР·РІСЂР°С‰Р°РµС‚ РІСЂРµРјСЏ, РїРѕС‚СЂР°С‡РµРЅРЅРѕРµ РЅР° Р·Р°РїСЂРѕСЃ,
Response.encoding СѓСЃС‚Р°РЅР°РІР»РёРІР°РµС‚ РєРѕРґРёСЂРѕРІРєСѓ, РґР»СЏ РґРµРєРѕРґРёСЂРѕРІР°РЅРёСЏ,
Response.history РІРѕР·РІСЂР°С‰Р°РµС‚ РёСЃС‚РѕСЂРёСЋ РїРµСЂРµРЅР°РїСЂР°РІР»РµРЅРёР№,
Response.is_permanent_redirect РѕРїСЂРµРґРµР»РµРЅРёРµ РїРѕСЃС‚РѕСЏРЅРЅС‹С… СЂРµРґРёСЂРµРєС‚РѕРІ,
Response.is_redirect РµСЃС‚СЊ Р»Рё СЂРµРґРёСЂРµРєС‚,
Response.iter_content() РїРµСЂРµР±РёСЂР°РµС‚ РґР°РЅРЅС‹Рµ РѕС‚РІРµС‚Р° РєСѓСЃРєР°РјРё,
Response.iter_lines() РїРµСЂРµР±РёСЂР°РµС‚ РґР°РЅРЅС‹Рµ РѕС‚РІРµС‚Р°, РїРѕ РѕРґРЅРѕР№ СЃС‚СЂРѕРєРµ,
Response.json() РІРѕР·РІСЂР°С‰Р°РµС‚ РѕС‚РІРµС‚ РІ РІРёРґРµ JSON,
Response.links РІРѕР·РІСЂР°С‰Р°РµС‚ СЃСЃС‹Р»РєРё Р·Р°РіРѕР»РѕРІРєР° РѕС‚РІРµС‚Р°,
Response.next РІРѕР·РІСЂР°С‰Р°РµС‚ РѕР±СЉРµРєС‚ PreparedRequest,
Response.ok True, РµСЃР»Рё status_code РјРµРЅСЊС€Рµ 400,
Response.raise_for_status() РІС‹Р·С‹РІР°РµС‚ РёСЃРєР»СЋС‡РµРЅРёРµ HTTPError,
Response.raw РІРѕР·РІСЂР°С‰Р°РµС‚ РѕС‚РІРµС‚Р° РІ РІРёРґРµ С„Р°Р№Р»РѕРІРѕРіРѕ РѕР±СЉРµРєС‚Р°,
Response.reason РІРѕР·РІСЂР°С‰Р°РµС‚ С‚РµРєСЃС‚РѕРІРѕРµ РїСЂРµРґСЃС‚Р°РІР»РµРЅРёРµ РѕС‚РІРµС‚Р°,
Response.request РІРѕР·РІСЂР°С‰Р°РµС‚ РѕР±СЉРµРєС‚ PreparedRequest Р·Р°РїСЂРѕСЃР°,
Response.status_code РІРѕР·РІСЂР°С‰Р°РµС‚ РєРѕРґ РѕС‚РІРµС‚Р° СЃРµСЂРІРµСЂР°,
Response.text РІРѕР·РІСЂР°С‰Р°РµС‚ РєРѕРЅС‚РµРЅС‚ РѕС‚РІРµС‚Р° СЃРµСЂРІРµСЂР° РІ СЋРЅРёРєРѕРґРµ,
Response.url РІРѕР·РІСЂР°С‰Р°РµС‚ URL-Р°РґСЂРµСЃ, РїРѕСЃР»Рµ РїРµСЂРµРЅР°РїСЂР°РІР»РµРЅРёР№.
'''

# print(response.content)

# response.encoding = 'utf-8'
# print(response.text)


# from requests import get, utils
# encodings = utils.get_encoding_from_headers(response.headers)
# content = response.content.decode(encoding=encodings)
# print(content)

# text = response.text
# print(text)


# response = requests.get('https://api.github.com/')
# data = response.text
# print(data)
# print(type(response.text))


# data = response.json()
# print(data)
# print(type(data))

from pprint import pprint
# data = response.json()
# pprint(data, indent=10, sort_dicts=True)



# git_response = response.headers
# print(git_response)
# print(git_response['server'])


# РџРµСЂРµРґР°РµРј РїР°СЂР°РјРµС‚СЂС‹
# jph_data = requests.get('https://jsonplaceholder.typicode.com/comments', params=b'postId=2')
# pprint(jph_data.json())






# import requests
from decimal import *
from datetime import datetime
#
# getcontext().prec = 4
# response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
# pprint(response)
#
# def currency_rates(val):
#     val = val.upper()
#     response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
#
#     if val not in response:
#         return None
#
#     rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
#     day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
#     day, month, year = map(int, day_raw)
#     return f"{Decimal(rub.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"
#
#
# print(currency_rates('USD'))
# print(currency_rates('EUR'))
# print(currency_rates('eur'))

#
# import requests
# from pprint import pprint
# data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# pprint(data)
# cur = input()
# print(data['Valute'][cur]['Name'], data['Valute'][cur]['Value'], data['Date'])
