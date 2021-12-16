# Άσκηση 1 Μέθοδος Newton-Raphson

import sympy as sp
from math import e as e

"""
def newtonraphson(f, f_prime, x, tol):
    xn = x - (f(x)-f_prime(x))
    if abs(xn - x) > tol:
        return newtonraphson(f, f_prime, xn, tol)
    else:
        return x
"""

x = sp.Symbol('x')

f = 14 * x * e ** (x - 2) - 12 * e ** (x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12
f_prime = f.diff(x)
f = sp.lambdify('x', f)
f_prime = sp.lambdify('x', f_prime)


eps = 10**(-6)
x = 0
xn = x - (f(x) / f_prime(x))
n = 0

#newtonraphson(f, f_prime, x, eps)

while abs(xn - x) > eps:
    x = xn
    xn = x - (f(x)/f_prime(x))
    n = n + 1

print(n)
print(xn)
