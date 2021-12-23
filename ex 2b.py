# Άσκηση 2 Μέθοδος Διχοτόμισης

import random


def f(x):
    return 54 * x ** 6 + 45 * x ** 5 - 102 * x ** 4 - 69 * x ** 3 + 35 * x ** 2 + 16 * x - 4


a = random.uniform(-2, 2)
b = random.uniform(-2, 2)
while a >= b:
    b = random.uniform(-2, 2)


print(a)
print(b)

n = 0
eps = 10 ** (-5)

c = 0   # for the warning
fa = f(a)
fb = f(b)

if fa == 0:
    c = a
elif fb == 0:
    c = b
elif fa * fb > 0:
    exit("can't find root in this space!")
else:
    while abs(b - a) >= eps * 0.5:
        fa = f(a)
        n = n + 1
        c = 0.5 * (a + b)
        fc = f(c)
        print("n: " + str("{:.5f}".format(n)) + " a: " + str("{:.5f}".format(a)) + ", b: " + str(
            "{:.5f}".format(b)) + ", c: " + str("{:.5f}".format(c)) + ", f(c): " + str(
            "{:.5f}".format(fc)))
        if fc == 0:
            break
        elif fc * fa > 0:
            a = c
        else:
            b = c

print("----------------------")

print("c: " + str("{:.5f}".format(c)))
print("f(c): " + str("{:.5f}".format(f(c))))