from math import *


def is_prime(num):
    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def next_prime(n):
    while True:
        n += 1
        if is_prime(n): return n


def main():
    # Two numbers are considered relatively prime if the only factor between them is 1.
    # This is also known as coprime
    ans = 1
    current_prime = 1
    while True:
        if ans * next_prime(current_prime) > 1000000: return ans
        current_prime = next_prime(current_prime)
        ans *= current_prime


print(main())
