from math import *


def get_triangle_numbers():
    triangle_numbers = []
    n = 1
    while True:
        next_num = (n * (n + 1) // 2)
        if next_num >= 10_000:
            return triangle_numbers
        if next_num > 999:
            triangle_numbers.append(next_num)
        n += 1


def get_square_numbers():
    numbers = [x for x in range(1000, 10_000) if sqrt(x) % 1 == 0]
    return numbers


def get_pentagonal_numbers():
    pentagonal_numbers = []
    n = 1
    while True:
        next_num = (n * ((3 * n) - 1) // 2)
        if next_num >= 10_000:
            return pentagonal_numbers
        if next_num > 999:
            pentagonal_numbers.append(next_num)
        n += 1


def get_hexagonal_numbers():
    hexagonal_numbers = []
    n = 1
    while True:
        next_num = n * ((2 * n) - 1)
        if next_num >= 10_000:
            return hexagonal_numbers
        if next_num > 999:
            hexagonal_numbers.append(next_num)
        n += 1


def get_heptagonal_numbers():
    heptagonal_numbers = []
    n = 1
    while True:
        next_num = (n * ((5 * n) - 3) // 2)
        if next_num >= 10_000:
            return heptagonal_numbers
        if next_num > 999:
            heptagonal_numbers.append(next_num)
        n += 1


def get_octagonal_numbers():
    octagonal_numbers = []
    n = 1
    while True:
        next_num = n * ((3 * n) - 2)
        if next_num >= 10_000:
            return octagonal_numbers
        if next_num > 999:
            octagonal_numbers.append(next_num)
        n += 1


def has_property(num1, num2):
    """
    :param num1: Num to check first two digits of
    :param num2: Num to check last two digits of
    :return: Boolean
    """

    first = str(num1)[:2]
    last = str(num2)[2:]
    return first == last


def check_lists(list1, list2):
    """
    :param list1: List to check first two digits of each number
    :param list2: List to check last two digits of each number
    :return:
    """


def main():
    triangle_numbers = get_triangle_numbers()
    square_numbers = get_square_numbers()
    pentagonal_numbers = get_pentagonal_numbers()
    hexagonal_numbers = get_hexagonal_numbers()
    heptagonal_numbers = get_heptagonal_numbers()
    octagonal_numbers = get_octagonal_numbers()
    pass


print(main())
