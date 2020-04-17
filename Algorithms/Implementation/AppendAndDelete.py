import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    _ = []
    for i in range(len(s)):
        try:
            if s[i] == t[i]:
                _.append(s[i])
            else:
                break
        except:
            break
 
    if not (t[len(_):] == "") and t[len(_):] in s:
        return "Yes"
    elif len(s) < len(t):
        return "No"
    elif k-(len(s) - len(_))-(len(t) - len(_)) >= 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')
    fptr.close()
