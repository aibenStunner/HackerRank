import math

def nd(m, s, x):
    Z = (x - m)/s
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

def ans(m, s, x, n):
    print(round(nd(m*n, s*math.sqrt(n), x), 4))
    
if __name__ == '__main__':
    x = float(input())
    n = float(input())
    m = float(input())
    s = float(input())
    ans(m, s, x, n)
