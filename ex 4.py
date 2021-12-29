import numpy as np

A = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]], float)

n = 15
q = 0.15

G = np.zeros([n, n], float)

for i in range(n):
    for j in range(n):
        nj = 0
        for k in range(n):
            nj += A[j][k]
        G[i][j] = q / n + (1 - q) * A[j][i] / nj

z = np.zeros(15, float)

for i in range(15):
    for k in range(15):
        z[i] = z[i] + G[k][i]
# ερώτημα 1
print("---------------")
print("z: " + str(z))

# ερώτημα 2

p = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], float)

# Μέθοδος των δυνάμεων
for i in range(n):
    p = np.dot(G, p)
    p = (1 /p[0]) * p

# Matrix Normalization
sum = 0
for i in range(n):
    sum += p[i]
for i in range(n):
    p[i] /= sum

print("p: ")
for i in range(n):
    print("p[" + str(i+1) + "]: " + str(p[i]))
print("-----------------------------------")


# Ερώτημα 3

A[13][9] = 0
A[1][13] = 1
A[2][13] = 1
A[9][13] = 1
A[10][13] = 1

G = np.zeros([n, n], float)

for i in range(n):
    for j in range(n):
        nj = 0
        for k in range(n):
            nj += A[j][k]
        G[i][j] = q / n + (1 - q) * A[j][i] / nj

p = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], float)

# Μέθοδος των δυνάμεων
for i in range(n):
    p = np.dot(G, p)
    p = (1 /p[0]) * p

# Matrix Normalization
sum = 0
for i in range(n):
    sum += p[i]
for i in range(n):
    p[i] /= sum

print("p (for for question 3): ")
for i in range(n):
    print("p[" + str(i+1) + "]: " + str(p[i]))
print("-----------------------------------")


# Ερώτημα 4α

q = 0.02
G = np.zeros([n, n], float)

for i in range(n):
    for j in range(n):
        nj = 0
        for k in range(n):
            nj += A[j][k]
        G[i][j] = q / n + (1 - q) * A[j][i] / nj

p = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], float)

# Μέθοδος των δυνάμεων
for i in range(n):
    p = np.dot(G, p)
    p = (1 /p[0]) * p

# Matrix Normalization
sum = 0
for i in range(n):
    sum += p[i]
for i in range(n):
    p[i] /= sum

print("p (with q = 0.02): ")
for i in range(n):
    print("p[" + str(i+1) + "]: " + str(p[i]))
print("-----------------------------------")


# Ερώτημα 4β

q = 0.6
G = np.zeros([n, n], float)

for i in range(n):
    for j in range(n):
        nj = 0
        for k in range(n):
            nj += A[j][k]
        G[i][j] = q / n + (1 - q) * A[j][i] / nj

p = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], float)

# Μέθοδος των δυνάμεων
for i in range(n):
    p = np.dot(G, p)
    p = (1 /p[0]) * p

# Matrix Normalization
sum = 0
for i in range(n):
    sum += p[i]
for i in range(n):
    p[i] /= sum

print("p (with q = 0.6): ")
for i in range(n):
    print("p[" + str(i+1) + "]: " + str(p[i]))
print("-----------------------------------")



# Ερώτημα 5

A[13][9] = 1
A[1][13] = 0
A[2][13] = 0
A[9][13] = 0
A[10][13] = 0

A[7][10] = 3
A[11][10] = 3

q = 0.15
G = np.zeros([n, n], float)

for i in range(n):
    for j in range(n):
        nj = 0
        for k in range(n):
            nj += A[j][k]
        G[i][j] = q / n + (1 - q) * A[j][i] / nj

p = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], float)

# Μέθοδος των δυνάμεων
for i in range(n):
    p = np.dot(G, p)
    p = (1 /p[0]) * p

# Matrix Normalization
sum = 0
for i in range(n):
    sum += p[i]
for i in range(n):
    p[i] /= sum

print("p (for question 5): ")
for i in range(n):
    print("p[" + str(i+1) + "]: " + str(p[i]))
print("-----------------------------------")

# Ερώτημα 6

for i in range(n):
    A[9][i] = 0
    A[i][9] = 0

G = np.zeros([n, n], float)

for i in range(n):
    if i == 9:
        continue
    for j in range(n):
        nj = 0
        if j == 9:
            continue
        for k in range(n):
            if k == 9:
                continue
            nj += A[j][k]
        G[i][j] = q / n + (1 - q) * A[j][i] / nj

p = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], float)

# Μέθοδος των δυνάμεων
for i in range(n):
    p = np.dot(G, p)
    p = (1 /p[0]) * p

# Matrix Normalization
sum = 0
for i in range(n):
    sum += p[i]
for i in range(n):
    p[i] /= sum

print("p (for question 6): ")
for i in range(n):
    print("p[" + str(i+1) + "]: " + str(p[i]))
