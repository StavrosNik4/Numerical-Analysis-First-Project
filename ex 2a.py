# Άσκηση 2 Μέθοδος Newton-Raphson

import sympy as sp

z = sp.Symbol('z')

f = 54 * z ** 6 + 45 * z ** 5 - 102 * z ** 4 - 69 * z ** 3 + 35 * z ** 2 + 16 * z - 4
f_prime = 324 * z ** 5 + 225 * z ** 4 - 408 * z ** 3 - 207 * z ** 2 + 70 * z + 16
f_2nd_prime = 1620 * z ** 4 + 900 * z ** 3 - 1224 * z ** 2 - 414 * z + 70
f = sp.lambdify('z', f)
f_prime = sp.lambdify('z', f_prime)
f_2nd_prime = sp.lambdify('z', f_2nd_prime)

print(f(-1)*f_2nd_prime(-1))

eps = 10 ** (-13)
x = -1
xn = x - (1 / (f_prime(x) / f(x)) - (0.5 * f_2nd_prime(x) / f_prime(x)))
n = 0

while abs(xn - x) > eps:
    x = xn
    xn = x - (1 / (f_prime(x) / f(x)) - (0.5 * f_2nd_prime(x) / f_prime(x)))
    n = n + 1

print(n)
print(x)
print(f(x))
