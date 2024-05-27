from math import *


def get_prime_factors(num):
    prime_factors = set([])
    while num % 2 == 0:
        prime_factors.add(2)
        num //= 2

    for i in range(3, ceil(sqrt(num)) + 1, 2):
        while num % i == 0:
            prime_factors.add(i)
            num //= i
    if num == 1:
        return prime_factors
    else:
        prime_factors.add(num)
        return prime_factors


def main():
    num1 = 646
    while True:
        num1 += 1
        num2 = num1 + 1
        num3 = num1 + 2
        num4 = num1 + 3

        a = len(get_prime_factors(num1))
        b = len(get_prime_factors(num2))
        c = len(get_prime_factors(num3))
        d = len(get_prime_factors(num4))

        if a == 4 and b == 4 and c == 4 and d == 4:
            return num1


print(main())
