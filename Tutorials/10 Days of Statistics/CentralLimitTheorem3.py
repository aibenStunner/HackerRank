import math

def ans(m, s, x, z):
    s_sample = s / (x**0.5)

    print(round(m - s_sample*z,2))
    print(round(m + s_sample*z,2))
    
if __name__ == '__main__':
    x = float(input())
    m = float(input())
    s = float(input())
    d = float(input())
    z = float(input())
    ans(m, s, x, z)
