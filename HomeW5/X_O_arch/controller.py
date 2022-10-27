import random
import model
import view
import bot

def intro():
    name = view.playerName()
    model.setName(name)

def printField():
    field = model.getField()
    view.printField(field)


def playerTurn():
    field = model.getField()
    mark = model.getMark() # обращение к переменной из файла модел
    name = model.getName()
    move = view.playerTurn(field, mark, name)
    model.setPlayerMove(move)
    printField()
    player_field = model.getPlayerField() # print(model.player_field) проверка записи 1 в нужную позицию
    if model.winCondition(player_field):
        print(f'Победил {name}')
        return
    model.changeMark()
    enemyTurn()

def enemyTurn():
    field = model.getField()
    mark = model.getMark()
    enemy_field = model.getEnemyField()
    player_field = model.getPlayerField()
    move = bot.AIMove(field, player_field, enemy_field, model.win)
    field[move] = mark
    model.setEnemyMove(move)
    printField()
    enemy_field = model.getEnemyField()  # print(model.player_field) проверка записи 1 в нужную позицию
    if model.winCondition(enemy_field):
        print('Победил bot')
        return
    model.changeMark()
    playerTurn()
