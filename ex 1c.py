# Άσκηση 1 Μέθοδος Τέμνουσας

from math import e as e
import sympy as sp

z = sp.Symbol('z')

f = 14 * z * e ** (z - 2) - 12 * e ** (z - 2) - 7 * z ** 3 + 20 * z ** 2 - 26 * z + 12
f = sp.lambdify('z', f)

eps = 10**(-5)

x = [1.6, 2.2]

n = 0

while abs(x[n+1] - x[n]) >= eps:
    n = n + 1
    Dx = x[n] - x[n-1]
    Dy = f(x[n]) - f(x[n-1])
    c = x[n] - ((f(x[n]) * Dx) / Dy)
    x.append(c)
    d = abs(x[n+1] - x[n])
    print("n: " + str(n) + " x: " + str("{:.5f}".format(x[n + 1])) + ", f(x): " + str(
        "{:.5f}".format(f(x[n + 1]))) + ", d: " + str("{:.5f}".format(d)))

print("-------------------")
print("c: " + str("{:.5f}".format(x[n])))
print("f(c): " + str("{:.5f}".format(f(x[n]))))
