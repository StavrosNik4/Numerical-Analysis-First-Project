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
    # for loop for 3 times as to calculate x, y , z
    for j in range(n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, z
        for i in range(n):
            if j != i:
                d -= a[j][i] * x[i]
        # updating the value of our solution
        x[j] = d / a[j][j]
    # returning our updated solution
    return x


n = 10

a = np.zeros([n, n], float)
b = np.zeros(n, float)

a = filla(a)
b = fillb(b)
x = np.zeros(n, float)

print(a)
print(b)
print(x)

for i in range(n):
    x = gauss_seidel(a, b, x)
    print(np.around(x, 4))
