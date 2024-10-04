from fractions import *


def middle_fraction(frac1, frac2):
    a = frac1.numerator
    b = frac1.denominator
    c = frac2.numerator
    d = frac2.denominator
    new_fraction = Fraction(a + c, b + d)

    return new_fraction


def find_fractions_between(frac1, frac2, count):
    mid = middle_fraction(frac1, frac2)
    if mid.denominator > 1_000_000:
        return count

    count += find_fractions_between(frac1, mid.numerator, count)
    return count


def main():
    upper = Fraction(1, 1)
    lower = Fraction(0, 1)

    count = find_fractions_between(upper, lower, 0)

    return count


print(main())
