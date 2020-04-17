import math

def nd(m, s, x):
    return 0.5 + 0.5 * math.erf((x-m)/(s* 2**0.5))

def ans(m, s, x, y1, y2):
    print(round(nd(m, s, x), 3))
    print(round(nd(m, s, y2) - nd(m, s, y1), 3))

if __name__ == '__main__':
    a = list(map(str, input().rstrip().split()))
    m, s = float(a[0]), float(a[1])
    x = float(input())
    a = list(map(str, input().rstrip().split()))
    y1, y2 = float(a[0]), float(a[1])
    ans(m, s, x, y1, y2)
