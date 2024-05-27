from math import *


def main():
    number = 600851475143
    number_factors = find_factors(number)
    number_factors.sort(reverse=True)

    for factor in number_factors:
        if len(find_factors(factor)) < 3:
            return factor


def find_factors(num):
    factors = []

    for i in range(1, ceil(sqrt(num))):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return factors


print(main())
