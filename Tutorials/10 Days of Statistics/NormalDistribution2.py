import math

def nd(m, s, x):
    return 0.5 + 0.5 * math.erf((x-m)/(s* 2**0.5))

def ans(m, s, x, y):
    print(round((1 - nd(m, s, x)) * 100, 2))
    print(round((1 - nd(m, s, y)) * 100, 2))
    print(round(nd(m, s, y) * 100, 2))

if __name__ == '__main__':
    a = list(map(str, input().rstrip().split()))
    m, s = float(a[0]), float(a[1])
    x = float(input())
    y = float(input())
    ans(m, s, x, y)
