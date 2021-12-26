# Άσκηση 1 Μέθοδος Τέμνουσας

from math import e as e


def f(x):
    return 14 * x * e ** (x - 2) - 12 * e ** (x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12


eps = 10 ** (-5)

print("Δώσε το x0:")
x0 = float(input())
print("Δώσε το x1:")
x1 = float(input())
if f(x0) == 0 or f(x1) == 0:
    exit("Έδωσες μια ρίζα!")

x = [x0, x1]
n = 0
while abs(x[n + 1] - x[n]) >= eps:
    n = n + 1
    Dx = x[n] - x[n - 1]
    Dy = f(x[n]) - f(x[n - 1])
    c = x[n] - ((f(x[n]) * Dx) / Dy)
    x.append(c)
    print("n: " + str(n) + ", x" + str(n - 1) + ": " + str("{:.5f}".format(x[n - 1])) + ", x" + str(n) + ": " + str(
        "{:.5f}".format(x[n])) + ", x" + str(n + 1) + ": " + str(
        "{:.5f}".format(x[n + 1])) + ", f(x" + str(n + 1) + "): " + str("{:.5f}".format(f(x[n + 1]))))

print("-------------------")
print("c: " + str("{:.5f}".format(x[n])))
print("f(c): " + str("{:.5f}".format(f(x[n]))))
