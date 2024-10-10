from decimal import *
from math import *


def main():
    """
    range n from 1 to d

    Generate count of every fraction < 1 with numerator n
    For every even n, count = (d-n) / 2
    For every odd n, count = (d-n) - ((d-n) DIV n), Remove every nth fraction
    (d-n) removes any fractions created where the numerator is greater than the denominator
        and the fraction is therefore greater than one
    """

    d = 1_000_000
    count = d - 1

    for n in range(2, d):
        if n == 208125:
            pass
        getcontext().prec = 100
        if n % 2 == 0:  # If n is even:
            this_count = Decimal((d-n) / 2)
        else:
            remaining_fractions = d - n
            this_count = Decimal(remaining_fractions / n)
            this_count = Decimal(remaining_fractions - this_count)
            this_count = ceil(this_count)

        print(f"{n}: {int(this_count)}")
        count += this_count
    return count



print(main())
