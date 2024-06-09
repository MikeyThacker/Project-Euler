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


def check_lists(list_smaller, list_bigger):
    works_dict = {}
    for num2 in list_smaller:
        first_two = str(num2)[:2]

        for num1 in list_bigger:
            last_two = str(num1)[2:]

            if first_two == last_two:
                works_dict[num1] = num2
    return works_dict


def main():
    triangle_numbers = get_triangle_numbers()
    square_numbers = get_square_numbers()
    pentagonal_numbers = get_pentagonal_numbers()
    hexagonal_numbers = get_hexagonal_numbers()
    heptagonal_numbers = get_heptagonal_numbers()
    octagonal_numbers = get_octagonal_numbers()

    works_7 = check_lists(octagonal_numbers, heptagonal_numbers)
    works_6 = check_lists(works_7, hexagonal_numbers)
    works_5 = check_lists(works_6, pentagonal_numbers)
    works_4 = check_lists(works_5, square_numbers)
    works_3 = check_lists(works_4, triangle_numbers)
    works_8 = check_lists(works_3, octagonal_numbers)

    nums = []
    nums.append(works_8[list(works_8)[0]])
    nums.append(works_3[list(works_3)[0]])
    nums.append(works_4[list(works_4)[0]])
    nums.append(works_5[list(works_5)[0]])
    nums.append(works_6[list(works_6)[0]])
    nums.append(works_7[list(works_7)[0]])


print(main())