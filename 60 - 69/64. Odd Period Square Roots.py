from math import *


def get_sequence_length(x):
    x_list = [sqrt(x)]
    a_list = [floor(sqrt(x))]
    p = 1
    q = a_list[0]
    # numerator = p(sqrt(x) q -> p = last denominator
    # denominator = 23 - A[n]^2

    while True:
        """
        p( sqrt(x) + q )
        ----------------
               d 
        """
        d = x - (q ** 2)  # Denominator

        x_list.append(p * (sqrt(x) + q) / d)
        a_list.append(floor(x_list[-1]))
        q = abs(q - (a_list[-1] * (d / p)))
        p = d /p

        if a_list[-1] == 2 * a_list[0]:
            print(len(a_list))
            return len(a_list) - 1


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
