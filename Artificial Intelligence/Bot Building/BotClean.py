#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return

    dirty_cells = [(i, j) for i in range(len(board))
                   for j in range(len(board[0])) if board[i][j] == 'd']
    best_cell, best_distance = None, float('inf')

    for i, j in dirty_cells:
        temp_distance = abs(posr - i) + abs(posc - j)
        if temp_distance < best_distance:
            best_cell = (i, j)
            best_distance = temp_distance

    # find the best move
    if posr - best_cell[0] < 0:
        print("DOWN")
    elif posr - best_cell[0] > 0:
        print("UP")
    elif posc - best_cell[1] < 0:
        print("RIGHT")
    else:
        print("LEFT")

    return


# def next_move(posr, posc, board):
#     next_move = ""
#     mini_move = len(board[0])

#     for cell_in_h in range(len(board[posr])):
#         if(board[posr][cell_in_h] == "d"):
#             h_move = cell_in_h - posc

#             if(abs(h_move) < mini_move):
#                 mini_move = abs(h_move)
#                 if(h_move > 0):
#                     next_move = "RIGHT"

#                 if(h_move < 0):
#                     next_move = "LEFT"

#                 if(h_move == 0):
#                     next_move = "CLEAN"

#     if(next_move != ""):
#         print(next_move)
#     else:
#         print("DOWN")
#     return

# Tail starts here


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
