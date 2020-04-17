import math
import os
import random
import re
import sys

def gd(a, b, n):
    prob = a/b

    print(round(pow(1-prob, n-1) * prob, 3))

if __name__ == '__main__':
    a = list(map(str, input().rstrip().split()))
    a, b = float(a[0]), float(a[1])
    n = int(input())
    gd(a, b, n)
