# Άσκηση 1 Μέθοδος Newton-Raphson

import sympy as sp
from math import e as e

x = sp.Symbol('x')

f = 14 * x * e ** (x - 2) - 12 * e ** (x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12
f = sp.lambdify('x', f)
f_prime = sp.diff(14 * x * e ** (x - 2) - 12 * e ** (x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12)

# f_prime = 14 * x * e ** (x-2) + 2 * e ** (x-2) - 21 * x ** 2 - 40 * x - 26


f_prime = sp.lambdify('x', f_prime)
f_2nd_prime = 14 * x * e ** (x - 2) + 16 * e ** (x - 2) - 42 * x + 40
f_2nd_prime = sp.lambdify('x', f_2nd_prime)

eps = 10 ** (-5)
x0 = 0
xn = x0 - (f(x0) / f_prime(x0))
n = 0

print(f(x0) * f_2nd_prime(x0))

while abs(xn - x0) > eps:
    n = n + 1
    print("n: " + str(n) + ", x0: " + str("{:.5f}".format(x0)) + ", xn: " + str(
        "{:.5f}".format(xn)) + ", c: " + ", f(xn): " + str(
        "{:.5f}".format(f(xn))))
    x0 = xn
    xn = x0 - (f(x0) / f_prime(x0))
    if f(xn) == 0:
        break

print("-------------------")
print("c: " + str("{:.5f}".format(xn)))
print("f(c): " + str("{:.5f}".format(f(xn))))
