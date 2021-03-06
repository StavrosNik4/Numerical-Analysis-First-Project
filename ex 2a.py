# Άσκηση 2 Μέθοδος Newton-Raphson

# Functions

def f(z):
    return 54 * z ** 6 + 45 * z ** 5 - 102 * z ** 4 - 69 * z ** 3 + 35 * z ** 2 + 16 * z - 4


def f_prime(z):
    return 324 * z ** 5 + 225 * z ** 4 - 408 * z ** 3 - 207 * z ** 2 + 70 * z + 16


def f_2nd_prime(z):
    return 1620 * z ** 4 + 900 * z ** 3 - 1224 * z ** 2 - 414 * z + 70


# Main

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

h = 1 / (f_prime(x[0]) / f(x[0]) - 0.5 * (f_2nd_prime(x[0]) / f_prime(x[0])))
n = 0
xn = x[n] - h
while abs(xn - x[n]) >= eps:
    x.append(xn)
    n = n + 1
    print("n: " + str(n) + ", x[" + str(n) + "]: " + str("{:.5f}".format(x[n])) + ", f(x): " + str("{:.5f}".format(f(x[n]))))
    if round(f(x[n]), 5) == 0:
        break
    h = 1 / (f_prime(x[n]) / f(x[n]) - 0.5 * f_2nd_prime(x[n]) / f_prime(x[n]))
    xn = x[n] - h

print("----------------------")

print("c: " + str("{:.5f}".format(x[n])))
print("f(c): " + str("{:.5f}".format(f(x[n]))))
