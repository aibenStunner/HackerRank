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

def bd(prob, n):
    ans = 0
    for i in range(3):
        ans += bino(n, i, prob/100)
    print(round(ans, 3))
    ans = 0
    for i in range(2):
        ans += bino(n, i, prob/100)
    print(round(1-ans, 3))

if __name__ == '__main__':
    a = list(map(str, input().rstrip().split()))
    prob, n = float(a[0]), float(a[1])
    bd(prob, n)
