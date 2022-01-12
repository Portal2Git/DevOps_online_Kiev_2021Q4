import math
import sys


def main():
    a = input("Enter the coefficient of a: ")
    a = validate_param(a)
    b = input("Enter the coefficient of b: ")
    b = validate_param(b)
    c = input("Enter the coefficient of c: ")
    c = validate_param(c)
    r = solv_square(a, b, c)
    square_print(a, b, c, r)


def validate_param(p):
    i = 0
    while i < 3:
        try:
            p = float(p)
        except ValueError:
            i += 1
            print("Input is incorrect. Try again.")
            p = input("Enter correct value: ")
        else:
            return p
    sys.exit(2)


def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c  # discriminant
    return d


def roots(d, a, b, c):
    if a == 0:
        sys.exit(3)
    if d < 0:
        return None
    elif d == 0:
        x = (-b + math.sqrt(d)) / 2 * a
        return x
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2


def solv_square(a, b, c):
    d = discriminant(a, b, c)
    return roots(d, a, b, c)


def square_print(a, b, c, r):
    eq = f"For equation: {a}*x\u00B2"
    if b < 0:
        eq = eq+f" - {abs(b)}*x"
    else:
        eq = eq + f" + {b}*x"
    if c < 0:
        eq = eq+f" - {abs(c)} = 0"
    else:
        eq = eq + f" + {c} = 0"
    print(eq)
    if r is None:
        print("There is no solutions at real numbers")
    else:
        if type(r) == float:
            print("Roots are: X1 = X2 =", r)
        else:
            print(f"Roots are: X1 = {r[0]}, X2 = {r[1]}")


if __name__ == '__main__':
    main()
