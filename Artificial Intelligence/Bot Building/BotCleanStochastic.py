#!/bin/python3

def nextMove(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return
    
    dirty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 'd']
    
    best_distance = float('inf')
    best_cell = None
    
    for (i, j) in dirty_cells:
        temp_distance = abs(posr - i) + abs(posc - j)
        if temp_distance < best_distance:
            best_distance = temp_distance
            best_cell = (i, j)
    
    if posr < best_cell[0]:
        print("DOWN")
    elif posr > best_cell[0]:
        print("UP")
    elif posc < best_cell[1]:
        print("RIGHT")
    else:
        print("LEFT")
    
    return

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)