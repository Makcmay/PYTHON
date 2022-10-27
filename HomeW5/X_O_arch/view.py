



def printField(game_field: list):
    print(f'{game_field[0]:^5}|{game_field[1]:^5}|{game_field[2]:^5}')
    print('-----------------')
    print(f'{game_field[3]:^5}|{game_field[4]:^5}|{game_field[5]:^5}')
    print('-----------------')
    print(f'{game_field[6]:^5}|{game_field[7]:^5}|{game_field[8]:^5}\n\n')


def playerTurn(game_field: list, mark) -> int: # -> int возвращает интеджер ход
    while True:
        move = int(input('Игрок делайте ваш ход: '))

        if 0 < move < 10 and game_field[move - 1].isdigit(): # проверяем есть ли нащ ход в поле, не занято ли, и его значение
            game_field[move - 1] = mark
            return move
        else:
            print('Эта клетка занята! Сделайте друной ход')

