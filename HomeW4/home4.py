'''30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл users_hobby.txt. 
Фрагмент файла с данными о пользователях (users.txt):
Иванов Иван Иванович
Петров Петр Петрович
Фрагмент файла с данными о хобби (hobby.txt):
скалолазание, охота
горные лыжи'''

string = input('Введите ФИО через пробел :')
string1 = input('Введите хобби через пробел :')

with open('users.txt', 'a', encoding='utf8') as f:
    f.write(string.title()+'\n')
with open('hobby.txt', 'a', encoding='utf8') as f1:
    f1.write(string1.capitalize()+'\n')

with open('users.txt', "r", encoding='utf8') as file:
    my_str = [line.strip() for line in file]
    print(my_str)
with open('hobby.txt', "r", encoding='utf8') as file:
    my_str1 = [line.strip() for line in file]
    print(my_str1)
    
users_hobby = dict(zip(my_str, my_str1))
print(users_hobby)

with open('users_hobby.txt', 'w', encoding='utf8') as out:
    for key, val in users_hobby.items():
        out.write('{}: {}\n'.format(key, val))


'''31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.'''

from mydef import inputNum

def factorN(number):
    fact =[]

    for i in range(1, number+1):
        if(number % i == 0):
            fact.append(i)
    return fact

print(factorN(inputNum('Введите число : ')))

'''32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.'''
from random import randint

def myList(num):
    
    arr_list = []
    
    for i in range(num):
        rand = randint(0, 6)
        arr_list.append(rand)
    print(arr_list)    
    return arr_list

def uniqList(my_list):

    uniq = [i for i in set(my_list) if my_list.count(i) == 1] #в новый лист мы отбираем только элементы из числа уникальных 
                                                              # при условии что они встречаются только один раз в основном списке'''  
    return uniq

print(uniqList(myList(inputNum('Введите динну листа :'))))


'''33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0'''

 
def write_file(st):
    with open('Task33.txt', 'a') as data:
        data.write(st + '\n')
 
def create_list(k):
    list = []
    for i in range(k + 1):
        list.append(randint(-10, 11))    
    return list
    
def create_str(sp):
    list = sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] > 0:
                    wr += '+'
                else:
                    wr+= ''
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i + 1] > 0:
                    wr += '+'
                else:
                    wr+= ''
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr
 
koef = create_list(inputNum('Введите натуральную степень k:'))
write_file(create_str(koef))


'''34. *Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0'''

import re
import itertools


file1 = 'Polynomial.txt'
file2 = 'Polynomial2.txt'
file_sum = 'Sum_polynomials.txt'

# Получение данных из файла

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

# Получение списка кортежей каждого (<коэффициент>, <степень>)

def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

def fold_pols(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

# Составление итогового многочлена

def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

pol1 = read_pol(file1)
pol2 = read_pol(file2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)

print(pol1)
print(pol2)
print(pol_sum)