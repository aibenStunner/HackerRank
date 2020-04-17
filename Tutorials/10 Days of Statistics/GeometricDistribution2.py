import math
import os
import random
import re
import sys

def gd(a, b, n):
    prob = a/b
    ans = 0
    for i in range(1, n+1):
        ans += pow(1-prob, i-1) * prob
    print(round(ans, 3))

if __name__ == '__main__':
    a = list(map(str, input().rstrip().split()))
    a, b = float(a[0]), float(a[1])
    n = int(input())
    gd(a, b, n)
