import math
import numpy as np

def cholesky(matrix):
    n = len(matrix)
    lower = np.zeros([n, n], float)
    for i in range(n):
        for j in range(i + 1):
            sum1 = 0
            if j == i:
                for k in range(j):
                    sum1 += pow(lower[j][k], 2)
                lower[i][j] = float(math.sqrt(matrix[j][j] - sum1))
            elif i > j:
                for k in range(j):
                    sum1 += (lower[i][k] * lower[j][k])
                if lower[j][j] > 0:
                    lower[i][j] = float((matrix[i][j] - sum1) / lower[j][j])
            else:
                lower[i][j] = 0
    return lower


# Main

matrix = np.array([[2, 1, 1],
          [1, 2, 1],
          [1, 1, 2]], float)

print("A matrix:")
print(matrix)

l = cholesky(matrix)

print("L of A matrix:")
print(l)
