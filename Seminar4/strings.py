'''
Метод .split()
Первая задача: дан адрес “https://geekbrains.ru/teacher/lessons/79615”. Нужно его распарсить — придать определённую структуру, понять, что есть что.
Обычно при парсинге начинают с разделения исходной строки на части по определённой схеме. В нашем примере очевидно, что надо делить по слешу:
url = 'https://geekbrains.ru/teacher/lessons/79615'
url_parts = url.split('/')
print(url_parts)
# ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', '79615']
'''
# url = 'https://geekbrains.ru/teacher/lessons/79615'
# url_parts = url.split('/') # по дефолту в сплит это пробел
# print(url_parts)
# # # ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', '79615']

# url = 'https://geekbrains.ru/teacher/lessons/79615'
# _t_protocol, _, domain, *resource_address = url.split('/')  # нижнее подчеркивание это пропуск элемента
# t_protocol = _t_protocol[:-1]                               # клвдем в протокол https первый элемент
# print(t_protocol, resource_address)


'''
.join()
!!! он корректно склеивает последовательности, состоящие только из строк
'''
# raw_url = ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', '79615']
# print('/'.join(raw_url))

# url = '/'.join(raw_url) # равносильно
# print(url)


# raw_url_2 = ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', 79615] # TypeError: sequence item 5: expected str instance, int found нужно число перевести в строку''
# url_2 = '/'.join(raw_url_2)
# print(url_2)

'''
.upper() и .lower() — вся строка переводится в верхний или нижний регистр:
'''
# msg = 'Товаров в корзине: 5'
# print(msg.upper())
# #
# print(msg.lower())

# print(msg.upper())  # ТОВАРОВ В КОРЗИНЕ: 5
# print(msg.lower())  # товаров в корзине: 5

'''
Правим регистр: методы .title() и .capitalize() — либо у всех слов первая буква становится заглавной, либо только первая:
'''

# msg = 'тОВАров в коРЗИНЕ: 5. стоимость: 4789,5 руб.'


# print(msg.title())  # Товаров В Корзине: 5. Стоимость: 4789,5 Руб. все первые заглавные
# print(msg.capitalize())  # Товаров в корзине: 5. стоимость: 4789,5 руб. только первая буква строки


# print(msg[::-2]) # срез строки выводит каждый второй знак с конца


'''
Реверс строк
Для реверса строк используем срез с шагом -1:
'''

# msg = 'а роза упала на лапу Азора'
# #
# #
# #
# print(msg[::-1]) # реверс строки через срез с шагом -1





# print(msg[::-1])  # арозА упал ан алапу азор а
