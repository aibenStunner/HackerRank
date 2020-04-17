def poisson(x, y):
    print(round(160+40*(x + x**2), 3))
    print(round(128+40*(y + y**2), 3)) 


if __name__ == '__main__':
    a = list(map(str, input().rstrip().split()))
    x, y = float(a[0]), float(a[1])
    poisson(x, y)
