from random import randint, random, shuffle
import math

'''def myList(num):

    arr_list = []

    for i in range(num):
        rand = randint(0, 10)
        arr_list.append(rand)

    return arr_list'''

def myList(num):
    return [randint(0, 10) for i in range(num)]
# print(myList(6))

'''def mathNum(num):
    '''
'''Программа подсчета факториала и вывола его с листе'''
'''
    sum = []
    fact = 1
    
    for i in range(2, num + 2):
        sum.append(fact)
        fact *= i
    return sum '''

def mathNum(num):
    return [math.factorial(n) for n in range(num)]
# print(mathNum(6))


'''def sufleList(num):
    """
    Программа создает лист из рандомных чисел, длинна листа задается пользователем, далее лист перемешивается.
    """
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
    
    return arr_list'''

def sufleList(num):
    arr_list = [randint(0, 10) for i in range(num)]
    print(arr_list)
    shuffle(arr_list)
    return arr_list
# print(sufleList(6))


'''def findSumPosition(lst):
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
    return sum_lst'''

def findSumPosition(lst):     
    return ([lst[i] * lst[len(lst) - i - 1] for i in range(0, (len(lst) // 2))] if len(lst) % 2 == 0 else [lst[k] * lst[len(lst) - k - 1] for k in range(0, (len(lst) +1) // 2)])
    
# print(findSumPosition([1,2,3,4,5,6]))

'''def factorN(number):
    fact =[]

    for i in range(1, number+1):
        if(number % i == 0):
            fact.append(i)
    return fact'''

def factorN(number):
    return [i for i in range(1, number+1) if number % i == 0]
# print(factorN(45))