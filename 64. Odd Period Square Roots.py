from math import *
from decimal import *


def get_sequence(x):
    n = 0
    X = [x]
    X_Rounded = [x]
    A = [floor(x)]

    while True:
        n += 1
        X.append(Decimal(1 / (X[n - 1] - A[n - 1])))  # e.g., x1 = 1/ x0-a0
        X_Rounded.append(round(X[-1], 6))

        if X_Rounded.count(X_Rounded[-1]) > 1:  # Check if pattern is repeating
            return A, X_Rounded.index(X_Rounded[-1])  # Return sequence and first digit of cycle
        A.append(floor(X[n]))


def main():
    count = 0  # Number of odd period square roots
    N = 1  # Number to sqrt

    while N <= 1000:
        N += 1
        print(N)
        root_N = Decimal(sqrt(N))

        if root_N % 1 == 0:  # Check for irrational square roots
            continue

        sequence, index = get_sequence(root_N)

        length_cycle = len(sequence[index:])
        if length_cycle % 2 == 1:
            count += 1
    return count


print(main())
