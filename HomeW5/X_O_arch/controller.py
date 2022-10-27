import random
import model
import view
import bot


def printField():
    field = model.getField()
    view.printField(field)


def playerTurn():
    field = model.getField()
    mark = model.getMark() # обращение к переменной из файла модел
    move = view.playerTurn(field, mark)
    model.setPlayerMove(move)
    printField()
    player_field = model.getPlayerField() # print(model.player_field) проверка записи 1 в нужную позицию
    if model.winCondition(player_field):
        print('Победил игрок')
        return
    model.changeMark()
    enemyTurn()

def enemyTurn():
    field = model.getField()
    mark = model.getMark()
    # while True:
    #     move = random.randint(0,9)
    #     if (0 < move < 10) and field[move].isdigit(): # проверяем есть ли ход для бота в поле, не занято ли, и его значение
    #         field[move] = mark
    #         break
    enemy_field = model.getEnemyField()
    move = bot.AIMove(field, enemy_field, model.win)
    field[move] = mark
    model.setPlayerMove(move)
    printField()
    enemy_field = model.getEnemyField()# print(model.player_field) проверка записи 1 в нужную позицию
    if model.winCondition(enemy_field):
        print('Победил bot')
        return
    model.changeMark()
    playerTurn()
