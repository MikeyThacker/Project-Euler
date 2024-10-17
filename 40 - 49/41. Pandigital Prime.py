from math import *
from itertools import permutations


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def is_pandigital(num):
    if "0" in num:
        return False

    digits = [0 for _ in range(len(num))]
    correct_digits = [1 for _ in range(len(num))]
    for digit in num:
        if int(digit) > len(num):
            return False
        digits[int(digit) - 1] += 1

    if digits == correct_digits:
        return True
    return False


def main():
    largest_pandigital = 0
    for i in range(10, 1, -1):
        all_permutations = permutations([x for x in range(1, i)])
        for permutation in all_permutations:
            number = ""
            for digit in permutation:
                number += str(digit)
            number = int(number)
            if is_pandigital(str(number)) and is_prime(number):
                largest_pandigital = max(number, largest_pandigital)
        if largest_pandigital != 0:
            return largest_pandigital


print(main())
