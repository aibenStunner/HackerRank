import math
import os
import random
import re
import sys

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x-1)

def bino(n, x, p):
    comb = factorial(n) / (factorial(n-x) * factorial(x))
    return comb * pow(p, x) * pow((1-p), n-x)

def bd(a, b):
    prob = a / (a+b)
    ans = 0

    for i in range(3, 7):
        ans += bino(6, i, prob)
    return round(ans, 3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(str, input().rstrip().split()))
    a, b = float(a[0]), float(a[1])
    QQQ = bd(a,b)


    fptr.write('\n'.join(map(str, QQQ)))
    fptr.close()
