#!/usr/bin/python

class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        
    def to_string(self):
        return f"{self.x} {self.y}"

def dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid):
    visited = [[False for _ in range(c)] for _ in range(r)]
    
    # x, y
    # up:    x - 1, y
    # left:  x, y - 1
    # right: x, y + 1
    # down:  x + 1, y
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    
    stack = []
    explored = []  # nodes explored
    
    # start state
    stack.append(Node(pacman_r, pacman_c, None))
    visited[pacman_r][pacman_c] = True
    ref_goal = None
    
    while (len(stack) > 0):
        current = stack.pop()
        explored.append(current)
        
        if current.x == food_r and current.y == food_c:
            ref_goal = current
            break
        
        for i in range(4):
            new_x = current.x + dx[i]
            new_y = current.y + dy[i]
            if new_x < 0 or new_x >= r: continue
            if new_y < 0 or new_y >= c: continue
            if grid[new_x][new_y] == '%': continue
            if visited[new_x][new_y]: continue
            visited[new_x][new_y] = True
            stack.append(Node(new_x, new_y, current))
    
    print(len(explored))
    
    for node in explored:
        print(node.to_string())
    
    reverse_explored = []
    while ref_goal is not None:
        reverse_explored.append(ref_goal)
        ref_goal = ref_goal.parent
    
    print(len(reverse_explored) - 1)
    
    while len(reverse_explored) > 0:
        node = reverse_explored.pop()
        print(node.to_string())
    
pacman_r, pacman_c = [ int(i) for i in input().strip().split() ]
food_r, food_c = [ int(i) for i in input().strip().split() ]
r, c = [ int(i) for i in input().strip().split() ]

grid = []
for i in range(0, r):
    grid.append(input().strip())

dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)