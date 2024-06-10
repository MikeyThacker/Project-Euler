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


def list_of_tuples_to_list(old_list):
    new_list = []
    for tuple in old_list:
        new_list.append(tuple[1])
    return sorted(list(set(new_list)))


def find_previous_link(num_search, list):
    for tuple in list:
        if tuple[1] == num_search:
            return tuple[0]


def check_lists(list1, list2):
    '''
    :param list1: list checking last two numbers match
    :param list2: list checking first two numbers match
    :return: dict containing first number leading to second
    '''
    list_of_works = []
    for num1 in list1:
        last_two = str(num1)[2:]

        for num2 in list2:
            first_two = str(num2)[:2]

            if last_two == first_two:
                list_of_works.append((num1, num2))

    return list_of_works


def find_solution(num_to_find, list):
    for tuple in list:
        if tuple[1] == num_to_find:
            return tuple[0]


def main():
    triangle_numbers = get_triangle_numbers()
    square_numbers = get_square_numbers()
    pentagonal_numbers = get_pentagonal_numbers()
    hexagonal_numbers = get_hexagonal_numbers()
    heptagonal_numbers = get_heptagonal_numbers()
    octagonal_numbers = get_octagonal_numbers()

    # Find chain
    works3_4 = check_lists(triangle_numbers, square_numbers)
    works4_5 = check_lists(list_of_tuples_to_list(works3_4), pentagonal_numbers)
    works5_6 = check_lists(list_of_tuples_to_list(works4_5), hexagonal_numbers)
    works6_7 = check_lists(list_of_tuples_to_list(works5_6), heptagonal_numbers)
    works7_8 = check_lists(list_of_tuples_to_list(works6_7), octagonal_numbers)

    # Check numbers loop
    works8_3 = 0

    # Find Chain
    num8 = works8_3[0][0]
    num7 = find_previous_link(num8, works7_8)
    num6 = find_previous_link(num7, works6_7)
    num5 = find_previous_link(num6, works5_6)
    num4 = find_previous_link(num5, works4_5)
    num3 = find_previous_link(num4, works3_4)

    nums = [num3, num4, num5, num6, num7, num8]
    print(nums)
    return sum(nums)





print(main())

# [8256, 5625, 2512, 1281, 8128, 2882]
