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


def gauss_seidel(a, b, iterations):
    n = len(a)
    x = np.zeros(n, float)
    # for loop for 3 times as to calculate x, y , z
    for k in range(iterations):
        for j in range(n):
            sum = 0
            for i in range(len(a[0])):
                sum += a[j][i]
            x[j] = (b[j] - sum + a[j][j] * x[j]) / a[j][j]
    # returning our updated solution
    return x


n = 10

a = np.zeros([n, n], float)
b = np.zeros(n, float)

a = filla(a)
b = fillb(b)
x = gauss_seidel(a, b, n)

print(x)
