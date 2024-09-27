from math import *
from decimal import *


def get_sequence_length(x):
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
        p = d /p

        if A[-1] == 2 * A[0]:
            print(len(A))
            return len(A) - 1


def main():
    count = 0  # Number of odd period square roots
    N = 1  # Number to square root

    while N <= 10_000:

        if sqrt(N) % 1 == 0:  # Check for irrational square roots
            N += 1
            continue

        sequence_length = get_sequence_length(N)
        if sequence_length % 2 == 1:  # If sequence length is odd
            count += 1

        N += 1

    return count


print(main())
