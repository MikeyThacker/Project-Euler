from itertools import count
from math import *


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


def get_prime_factors(n, primes, known_factors):

    original_n = n
    factors = set([])
    prime_index = 0

    while n != 1:
        if n in known_factors:
            for factor in known_factors[n]:
                factors.add(factor)
            known_factors[original_n] = factors
            return factors, known_factors
        current_prime = primes[prime_index]

        if current_prime > n //2:
            factors.add(n)
            break
        if n % current_prime == 0:
            # If current prime is a factor of n

            factors.add(current_prime)
            n //= current_prime
        else:
            prime_index += 1

    known_factors[original_n] = factors
    return list(factors), known_factors


def get_count(d, n, primes, known_factors):
    """
    Take number of fractions left (d-n),
    Multiply by (x-1)/x for x in fractions
        This removes every nth fraction
    """
    product = d - n
    prime_factors, known_factors = get_prime_factors(n, primes, known_factors)

    for prime in prime_factors:
        product *= (prime - 1) / prime
    product = ceil(product)

    return product, known_factors


def main():
    """
    range n from 1 to d

    Generate count of every fraction < 1 with numerator n
    (d-n) removes any fractions created where the numerator is greater than the denominator
        and the fraction is therefore greater than one
    """

    d = 1_000_000
    count = d - 1
    primes = get_primes(d)
    # Keep dictionary of prime factors to reference later so smaller numbers not being calculated lots of times
    known_factors = {}

    for n in range(2, d):
        this_count, known_factors = get_count(d, n, primes, known_factors)

        print(f"{n}: {this_count}")
        count += this_count
    return int(count)

print(main())


# 366663327241
# 325714454051
# 354256844782
# 377165084807
# 377164511818
# 303964043372
