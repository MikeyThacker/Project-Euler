from math import *


def truncate(num):
    new_num_L, new_num_R = str(num), str(num)

    for _ in range(len(str(num)) - 1):
        new_num_R = new_num_R[1:]
        new_num_L = new_num_L[:-1]

        if not is_prime(int(new_num_R)):
            return False
        if not is_prime(int(new_num_L)):
            return False
    return True


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def main():
    truncatable_primes = []
    num = 10

    while len(truncatable_primes) < 11:
        num += 1
        if num % 2 == 0 or num % 5 == 0:
            continue

        if not is_prime(num):
            continue

        if truncate(num):
            truncatable_primes.append(num)
    return sum(truncatable_primes)


print(main())
