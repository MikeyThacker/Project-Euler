from math import *
from fractions import *


def get_sequence(x):
    X = [sqrt(x)]
    A = [floor(sqrt(x))]
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
        d = x - (q ** 2)  # Denominator

        X.append(p * (sqrt(x) + q) / d)
        A.append(floor(X[-1]))
        q = abs(q - (A[-1] * (d / p)))
        p = d / p

        if A[-1] == 2 * A[0]:
            return A


def truncate(sequence):
    if len(sequence) % 2 == 1:  # If length of entire sequence is odd, repeating bit is even
        # Return sequence minus last digit
        return sequence[:-1]

    # If even, length of repeating is odd
    # Return sequence + repeated bit - last digit
    sequence.extend(sequence[1:-1])
    return sequence


def create_fraction(sequence):
    sequence.reverse()
    fraction = sequence[0]
    for num in sequence[1:]:
        fraction = Fraction(1, fraction) + Fraction(num, 1)
    return fraction


def get_solution(d):
    """
    In: d - integer value of D
    Out: [x, D] for minimal x in Diophantine equation, y doesn't matter

    Research into Wikipedia shows that the minimal solution for x and y can be found using the continued fraction of
    the square root of d.

    For a number with an even period, the sequence is truncated right before the last digit in the first cycle.
    For a number with an odd period, the sequence is truncated right before the last digit in the second cycle.
    e.g., sqrt(7) = [2;(1,1,1,4)], cycle is 4 long so [2,1,1,1] = 8/3, x = 8, y = 3
    e.g., sqrt(13) = [3;(1,1,1,1,6)], cycle is 5 long so [3,1,1,1,1] = 649/180, x = 649, y = 180
    """
    sequence = get_sequence(d)
    sequence = truncate(sequence)
    fraction = create_fraction(sequence)
    x = fraction.numerator
    return x


def main():
    """
    Diophantine Equation when x^2 -Dy^2 = 1
    When D = 13, minimal solution is 649^2 -13*180^2 = 1
    There are no solutions in positive integers when D is a square number
    """
    max_x = 0
    d_for_max_x = 0

    for d in range(2, 1001):
        if sqrt(d) % 1 == 0:
            continue
        solution = get_solution(d)
        if solution > max_x:
            max_x = solution
            d_for_max_x = d

        print(f"{d} = {solution}")

    return d_for_max_x


print(main())
