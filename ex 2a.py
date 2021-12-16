# Άσκηση 2 Μέθοδος Newton-Raphson

import sympy as sp

x = sp.Symbol('x')

f = 54 * x ** 6 + 45 * x ** 5 - 102 * x ** 4 - 69 * x ** 3 + 35 * x ** 2 + 16 * x - 4
f_prime = f.diff(x)
f_2nd_prime = f.diff(x).diff(x)
f = sp.lambdify('x', f)
f_prime = sp.lambdify('x', f_prime)
f_2nd_prime = sp.lambdify('x', f_2nd_prime)

eps = 10**(-13)
x = 0
xn = x - (1 / (f_prime(x) /f(x)) - 0.5 * (f_2nd_prime(x) / f_prime(x)))
n = 0


while abs(xn - x) > eps:
    x = xn
    xn = x - (1 / (f_prime(x) /f(x)) - 0.5 * (f_2nd_prime(x) / f_prime(x)))
    n = n + 1

print(n)
print(x)
