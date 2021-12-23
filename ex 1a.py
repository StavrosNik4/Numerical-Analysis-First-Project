# Άσκηση 1 Μέθοδος Διχοτόμισης

from math import e as e


def fx(x):
    return 14 * x * e ** (x - 2) - 12 * e ** (x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12


a = 1.5
b = 3
n = 0
c = 0  # for the warning
eps = 10 ** (-5)

fa = fx(a)
fb = fx(b)

if fa == 0:
    c = a
elif fb == 0:
    c = b
else:
    while abs(b - a) >= eps / 2:
        n = n + 1
        c = 0.5 * (a + b)
        fc = fx(c)
        fa = fx(a)
        print("n: " + str(n) + ", a: " + str("{:.5f}".format(a)) + ", b: " + str(
            "{:.5f}".format(b)) + ", c: " + str("{:.5f}".format(c)) + ", f(c): " + str(
            "{:.5f}".format(fc)))
        if fc == 0:
            break
        elif fc * fa > 0:
            a = c
        else:
            b = c


print("--------------")

print("c: " + str("{:.5f}".format(c)))
print("f(c): " + str("{:.5f}".format(fx(c))))
