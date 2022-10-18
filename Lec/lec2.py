# with open('file.txt', 'a') as data: # данная конструкция автоматически закрывает работу с файлом
#   data.write('line 1141\n')
#   data.write('line 3322\n')

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # a дозаписывает данные к уже сущетвующим, w перезаписывает
# # data.writelines(colors) # разделителей не будет
# data.write('LINE 12\n')
# data.write('LINE 12ww\n')
# data.close()

# exit()

# path = 'file.txt' # вывод на экран, все данные хранятся как строки, нужно переводить а инт
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import lec # название файла

# print(lec.f(1)) # название файла, название метода, пременная

# import lec as l # название файла превращаем в L

# print(l.f(2)) # название файла, название метода, пременная

# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5))        # !!!!! можно перемножать строку на число
# print(new_string('!'))           # TypeError missing 1 required ... не указано число

# def new_string(symbol, count = 3):   # можно установить значение по умолчанию
#     return symbol * count
# print(new_string('!', 5))           # !!!!!
# print(new_string('!'))              # !!!
# print(new_string(4))                # 12       

# def concatenatio(*params):   # для работы с раздичными параметрами ставим зведочку
#     res: str = ""            # если хотим работать с цифрами нужно поставить int = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(concatenatio(1, 2, 3, 4)) # TypeError: ...


# def fib(n):
#     if n in [1, 2]: # если 1 или 2 возвращаем 1
#         return 1
#     else:
#         return fib(n-1) + fib(n-2) # 1 в противном случау вызываем рекурсивную функцию
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)  # 1 1 2 3 5 8 13 21 34


# Кортеж – это неизменяемый “список”
# t = ()
# print(type(t))  # tuple
# t = (1,)
# print(type(t))  # tuple
# t = (1)
# print(type(t))  # int
# t = (28, 9, 1990)
# print(type(t))  # tuple
# colors = ['red', 'green', 'blue']
# print(colors)   # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)        # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
#     t[0] = 'black' # TypeError: 'tuple' object does not support item assignment

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# # Словари
# dictionary = {} # пустой словарь
# dictionary = \
# {
# 'up': '↑',
# 'left': '←',
# 'down': '↓',
# 'right': '→'
# }
# print(dictionary['up'])
# dictionary['up'] = 'up' #замена значения
# print(dictionary['up'])

# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k) # пролучим все значения

# for e in dictionary.values():
#     print(e) # пролучим все ключи

# for v in dictionary:
#     print(dictionary[v]) # пролучим все ключи

# # Множества
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # при добавдении существующего, ничего не добавиться
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray') # добавление
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # удаление
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red' если нет - то ошибка
# colors.discard('red') # ok отсутсвие ошибки при отсутвии элемента
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } очистить множество
# print(colors) # set()

# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# Множества
# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# # Множества
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                # c = {1, 2, 3, 5, 8} копирование
# u = a.union(b)              # u = {1, 2, 3, 5, 8, 13, 21} объяденение
# i = a.intersection(b)       # i = {8, 2, 5} пересечение
# dl = a.difference(b)        # dl = {1, 3}
# dr = b.difference(a)        # dr = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}

# s = frozenset(a) # замороженное множество

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)

# for e in list2:
#     print(e)    

# list1[0] = 123  # измениться и в первом и во втором
# list2[1] = 333
# for e in list1:
#     print(e)

# for e in list2:
#     print(e)

# list1 = [1, 2, 3, 4, 5]

# print(list1.pop()) # метод уберает последний элемент
# print(len(list1))
# print(list1)
# print(list1.pop())
# print(len(list1))
# print(list1)

# list1 = [1, 2, 3, 4, 5]
# print(list1.pop(2)) # удалит третий элемент

# list1 = [1, 2, 3, 4, 5]
# print(list1.insert(2, 11)) # вставить на позицию третьего элемента 11

# list1 = [1, 2, 3, 4, 5]
# print(list1.append(11)) # вставить элемент в конец 