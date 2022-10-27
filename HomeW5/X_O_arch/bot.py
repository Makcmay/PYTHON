

def AIMove(field: list, enemy_field: list, win: list):
    if field[4].isdigit():
        return 4
    for pos in win:
