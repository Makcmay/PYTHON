
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




