import numpy as np

def filla(a):
    n = len(a)
    tmp = np.zeros([n, n], float)
    for i in range(n):
        for j in range(n):
            if i == j and i == 0:
                tmp[i][j] = 5
                tmp[i][j+1] = -2
            elif i == j and i == n-1:
                tmp[i][j] = 5
                tmp[i][j - 1] = -2
            elif i == j:
                tmp[i][j] = 5
                tmp[i][j - 1] = -2
                tmp[i][j + 1] = -2


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
    xi = x.copy()
    # for loop for 3 times as to calculate x, y , z
    for j in range(n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, z
        for i in range(n):
            if j != i:
                d -= a[j][i] * xi[i]
        # updating the value of our solution
        xi[j] = d / a[j][j]
    # returning our updated solution
    return xi


print("Δώσε το n:")
n = int(input())

a = np.zeros([n, n], float)
b = np.zeros(n, float)
x = np.zeros(n, float)
xn = np.zeros(n, float)  # for the warning

a = filla(a)
b = fillb(b)


def maxi(m):
    l = len(m)
    ma = m[0]
    for i in range(1, l):
        if m[i] > ma:
            ma = m[i]
    return ma


while True:
    xn = gauss_seidel(a, b, x)
    inf = abs(maxi(xn)) - abs(maxi(x))
    if abs(inf) <= 0.00005:
        break
    x = xn

print("Η λύση του συστήματος: " + str(xn))
