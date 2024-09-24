from math import *
from decimal import *
from fractions import *


def get_sequence(x):
    X = [x]
    A = [floor(x)]
    p = 1
    q = A[0]
    # numerator = p(sqrt(x) q -> p = last denominator
    # denominator = 23 - A[n]^2

    while True:
        '''
        p( sqrt(x) + q )
        ----------------
               d 
        '''
        d = (x ** 2) - (q ** 2)  # Denominator

        X.append(Decimal(p * (x + q) / d))
        A.append(floor(Decimal(X[-1])))
        q = abs(q - (A[-1] * (d / p)))
        p = Decimal(d / p)

        if len(A) == 100:
            return A


def create_fraction(sequence):
    sequence.reverse()
    total_denominator = sequence[0]
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
