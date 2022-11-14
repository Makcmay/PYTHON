
'''2. Создайте программу для игры в ""Крестики-нолики"".'''    
# game_matrix = [[None, None, None], [None, None, None], [None, None, None]]
# game_is_on = True
# while game_is_on:
#     # Крестик - латинская буква X, нолик - латинская буква O 
#     # Ходы принимаются в формате [0][0] = "X" или [2][1] = "О"
#     move = input()
#     exec("game_matrix" + move)
#     for row in game_matrix:
#         print(row)
    
#     reference_matrix = [
#         game_matrix[0],
#         game_matrix[1],
#         game_matrix[2],
#         [i[0] for i in game_matrix],
#         [i[1] for i in game_matrix],
#         [i[2] for i in game_matrix],
#         [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]],
#         [game_matrix[0][2], game_matrix[1][1], game_matrix[2][0]]
#     ]
#     for item in reference_matrix:
#         result = list(set(item))
#         if len(result) == 1 and result[0] != None:
#             print("Game over!")
#             game_is_on = False
#             break


# board = ['', '', '', '', '', '', '', '', '']

# def print_state(state):
#     for i, c in enumerate(state):
#         if (i + 1) % 3 == 0:
#             print(f'{c}')
#         else:
#             print(f'{c}|', end=' ')

# print_state(board)

# winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# def get_winner(state, combinations):
#     for (x, y, z) in combinations:
#         if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == '0'):
#             return state[x]
#         return ''

# def play_game(board):
#     current_sign = 'X'
#     while (get_winner(board, winning_combinations) == ''):
#         index = int(input(f'Поставьте {current_sign} '))
#         board[index] = current_sign
#         print_state(board)
#         winner_sign = get_winner(board, winning_combinations)
#         if winner_sign != '':
#             print(f'У нас есть победитель: {winner_sign}')
#     current_sign = 'X' if current_sign == '0' else '0'

# play_game(board)