#!/usr/bin/python3
import random


def next_move(posx, posy, board):
    if board[posx][posy] == 'd':
        print("CLEAN")
        return

    dirty_adjacent_cells = [(i, j) for i in range(len(board))
                            for j in range(len(board[0])) if board[i][j] == 'd']

    for (i, j) in dirty_adjacent_cells:
        if posx < i:
            print("DOWN")
        elif posx > i:
            print("UP")
        elif posy < j:
            print("RIGHT")
        else:
            print("LEFT")
        return

    if dirty_adjacent_cells == []:
        observable_cells = [(i, j) for i in range(len(board))
                            for j in range(len(board[0])) if board[i][j] == 'o']

        random.shuffle(observable_cells)

        for (i, j) in observable_cells:
            if posx < i:
                print("DOWN")
            elif posx > i:
                print("UP")
            elif posy < j:
                print("RIGHT")
            else:
                print("LEFT")
            return


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
