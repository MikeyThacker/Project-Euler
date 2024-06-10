from math import *


def get_nums():
    nums = []

    # Triangle Numbers
    n = 1
    while True:
        next = n * (n + 1) // 2
        if next > 10_000:
            break
        if next >= 1_000:
            nums.append((next, 3))
        n += 1

    # Square Numbers
    n = 1
    while True:
        next = n ** 2
        if next > 10_000:
            break
        if next >= 1_000:
            nums.append((next, 4))
        n += 1

    # Pentagon Numbers
    n = 1
    while True:
        next = n * ((3 * n) - 1) // 2
        if next > 10_000:
            break
        if next >= 1_000:
            nums.append((next, 5))
        n += 1

    # Hexagon Numbers
    n = 1
    while True:
        next = n * ((2 * n) - 1)
        if next > 10_000:
            break
        if next >= 1_000:
            nums.append((next, 6))
        n += 1

    # Heptagon Numbers
    n = 1
    while True:
        next = n * ((5 * n) - 3) // 2
        if next > 10_000:
            break
        if next >= 1_000:
            nums.append((next, 7))
        n += 1

    # Octagon Numbers
    n = 1
    while True:
        next = n * ((3 * n) - 2)
        if next > 10_000:
            break
        if next >= 1_000:
            nums.append((next, 8))
        n += 1

    return nums


def check_property(num1, num2):
    """
    :param num1: Number to check last two digits of
    :param num2: Number to check first two digits of
    :return: boolean
    """
    last = str(num1)[2:]
    first = str(num2)[:2]
    return first == last


def get_connections(all_nums):
    dictionary = {}
    for num1 in all_nums:
        cyclic_to_x = []
        for num2 in all_nums:
            if num1[0] == num2[0]:  # If numbers are same value
                continue
            elif num1[1] == num2[1]:  # If numbers are same shape
                continue
            elif not check_property(num1[0], num2[0]):
                continue
            cyclic_to_x.append(num2)
        dictionary[num1] = cyclic_to_x
    return dictionary


def find_route(connections):
    # TODO Step 3: https://www.ivl-projecteuler.com/overview-of-problems/20-difficulty/problem-61
    return None


def main():
    all_nums = get_nums()
    connections = get_connections(all_nums)
    solution = find_route(connections)


print(main())

# [8256, 5625, 2512, 1281, 8128, 2882]
