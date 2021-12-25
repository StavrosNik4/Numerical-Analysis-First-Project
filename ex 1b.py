# Άσκηση 1 Μέθοδος Newton-Raphson

import sympy as sp
from math import e as e


def f(x):
    return 14 * x * e ** (x - 2) - 12 * e ** (x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12


def f_prime(x):
    return 14 * x * e ** (x - 2) + 2 * e ** (x - 2) - 21 * x ** 2 + 40 * x - 26


def f_2nd_prime(x):
    return 14 * x * e ** (x - 2) + 16 * e ** (x - 2) - 42 * x + 40


eps = 10 ** (-5)
x = 0
n = 0
h = f(x) / f_prime(x)

print(f(x) * f_2nd_prime(x))

while abs(h) >= eps:
    n = n + 1
    x = x - (f(x) / f_prime(x))
    h = f(x) / f_prime(x)
    print("n: " + str(n) + ", x: " + str("{:.5f}".format(x)) + ", f(x): " + str("{:.5f}".format(f(x))))
    if f(x) == 0:
        break

print("-------------------")
print("c: " + str("{:.5f}".format(x)))
print("f(c): " + str("{:.5f}".format(f(x))))
