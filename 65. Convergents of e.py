from math import *
from decimal import *
from fractions import *


def get_sequence(x):
    '''
    For the continued fraction of e:
    The patter goes [2]
    Followed by [1, i*2, 1] where i increases by 1 each time
    '''

    pattern = [2]
    i = 1
    while len(pattern) < 100:
        pattern.extend([1, i * 2, 1])
        i += 1
    return pattern[:101]  # Restrain length to 100


def create_fraction(sequence):
    sequence.reverse()
    fraction = sequence[0]
    for num in sequence[1:]:
        total_denominator = Fraction(1, total_denominator) + Fraction(num, 1)
    return total_denominator


def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total


def main():
    sequence = get_sequence(Decimal(e))
    fraction = create_fraction(sequence)
    numerator = fraction.numerator
    return sum_of_digits(numerator)


print(main())
