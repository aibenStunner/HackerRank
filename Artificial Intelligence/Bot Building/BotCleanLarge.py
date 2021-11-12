

def next_move(posx, posy, dimx, dimy, board):
    if board[posx][posy] == 'd': 
        print("CLEAN")
        return
    
    dirty_cells = [(i, j) for i in range(dimx) for j in range(dimy) if board[i][j] == 'd']
    best_cell, best_distance = None, float('inf')
    
    for (i, j) in dirty_cells:
        temp_distance = abs(posx - i) + abs(posy - j)
        if temp_distance < best_distance:
            best_distance = temp_distance
            best_cell = (i, j)
    
    if posx < best_cell[0]:
        print("DOWN")
    elif posx > best_cell[0]:
        print("UP")
    elif posy < best_cell[1]:
        print("RIGHT")
    else:
        print("LEFT")
    return
    
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)