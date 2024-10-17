from fractions import *


def middle_fraction(frac1, frac2):
    a = frac1.numerator
    b = frac1.denominator
    c = frac2.numerator
    d = frac2.denominator
    new_fraction = Fraction(a + c, b + d)

    return new_fraction


def main(d):
    max_denominator = d

    left_border = Fraction(2, 5)
    right_border = Fraction(3, 7)

    last_left_border = left_border

    while left_border.denominator < max_denominator:
        last_left_border = left_border
        left_border = middle_fraction(left_border, right_border)

    return last_left_border


print(main(1_000_000))
