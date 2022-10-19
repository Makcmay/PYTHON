
from random import randint, random

def inputNum(inputText):
    flag = False
    while not flag:
        try:
            number = int(input(f"{inputText}"))
            flag = True
        except ValueError:
            print("Это не число!")
    return number

def myList(num):
    
    arr_list = []
    
    for i in range(num):
        rand = randint(0, 10)
        arr_list.append(rand)
        
    return arr_list

def myFloatList(num):

    arr_list = []
    
    for i in range(num):
        rand = randint(0, 10) + round(random(), 2)
        arr_list.append(rand)
        
    return arr_list


'''1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
*Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

def findPosition(lst):
    sum = 0
    print(lst)
    for i in range(1, len(lst), 2):
        sum += lst[i]
    return sum

print(f'Сумма чисел на нечетных позициях = {findPosition(myList(inputNum("Введите число: ")))}')

'''2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

def findSumPosition(lst):
    sum_lst = []
    print(lst)
    length = int(len(lst))

    if length % 2 == 0:
        for i in range(0, (length // 2)):
            sum_lst.append(lst[i] * lst[length - i - 1])
    else:
        length = int(len(lst) + 1)
        for i in range(0, (length // 2)):
            sum_lst.append(lst[i] * lst[length - i - 2])
    return sum_lst
print(f'Произведение = {findSumPosition(myList(inputNum("Введите число: ")))}')

'''3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

def minMaxList(lst):

    print(lst)
    new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]

    print(f'Разница между максимальным и минимальным значением дробной части элементов = {max(new_lst) - min(new_lst)}')

minMaxList(myFloatList(inputNum("Введите число: ")))

'''4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*
- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

def numToTen(num):

    string = ""
    while num != 0:
        string = str(num % 2) + string
        num //=2
    print(f'В десятичной системе = {string} ')

numToTen(inputNum("Введите число для преобразовывания десятичного числа в двоичное :"))

'''5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
*Пример:*- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]'''


def fibonacciMod(n):
    if n >= 0:
       idx = range(n+1)
       x = [0,1]
       for k in idx[2:]:
           x.append(x[k-1] + x[k-2]) 
       return x[n]
    else:
       n=-(n-1)
       idx = range(n+1)
       x = [1,0]
       for k in idx[2:]:
           x.append(x[k-2] - x[k-1]) 
       x.reverse()
    return x[0]

n = inputNum('Enter namber : ')
fib_list = []

for i in range(-n, n+1):
   fib_list.append(fibonacciMod(i)) 
print(fib_list)