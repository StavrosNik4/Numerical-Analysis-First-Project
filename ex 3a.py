import numpy as np
from numpy import zeros


def gauss(a, b):
    n = len(b)
    p = np.identity(n)
    for k in range(n):
        if a[k][k] == 0:
            for i in range(k, n):
                if a[i][k] != 0:
                    a[[k, i]] = a[[i, k]]
                    p[[k, i]] = p[[i, k]]
                    break

    # LU decomposition

    lower = np.array([[0 for z in range(n)]
                      for y in range(n)], float)
    upper = np.array([[0 for x in range(n)]
                      for y in range(n)], float)
    # Decomposing matrix into Upper
    # and Lower triangular matrix
    for i in range(n):
        # Upper Triangular
        for k in range(n):

            # Summation of L(i, j) * U(j, k)
            su = 0
            for j in range(i):
                su += float(lower[i][j] * upper[j][k])

            # Evaluating U(i, k)
            upper[i][k] = float(a[i][k] - su)

        flag = False
        if a[i][i] == 0:
            for k in range(i, n):
                if a[k][i] != 0:
                    a[[k, i]] = a[[i, k]]
                    p[[k, i]] = p[[i, k]]
                    flag = True

        # Lower Triangular
        for k in range(i, n):
            if i == k:
                lower[i][i] = 1  # Diagonal as 1
            else:
                # Summation of L(k, j) * U(j, i)
                su = 0
                for j in range(i):
                    su += (lower[k][j] * upper[j][i])

                # Evaluating L(k, i)
                lower[k][i] = float((a[k][i] - su) / upper[i][i])

        if flag and i < n - 2:
            temp = lower.T[i]
            temp[i + 1], temp[i + 2] = temp[i + 2], temp[i + 1]
            lower[i] = temp

    print(lower)
    print(upper)
    # Gauss elimination for LY = B

    y = zeros(n, float)

    for k in range(n - 1):
        for i in range(k + 1, n):
            fc = lower[i, k] / lower[k, k]
            for j in range(k, n):
                lower[i, j] = lower[i, j] - fc * lower[k, j]
            b[i] = b[i] - fc * b[k]

    y[n - 1] = b[n - 1] / lower[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        Sum = b[i]
        for j in range(i + 1, n):
            Sum = Sum - lower[i, j] * y[j]
        y[i] = Sum / lower[i, i]

    # Gauss Elimination for UX = Y

    x = zeros(n, float)
    x[n - 1] = y[n - 1] / upper[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        Sum = y[i]
        for j in range(i + 1, n):
            Sum = Sum - upper[i, j] * x[j]
        x[i] = Sum / upper[i, i]

    return x


'''
a = np.array([[1, 2, -1, 1],
              [-1, 1, 2, -1],
              [2, -1, 2, 2],
              [1, 1, -1, 2]], float)'''

a = np.array([[1, 6, 2],
              [2, 12, 5],
              [-1, -3, -1]], float)

b = np.array([6, 3, 14], float)

x = gauss(a, b)

# gauss(a, b)

print(x)
