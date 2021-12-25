# Άσκηση 1 Μέθοδος Newton-Raphson

import numpy as np
import sympy as sp

x = sp.Symbol('x')

f = 1.1 * x ** 4 - 2.5
f_prime = f.diff(x)
f = sp.lambdify('x', f)
f_prime = sp.lambdify('x', f_prime)

eps = 10 ** (-2)
x = 8.8
xn = x - (f(x) / f_prime(x))
n = 1

print(n)
print(xn)

x = xn
xn = x - (f(x) / f_prime(x))
n = n + 1

print(n)
print(xn)

'''
while abs(xn - x) > eps:
    x = xn
    xn = x - (f(x)/f_prime(x))
    n = n + 1
'''


# alla

print("---------------")

def padiko(p, n, c):
    g = 2 * (2 * c + 1) * (p - 1) * p ** (n - 1) + 1
    return g


print(padiko(9, 3, 8))

print("---------------")


def epanalipseis(k, ba):
    ep = 0.5 * 10 ** (-k)
    return np.ceil(((np.log(ba) - np.log(ep)) / np.log(2)))


print(epanalipseis(5, 1))

print("---------------")

