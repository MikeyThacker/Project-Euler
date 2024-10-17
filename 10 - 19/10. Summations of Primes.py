from math import *


def main():
    primes = get_primes(2_000_000)
    return sum_list(primes)


def get_primes(max):
    primes = []
    for i in range(2, max + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(num):
    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def sum_list(list):
    return sum(list)


print(main())
