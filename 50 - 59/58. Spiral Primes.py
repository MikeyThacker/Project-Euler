from math import *


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def main():
    num = 1
    num_diagonals = 1
    prime_diagonals = 0

    side_length = 3
    num_to_add = 0
    while True:
        num_to_add += 2
        for _ in range(4):
            num += num_to_add
            num_diagonals += 1
            if is_prime(num):
                prime_diagonals += 1

        if prime_diagonals / num_diagonals < 0.1:
            return side_length
        side_length += 2


print(main())
