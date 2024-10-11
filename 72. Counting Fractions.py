from decimal import *
from math import *
from itertools import count


def get_primes(MAX):
    all_nums = [True] * MAX
    all_nums[0] = False
    all_nums[1] = False

    for num in range(MAX):
        if all_nums[num]:
            for factor in count(2):
                multiple = factor * num
                if multiple >= MAX:
                    break
                all_nums[multiple] = False
    primes = [number for number, state in enumerate(all_nums) if state]
    return primes


def get_prime_factors(n, primes):
    factors = []
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
    return factors


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
    primes = get_primes(d)

    for n in range(2, d):
        getcontext().prec = 100
        if n % 2 == 0:  # If n is even:
            this_count = Decimal((d - n) / 2)
        else:
            smallest_prime_factor = get_prime_factors(n, primes)
            # TODO calculate sum based on prime factors

            remaining_fractions = d - n
            this_count = Decimal(remaining_fractions / smallest_prime_factor)
            this_count = Decimal(remaining_fractions - this_count)
            this_count = ceil(this_count)

        print(f"{n}: {int(this_count)}")
        count += this_count
    return count


print(main())
