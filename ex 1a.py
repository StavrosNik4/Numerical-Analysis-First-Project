# Άσκηση 1 Μέθοδος Διχοτόμισης

from math import e as e
import sympy as sp

def f(x):
    return 14 * x * e ** (x - 2) - 12 * e ** (x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12

x = sp.Symbol('x')
fx = 14 * x * e ** (x - 2) - 12 * e ** (x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12
fx_prime = fx.diff(x)
fx = sp.lambdify('x', fx)
fx_prime = sp.lambdify('x', fx_prime)

a = 0
b = 1.5
n = 0
eps = 10 ** (-6)
rootFound = False

fa = f(a)
fb = f(b)

if fa == 0:
    rootFound = True
    c = a
elif fb == 0:
    rootFound = True
    c = b
elif fa * fb > 0:
    exit("can't find root in that field")
else:
    while not rootFound:
        c = 0.5 * (a + b)
        fc = f(c)
        print("n: " + str("{:.5f}".format(n)) + " a: " + str("{:.5f}".format(a)) + ", b: " + str(
            "{:.5f}".format(b)) + ", c: " + str("{:.5f}".format(c)) + ", f(c): " + str(
            "{:.5f}".format(fc)))
        if fc == 0:
            rootFound == True
            break
        elif fc * fa > 0:
            a = c
        else:
            b = c

        fa = f(a)

        if 0.5 * abs(b - a) < eps:
            rootFound = True
            break
        n = n + 1

print("--------------")

print("f(c): " + str(fx(c)))
print("f(2): " + str(fx(2)))
print("f'(c): " + str(fx_prime(c)))
print("f'(2): " + str(fx_prime(2)))