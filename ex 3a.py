import numpy as np


def gauss(a, b):
    n = len(a)

    lower = np.zeros([n, n], float)
    upper = np.zeros([n, n], float)

    p = np.identity(n, float)
    for k in range(n):
        if a[k][k] == 0:
            for i in range(k, n):
                if a[i][k] != 0:
                    a[[k, i]] = a[[i, k]]
                    p[[k, i]] = p[[i, k]]
                    break

    # Decomposing matrix into Upper
    # and Lower triangular matrix
    for i in range(n):

        # Upper Triangular
        for k in range(i, n):

            # Summation of L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            # Evaluating U(i, k)
            upper[i][k] = a[i][k] - sum

        # Lower Triangular
        for k in range(i, n):
            if i == k:
                lower[i][i] = 1  # Diagonal as 1
            else:

                # Summation of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                # Evaluating L(k, i)
                lower[k][i] = float((a[k][i] - sum) / upper[i][i])

    print(p)
    print(lower)
    print(upper)


    # Gauss elimination for LY = Pb

    y = np.array(np.zeros(n, float))

    # P*b

    bn = np.array(np.matmul(p, b), float)

    for k in range(n - 1):
        for i in range(k + 1, n):
            fc = lower[i, k] / lower[k, k]
            for j in range(k, n):
                lower[i, j] = lower[i, j] - fc * lower[k, j]
            bn[i] = bn[i] - fc * bn[k]

    y[n - 1] = bn[n - 1] / lower[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        Sum = bn[i]
        for j in range(i + 1, n):
            Sum = Sum - lower[i, j] * y[j]
        y[i] = Sum / lower[i, i]

    # Gauss Elimination for UX = Y

    x = np.zeros(n, float)
    x[n - 1] = y[n - 1] / upper[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        Sum = y[i]
        for j in range(i + 1, n):
            Sum = Sum - upper[i, j] * x[j]
        x[i] = Sum / upper[i, i]

    return x


'''
a = np.array([[0, 1, 2, 1, 2],
              [1, 0, 0, 0, 1],
              [2, 1, 2, 1, 5],
              [1, 2, 4, 3, 6]], float)'''


a = np.array([[0, 2, -1, 1],
              [-1, 1, 2, -1],
              [2, -1, 2, 2],
              [1, 1, -1, 2]],
             float)

b = np.array([6, 3, 14, 8], float)

x = gauss(a, b)

print(x)