# print('Hellow world')

# # Тип данных int-целые float-плавающая запятая boolean - логические str-строки list-массивы none

# value = None #для обьявления переменной заранее
# #print(type(value))
# a = 123
# b = 1.23
# #print(type(a)) # type показывает тип переменной
# #print(type(b))
# value = 12334
# #print(type(value))
# s = 'hellow world' # ввод строки можно добавить двой ные ковычки "hellow 'world" \n переход на новую строку "hellow \n world" \" исключение знака
# print(s)
# print(a, '-' ,b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s)) # можно определить порядок вывода расставив индексы 0, 1, 2, в соответсвующие позиции ('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)

# list = ['1', '2', '3', 'hellow', 1,2,3,4, True] #можно миксовать типы данных, строки, числа, логические
# print(list)

# list = ['1', '2', '3',]
# col = ['hellow', 1,2,3,4, True] #пробедл может сломать программу
# print(list)
# print(col)

# print('Введите a'); 
# a = int(input()) # int(input()) позволит складывать целочисленные значения  float(input())дробные
# print('Введите b');
# b = int(input())
# print(a, ' + ', b, ' = ', a+b) #выведе сумму строк
# # print(f'{a} {b}')
# # print('{} {}'.format(a, b))
# a = int(input('Введите а: ')) # 11
# b = int(input('Введите b: ')) # 22
# c = 33
# print('{} + {} = {}'.format(a, b, c)) 

# a = int(input('Введите \nа: '))
# b = int(input('Введите \nb: '))
# c = a + b
# print('{} + {} = {}'.format(a, b, c))

# Арифметические операции
# Важно и нужно, без них вы не напишете ни одной
# программы
# Если помните математику – проблем не будет
# +, -, *, /, %, //,**
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, - ( ) Скобки меняют приоритет

# a = 1.3 #плюс или минус перед числом это унарный плюс или минус a = +123 b = -345
# b = 3
# c = a * b # один знак деления / будет в дробных // знака будет в целых % отаток от деления ** возведение в степень
# print(c)

# a = 1.332322222
# b = 3
# c = round(a * b, 3) # итог 3.9000000000000004 для округдения используем round (a*b, 3) через запятую количестро символов
# print(c)

# a = 3
# a = a + 5 # a +=5 аналог
# print(a)

# Логические операции
# >, >=, <, <=, ==, != 

# not, and, or – не путать с &, |,^

# Кое-что ещё: is, is not, in, not in

# a = 1 == 2 #a = 1 < 4 and 5 > 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1,2] # в списке сравнение по элементно
# b = [1,2]
# print(a == b)

# a = 1<3<5<10 # можно использовать четверные условия
# print(a)

# f = 1<3 or 5>10 # можно использовать условия или
# print(f)

# f = [1,2,3,4]
# # print(2 in f) # проверяем наличие 2 в массиве print(not 2 in f) проверить отсутсвие 

# is_odd = not f[0] % # is_odd = f[0] %2 == 0 равносильно
# print(is_odd)

# Управляющие конструкции: if, if-else  Отступы важны!
# if condition :
 # operator 1
 # operator 2
 # ...
 # operator n
# else:
 # operator n + 1
 # operator n + 2
 # ...
 # operator n + m


# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)    

# Управляющие конструкции: if, if-else
# if condition1:
#  # operator
# elif condition2:
#  # operator
# elif condition3:
#  # operator
# else:
#  # operator

# Управляющие конструкции: if, if-else
# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

# Управляющие конструкции: while

# while condition:
#  operator 1
#  operator 2
#  . . .
#  operator n

# original = 23 # переворот числа, инверсия
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Управляющие конструкции: while-else
# while condition:
#  # operator 1
#  # operator 2
#  # . . .
#  # operator n
# else:
#  # operator n + 1
#  # operator n + 2
#  # . . .
#  # operator n + m


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original) #посмотреть выполнение цикла
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции: for
# for i in enumeration:
#  # operator 1
#  # operator 2
#  # . . .
#  # operator n

# Когда мы знаем, что хотим
# list = [1, -2, 3, 14, 5]
# for i in list: # можно писать данные вместо list
#     print(i**2)

# ранджирование,

# list = range(10) # вывод диапозона от 0 до 9
# for i in list: # можно писать данные вместо list
#     print(i)


# for i in range(1, 5): # вывод диапозона от 0 до 4 
#     print(i)

# for i in range(1, 10, 2): # третий аргумент это приращение (прибавление к первому)
#     print(i)

# for i in 'qweerrty': # вывод строки 
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# Немного о строках
text = 'съешь ещё этих мягких французских булок'
# help(text.islower) # описание функции
# print(len(text)) # 39 , определить количесво символов
# print('ещё' in text) # True, орпределить наличие в строке
# print(text.isdigit()) # False, проверяем строка цифр ли это, Строка является строкой цифр, если все символы в строке являются цифрами и существует хотя бы один символ в строке.
# print(text.islower()) # True, Строка является строчной, если все символы в строке в нижнем регистре и в строке есть хотя бы один символ в регистре.
# print(text.replace('ещё','ЕЩЁ')) # замена
# for c in text:
#     print(c) # выод всех символов строки 


# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов
# Списки: введение

# numbers = [1, 2, 3, 4, 5]
# print(numbers)               # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))

# numbers = list(ran) # изменение типа рандж в тип лист
# print(type(numbers))

# print(numbers)               # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len') # определили длинну или кол-во символов в листе намберс
# print(numbers)              # [10, 2, 3, 4, 5]
# for i in numbers:       
#     i *= 2                  #изменение значения текущей переменно, начальный список не меняется
#     print(i)                   # [20, 4, 6, 8, 10]
# print(numbers)                 # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors)
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент
# print(colors)

# # Функции
# # Это фрагмент программы, используемый многократно
# def function_name(x):
# # body line 1
# # . . .
# # body line n
#  # optional return


# Функции

# def f(x):
#     return x**2

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 1
print(f(arg))
print(type(f(arg)))
# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType