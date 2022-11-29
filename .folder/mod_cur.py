import requests
import datetime
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
    print(data)
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