from math import *


def get_primes(max_num):
    return [x for x in range(2, max_num) if is_prime(x)]


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def main(max_num):
    primes = get_primes(max_num)
    greatest_prime_made = 0
    greatest_chain = 0
    while len(primes) > 0:
        start_prime = primes[0]
        sum = start_prime
        chain = 1

        for next_prime in primes[1:]:
            sum += next_prime
            chain += 1
            if sum > max_num:
                break
            if greatest_chain < chain and sum in primes:
                greatest_prime_made = sum
                greatest_chain = chain

        primes = primes[1:]
    print(greatest_chain)
    return greatest_prime_made


print(main(1_000_000))
