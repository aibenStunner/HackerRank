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

def poisson(a, b):
    print(round((pow(a, b) * math.exp(-a)) / factorial(b), 3))

if __name__ == '__main__':
    a = float(input())
    b = float(input())
    poisson(a,b)
