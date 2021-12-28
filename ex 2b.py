# Άσκηση 2 Μέθοδος Διχοτόμισης

import random

def f(x):
    return float(54 * x ** 6 + 45 * x ** 5 - 102 * x ** 4 - 69 * x ** 3 + 35 * x ** 2 + 16 * x - 4)


print("Δώσε διάστημα για εύρεση ρίζας:")
print("a: ")
a = float(input())
print("b: ")
b = float(input())
while b < a:
    print("Το b δεν μπορεί να είναι μικρότερο από το a!")
    print("b: ")
    b = float(input())


n = 0
eps = 10 ** (-5)
c = 0   # for the warning

if f(a) == 0:
    c = a
elif f(b) == 0:
    c = b
elif f(a) * f(b) > 0:
    exit("can't find root in this space!")
else:
    while abs(b-a) >= eps * 0.5:
        n = n + 1
        c = random.uniform(a, b)
        print("n: " + str("{:.5f}".format(n)) + " a: " + str("{:.5f}".format(a)) + ", b: " + str(
            "{:.5f}".format(b)) + ", c: " + str("{:.5f}".format(c)) + ", f(c): " + str(
            "{:.5f}".format(f(c))))
        if f(c) == 0:
            break
        elif f(c) * f(a) > 0:
            a = c
        else:
            b = c

print("----------------------")

print("c: " + str("{:.5f}".format(c)))
print("f(c): " + str("{:.5f}".format(f(c))))
