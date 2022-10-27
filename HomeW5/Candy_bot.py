'''1. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) * Подумайте как наделить бота ""интеллектом""'''




from random import randint

def intDataCandy(name):  # ввод числа конфут с проверкой на количество и на символы
    flag = False
    while not flag:
        try:
            x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
            if 0 < x < 29:
                flag = True
            else:
                print(f"{name}, введите корректное количество конфет")
        except ValueError:
            print("Это не число!")           
    return x

def intCandy(int):
    flag = False
    while not flag:
        try:
            num = int(input("Введите количество конфет на столе: "))
            if  num > 55:
                flag = True
            else:
                print(f"{num} недостаточно для игры, минимальное количество конфет 56 ")
        except ValueError:
            print("Это не число!")           
    return num


def ternPrint(name, candy, counter, value): # выводмим данные после хода игрока
    print(f"Ходил {name}, он взял {candy}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = 'VERTER'
print(f'Привет {player1}, я Робот {player2}!')
value = intCandy(int)
player_turn = randint(0,2)              # очередность
if player_turn:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:           # пока общее число конфет больше 28 продолжаются ходы
    if player_turn:
        candy = intDataCandy(player1)
        counter1 += candy
        value -= candy
        player_turn = False
        ternPrint(player1, candy, counter1, value)
    else:
        candy = randint(1,28) # бот берет рандомное число от 1 до 28
        counter2 += candy
        value -= candy
        player_turn = True
        ternPrint(player2, candy, counter2, value)

if player_turn:   # когда общее число конфет стало меньше 28 определяем победителя
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")