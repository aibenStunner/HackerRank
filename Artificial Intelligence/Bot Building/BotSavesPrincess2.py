#

def nextMove(n,r,c,grid):
    counter = 1
    next_move = ""
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                px, py = i, j
                
    if px == r and py < c: next_move = 'LEFT'
    elif px == r and py > c: next_move = 'RIGHT'
    elif px < r: next_move = 'UP'
    else: next_move = 'DOWN'
    
    return next_move

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))