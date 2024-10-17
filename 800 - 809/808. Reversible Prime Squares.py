from math import *


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def next_prime(current_number):
    while True:
        current_number += 1
        if is_prime(current_number):
            return current_number


def get_reverse(num):

    return int(str(num)[::-1])


def main():
    reversible_prime_squares = set([])
    num = 3

    while len(reversible_prime_squares) != 50:

        num = next_prime(num)
        num_squared = num ** 2
        num_squared_reversed = get_reverse(num_squared)

        if num_squared_reversed == num_squared:
            continue

        if sqrt(num_squared_reversed) % 1 == 0 and is_prime(sqrt(num_squared_reversed)):
            reversible_prime_squares.add(num_squared)

    return sum(reversible_prime_squares)




print(main())
