#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    t = s.split(':')
    if 'PM' in s:
        if t[0] == '12' or t[0] == '00':
            sec = t[2].split('PM')
            Time = t[0]+':'+t[1]+':'+sec[0]
        else:
            t[0] = str(int(t[0])+12%24)
            sec = t[2].split('PM')
            Time = t[0]+':'+t[1]+':'+sec[0]
        return Time
    else:
        if t[0] == '12':
            t[0] = '00'
        sec = t[2].split('AM')
        Time = t[0]+':'+t[1]+':'+sec[0]
        return Time

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
