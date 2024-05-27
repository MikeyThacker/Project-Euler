from math import *


def make_list(numerator, denominator):
    digits_used = set([])
    for digit in str(numerator):
        digits_used.add(str(digit))

    for digit in str(denominator):
        digits_used.add(str(digit))

    return digits_used


def main():
    fractions = []
    for denominator in range(11, 100):
        for numerator in range(10, denominator):

            included_nums = make_list(numerator, denominator)
            for num in included_nums:
                numerator = str(numerator)
                denominator = str(denominator)

                new_numerator = numerator.replace(num, "")
                new_denominator = denominator.replace(num, "")
                if not (new_numerator and new_denominator):
                    continue

                new_numerator = int(new_numerator)
                new_denominator = int(new_denominator)
                numerator = int(numerator)
                denominator = int(denominator)

                try:
                    if new_numerator / new_denominator == numerator / denominator:
                        fractions.append([numerator, denominator])
                except ZeroDivisionError:
                    pass

    non_trivial_product_numerator = 1
    non_trivial_product_denominator = 1
    for fraction in fractions:
        if not int(fraction[0]) % 10 == 0 or not int(fraction[1]) % 10 == 0:
            non_trivial_product_numerator *= int(fraction[0])
            non_trivial_product_denominator *= int(fraction[1])

    return non_trivial_product_denominator / gcd(non_trivial_product_numerator, non_trivial_product_denominator)


print(main())
