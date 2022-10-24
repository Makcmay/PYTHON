def f(x):
    x**2

g = f
print(f(1))
print(g(1))


def f(x):
    return x**2

g = f

print(type(f))
print(type(g))

print(f(4))
print(g(4))

def calc1(x):
    return x + 10
print(calc1(10))

def calc2(x):
    return x*10
print(calc2(10))

def math(op, x): # ор - это функция, х переменная
    print(op(x))

math(calc2, 10) # в качестве аргемента в math мы передаем функцию, которая выполнит действие с переменной

def sum(x, y):
    return x+y
f = sum
f = lambda q, w: q+w # аналог записи sum

sum = lambda x, y: x+y

def mult(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

# calc(sum, 4, 5)
calc(lambda x, y: x+y, 4, 5)


List Comprehension
[exp for item in iterable]
[exp for item in iterable (if conditional)]
[exp <if conditional> for item in iterable (if conditional)]

list=[]

for i in range(1, 101):
    # if(i%2 == 0):
        list.append(i)
print(list)

def f(x):
    return x**3

# list = [i for i in range(1, 21) if i%2 == 0]
# list = [(i, i) for i in range(1, 21) if i%2 == 0] #добавляем картеж

# list = [f(i) for i in range(1, 21) if i%2 == 0] # берем только четные и возводим в куб

list = [(i, f(i)) for i in range(1, 21) if i%2 == 0] # берем только четные и возводим в куб и добавляем кортеж с номером i

print(list)

m = '1 2 3 5 8 15 23 38'
path = 'C:\PYTHON\Lec\m.txt'
f = open(path, 'r')
data = f.read() + ' '                # считали информацию из файла и добавили пробел
f.close()
numbers = []
while data != '':                # запускаем цикл до пробела, пока сторка не пусатя
    space_pos = data.index(' ') #проходим по списку до первого пробела и узнаем его индекс
    numbers.append(int(data[:space_pos])) # превращаем все что до пробела в число и добавляем в список
    data = data[space_pos+1:]            # обнавляем строку с учетом того что мы добавили(отрезаем проверенную часть)
out = []                                # создаем новый список куда будем класть итог
for e in numbers:                        # проходим по исходному
    if not e % 2:                        # проверка
        out.append((e,e **2))            # создаем кортеж номер и квадрат
print(out)

def select(f, col): # функция в качестве первого элемента принимает функцию которая отвечает за логику обработки данных, в качестве второго аргумента список данных
    return [f(x) for x in col]

def where(f, col):
    return[x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x %2, res)  # lambda  временная функция, принимает аргумент и что-то с ним делает
res = select(lambda x: (x, x**2), res)
print(res)

li = [x for x in range(1, 20)]
print(li)
li = list(map(lambda x: x+10, li)) #<map object at 0x000001A2E816B6A0> необходимо заврнуть в лист
# добавим 10 к каждому элементу списка 
print(li)

data = list(map(int, input().split())) #преобразование строки в лист 
print(data)

data = list(map(int, '1 2 3 5'.split())) #распарсили строку на числа

for e in data: оборачивание в лист позволяет работать с сохранеными данными
    print(e)

print('--')

for e in data:
    print(e)



def where(f, col):
    return[x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x %2, res)  # lambda  временная функция, принимает аргумент и что-то с ним делает
res = list(map(lambda x: (x, x**2), res))
print(res)

data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data))  # not x%2 = x%2 ==0
print(res)

используем filter вместо where

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x %2, res)  # lambda  временная функция, принимает аргумент и что-то с ним делает
res = list(map(lambda x: (x, x**2), res))
print(res)

users = ['u1', 'u2', 'u3', 'u4', 'u5',]
ids = [1, 3, 5, 8]
salsry = [111, 222, 333] # будет проходить по нименьшему списку

data = list(zip(users, ids, salsry))
print(data)

users = ['u1', 'u2', 'u3', 'u4', 'u5',]
ids = [1, 3, 5, 8]
salsry = [111, 222, 333] # будет проходить по нименьшему списку

data = list(enumerate(users))
print(data)