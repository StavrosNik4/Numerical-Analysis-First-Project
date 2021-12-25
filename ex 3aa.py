import numpy as np
from numpy import zeros

def gauss(a, b):
    n = len(b)
    p = np.identity(n, float)
    x = zeros(n, float)
    # row exchange
    for k in range(n):
        if a[k][k] == 0:
            for i in range(k, n):
                if a[i][k] != 0:
                    a[[k, i]] = a[[i, k]]
                    p[[k, i]] = p[[i, k]]
                    break

    # LU
    lower = np.identity(n, float)

    for k in range(n-1):
        for i in range(k+1, n):
            pivot = a[k, k]
            if pivot != 0:
                fc = a[i, k] / a[k, k]
            else:
                


            fc = a[i, k] / a[k, k]

            for j in range(k, n):
                a[i, j] = a[i, j] - fc * a[k, j]
            #b[i] = b[i] - fc * b[k]
            lower[i, k] = fc

    print(lower)
    print(a)

'''            if found:
                print('----')
                lower[i], lower[j] = lower[j], lower[i]
                lower.T[i], lower.T[j] = lower.T[j], lower.T[i] '''




a = np.array([[0, 1, 2, 1, 2],
              [1, 0, 0, 0, 1],
              [2, 1, 2, 1, 5],
              [1, 2, 4, 3, 6]], float)

b = np.array([1, 2, 3, 4], float)

#x = gauss(a, b)

gauss(a, b)