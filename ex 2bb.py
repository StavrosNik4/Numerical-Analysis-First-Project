# Άσκηση 1 Μέθοδος Διχοτόμισης


def fx(z):
    return 54 * z ** 6 + 45 * z ** 5 - 102 * z ** 4 - 69 * z ** 3 + 35 * z ** 2 + 16 * z - 4

1
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
c = 0  # for the warning
eps = 10 ** (-5)

fa = fx(a)
fb = fx(b)

if fa == 0:
    c = a
elif fb == 0:
    c = b
elif fa*fb > 0:
    exit("can't find root in this space!")
else:
    c = a
    while abs(b - a) >= eps/2:
        n = n + 1
        c = 0.5 * (a + b)
        fc = fx(c)
        fa = fx(a)

        print("n: " + str(n) + ", a: " + str("{:.5f}".format(a)) + ", b: " + str(
            "{:.5f}".format(b)) + ", c: " + str("{:.5f}".format(c)) + ", f(c): " + str(
            "{:.5f}".format(fc)))

        if fc == 0:
            break
        elif fc * fa >= 0:
            a = c
        else:
            b = c

print("--------------")

print("c: " + str("{:.5f}".format(c)))
print("f(c): " + str("{:.5f}".format(fx(c))))
