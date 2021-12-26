# Άσκηση 1 Μέθοδος Newton-Raphson

from math import e as e


def f(x):
    return 14 * x * e ** (x - 2) - 12 * e ** (x - 2) - 7 * x ** 3 + 20 * x ** 2 - 26 * x + 12


def f_prime(x):
    return 14 * x * e ** (x - 2) + 2 * e ** (x - 2) - 21 * x ** 2 + 40 * x - 26


def f_2nd_prime(x):
    return 14 * x * e ** (x - 2) + 16 * e ** (x - 2) - 42 * x + 40


eps = 10 ** (-5)

print("Δώσε το x0:")
x0 = float(input())
x = [x0]
if f(x0)*f_2nd_prime(x0) > 0:
    print("Ισχύει το f(x0) * f''(x0) > 0!")
else:
    exit("Δεν ισχύει το f(x0) * f''(x0) > 0!")
if f(x0) == 0:
    exit("Έδωσες την ρίζα για x0!")

h = f(x[0]) / f_prime(x[0])
n = 0

while abs(h) >= eps:
    h = f(x[n]) / f_prime(x[n])
    x.append(x[n] - h)
    n = n + 1
    print("n: " + str(n) + ", x[" + str(n) + "]: " + str("{:.5f}".format(x[n])) + ", f(x): " + str("{:.5f}".format(f(x[n]))))
    if f(x[n]) == 0:
        break

print("-------------------")
print("c: " + str("{:.5f}".format(x[n])))
print("f(c): " + str("{:.5f}".format(f(x[n]))))

if round(f(x[n]), 5) == 0 and round(f_prime(x[n]), 5) != 0:
    print('Συγκλίνει τετραγωνικά!')
else:
    print('Δεν συγκλίνει τετραγωνικά!')