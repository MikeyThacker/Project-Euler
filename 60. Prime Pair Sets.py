from math import *


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def is_prime_concatenations(primes):
    for index_1, prime_1 in enumerate(primes):
        for index_2 in range(index_1, 5):
            prime_2 = primes[index_2]
            if prime_1 == prime_2:
                continue

            if not is_prime(int(f"{prime_1}{prime_2}")) or not is_prime(int(f"{prime_2}{prime_1}")):
                return False
    return True


def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num


def main():
    all_primes = [num for num in range(1_000) if is_prime(num)]
    for index_1, prime_1 in enumerate(all_primes):
        try:
            for index_2 in range(index_1 + 1, len(all_primes)):
                for index_3 in range(index_2 + 1, len(all_primes)):
                    for index_4 in range(index_3 + 1, len(all_primes)):
                        for index_5 in range(index_4 + 1, len(all_primes)):
                            prime_2 = all_primes[index_2]
                            prime_3 = all_primes[index_3]
                            prime_4 = all_primes[index_4]
                            prime_5 = all_primes[index_5]
                            five_primes = [prime_1, prime_2, prime_3, prime_4, prime_5]
                            if is_prime_concatenations(five_primes):
                                return five_primes, sum(five_primes)
        except IndexError:
            return None


print(main())
