from math import *


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def main():
    i = 33

    while True:
        i += 2

        if is_prime(i):
            continue

        check = False
        for sq in range(1, ceil(sqrt(i)) + 1):
            left = i - (2*(sq**2))
            if is_prime(left):
                check = True
        if not check:
            return i



print(main())
