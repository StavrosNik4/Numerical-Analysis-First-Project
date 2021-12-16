# Άσκηση 1 Μέθοδος Τέμνουσας

from math import e as e
import sympy as sp

x = sp.Symbol('x')

f = 14 * x * e ** (x - 2) - 12 * e ** (x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12
f = sp.lambdify('x', f)

x0 = 1.4
x1 = 3
xn = x1 - (f(x1)*(x1-x0)/(f(x1)-f(x0)))
n = 1

while abs(xn-x1) > 10**(-13):
    x0 = x1
    x1 = xn
    xn = x1 - (f(x1)*(x1-x0)/(f(x1)-f(x0)))
    n = n + 1

print(n)
print(xn)