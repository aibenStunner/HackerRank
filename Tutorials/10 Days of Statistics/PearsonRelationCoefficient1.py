import math

def sd(arr, n):
    u = mean(arr)
    sd = 0
    for x in arr:
        sd += (x-u)**2
    return float(math.sqrt(sd/n))

def mean(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

    return float(sum/len(arr))

def pcc(X, Y, n):
    sd_x, sd_y = sd(X, n), sd(Y, n)
    sigmaFunc = sum([(X[i] - sum(X) / n) * (Y[i] - sum(Y) / n) for i in range(n)])
    print(round((sigmaFunc / (sd_x * sd_y) / n), 3))

if __name__ == "__main__":
    n = int(input())
    X = list(map(float, input().rstrip().split()))
    Y = list(map(float, input().rstrip().split()))    
    pcc(X, Y, n)
