# Άσκηση 2 Μέθοδος Τέμνουσας

import sympy as sp

z = sp.Symbol('z')

f = 54 * z ** 6 + 45 * z ** 5 - 102 * z ** 4 - 69 * z ** 3 + 35 * z ** 2 + 16 * z - 4
f = sp.lambdify('z', f)

eps = 10**(-5)

print("Δώσε x0:")
x0 = float(input())
print("Δώσε x1:")
x1 = float(input())
print("Δώσε x2:")
x2 = float(input())

x = [x0, x1, x2]
n = 0
rootFound = False

while abs(x[n+1] - x[n]) >= eps:
    q = f(x[n]) / f(x[n+1])
    r = f(x[n+2]) / f(x[n+1])
    s = f(x[n+2]) / f(x[n])
    c = x[n+2] - (r * (r-q) * (x[n+2] - x[n+1]) + (1-r) * s * (x[n+2] - x[n])) / ((q-1) * (r-1) * (s-1))
    x.append(c)
    print("n: " + str(n+1) + " x: " + str("{:.5f}".format(x[n + 1])) + ", f(x): " + str(
        "{:.5f}".format(f(x[n + 1]))))
    n = n + 1

print("-----------------------")
print("xn - x: " + str("{:.6f}".format(abs(x[n+1] - x[n]))))
print("c: " + str("{:.5f}".format(x[n])))
print("f(c): " + str("{:.5f}".format(f(x[n]))))