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


def gauss_seidel(a, b, x):
    n = len(a)
    xi = np.zeros(n, float)
    for i in range(n):
        sum1 = 0
        sum2 = 0
        for j in range(i-1):
            sum1 += a[i][j] * x[j][i+1]
        for j in range(i+1, n):
            sum2 += a[i][j] * x[j][i]
        xi[i] = round((b[i] - sum1 - sum2) / a[i][i], 4)
    x.append(xi)
'''
n = 10

a = np.zeros([n, n], float)
b = np.zeros(n, float)
x = np.zeros(n, float)
xn = np.zeros(n, float)     # for the warning

a = filla(a)
b = fillb(b)
for i in range(n):
    xn = gauss_seidel(a, b, x)
    infx = np.subtract(xn, x)
    inf = 0
    for k in range(n):
        inf += infx[k]
    if inf <= 0.00005:
        break
    x = xn

print(xn)
'''

n = 3

b = np.array([10, 10, 10], float)
a = np.array([[8, 1, 1],
             [1, 8, 1],
             [1, 1, 8]], float)
x = np.zeros([n,2], float)

for m in range(100):
    gauss_seidel(a, b, x)
    print(x)
    infx = np.subtract(x[m+1], x[m])
    inf = 0
    for k in range(n):
        inf += infx[k]
    if abs(inf) <= 0.00005:
        break
    x = xn




