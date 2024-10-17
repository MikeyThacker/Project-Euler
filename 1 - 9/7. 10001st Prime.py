from math import *


def main():
    num_of_primes = 5
    var = 12
    while num_of_primes < 10_001:
        var += 1
        if is_prime(var):
            num_of_primes += 1

    return var

def is_prime(num):
    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

print(main())