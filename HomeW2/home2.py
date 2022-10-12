# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


def inputFloatNum(inputNum):
    '''
    Программа для ввода дробного числа
    '''
    number = float(input(inputNum))
    return number

def countSum(num):
    '''
    Программа для подсчета суммы цифр в числе
    '''
    sum = 0
    for i in str(num):
        if  i != '.':
            sum = sum + int(i)
    return sum    

num = inputFloatNum('Enter namber :')
print(f'Сумма цифр числа = {countSum(num)}')

# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def inputNum(inputNum):
    '''
    Программа для ввода числа
    '''
    number = int(input(inputNum))
    return number

def mathNum(num):
    '''
    Программа подсчета факториала и вывола его с листе
    '''
    sum = []
    fact = 1
    
    for i in range(2, num + 2):
        sum.append(fact)
        fact *= i
    return sum 

num = inputNum('Enter namber : ')
print(f'Произведений чисел от 1 до {num} = {mathNum(num)}')



# 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}


def dictCount(num):
    '''
    программа для записи результата в словарь с округленрем числа
    '''
    return {i:  round(((1 + (1 / i)) ** i), 2) for i in range(1, num+1)}

num = inputNum('Enter namber : ')
print(f'Сумма чисел  N последовательности = {dictCount(num)}')

# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на введенных пользователем позициях.

from random import randint


def mathList(num):
    '''
    Программа создает массив из чисел внутри интревала от -N до N, 
    и считает призведение чисел на выбранных позициях.
    '''

    arr_list = []

    for i in range(num):

        rand = randint(- num, num)
        arr_list.append(rand)
    print(f'Список из {num} элементов {arr_list}')

    pos1 = inputNum('Enter index_1 : ')
    pos2 = inputNum('Enter index_2 : ')

    resalt = arr_list[pos1] * arr_list[pos2]
    return resalt

num = inputNum('Enter namber : ')
print(f'Произведение элементов на введенных позициях = {mathList(num)}')


# 18. *Реализуйте алгоритм перемешивания списка



def sufleList(num):
    '''
    Программа создает лист из рандомных чисел, длинна листа задается пользователем, далее лист перемешивается.
    '''
    arr_list = []
    temp = 0

    for i in range(num):

        rand = randint(0, 100)
        arr_list.append(rand)

    print(f'Список из {num} элементов {arr_list}')
    
    for n in range(0, len(arr_list)):

        randSufle = randint(0, len(arr_list) - 1)

        if arr_list[n] != arr_list[randSufle]:

            temp = arr_list[n]
            arr_list[n] = arr_list[randSufle]
            arr_list[randSufle] = temp
    
    return arr_list

num = inputNum('Enter namber : ')
print(f'Перемешанный список = {sufleList(num)}')

