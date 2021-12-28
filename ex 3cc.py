import numpy as np


def filla(a):
    n = len(a)
    tmp = np.zeros([n, n], float)
    for i in range(n):
        for j in range(n):
            if i == j:
                tmp[i][j] = 5
            else:
                tmp[i][j] = -2
    return tmp


def fillb(b):
    n = len(b)
    tmp = np.zeros(n, float)
    for i in range(n):
        if i == 0 or i == n - 1:
            tmp[i] = 3
        else:
            tmp[i] = 1
    return tmp


def gauss_seidel(a, b):
    n = len(a)
    x = np.zeros(n, float)
    for i in range(n):
        sum1 = 0
        sum2 = 0
        for j in range(i-1):
            sum1 += a[i][j] * x[j]
        for j in range(i+1, n):
            sum2 += a[i][j] * x[j]
        x[i] =  (b[i] - sum1 - sum2) / a[i][i]
    # returning our updated solution
    return x


n = 10

a = np.zeros([n, n], float)
b = np.zeros(n, float)

a = filla(a)
b = fillb(b)
for i in range(n):
    x = gauss_seidel(a, b)
    print(x)
