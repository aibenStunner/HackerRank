#!/usr/bin/python

def displayPathtoPrincess(n, grid):
    # print all the moves here
    counter = 1
    for row in grid:
        if 'p' in row:
            px = row.index('p') + 1
            py = n - counter + 1
        if 'm' in row:
            mx = row.index('m') + 1
            my = n - counter + 1
        counter += 1

    dx = px - mx
    dy = py - my

    if dx > 0:
        for _ in range(dx):
            print('RIGHT')
    else:
        for i in range(abs(dx)):
            print('LEFT')

    if dy > 0:
        for _ in range(dy):
            print('UP')
    else:
        for _ in range(abs(dy)):
            print('DOWN')


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
