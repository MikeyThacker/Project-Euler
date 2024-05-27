from math import *


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def num_primes_produced(a, b):
    n = -1
    while True:
        n += 1
        num_produced = (n ** 2) + (a * n) + b
        if not is_prime(num_produced):
            return n


def main():
    max_primes_produced = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            primes_produced = num_primes_produced(a, b)

            if primes_produced > max_primes_produced:
                max_coefficients = [a, b]
                max_primes_produced = primes_produced

    return prod(max_coefficients)


print(main())
