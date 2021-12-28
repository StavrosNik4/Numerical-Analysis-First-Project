from math import e as e

def f(z):
    return 54 * z ** 6 + 45 * z ** 5 - 102 * z ** 4 - 69 * z ** 3 + 35 * z ** 2 + 16 * z - 4


def f_prime(z):
    return 324 * z ** 5 + 225 * z ** 4 - 408 * z ** 3 - 207 * z ** 2 + 70 * z + 16


def f_2nd_prime(z):
    return 1620 * z ** 4 + 900 * z ** 3 - 1224 * z ** 2 - 414 * z + 70



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