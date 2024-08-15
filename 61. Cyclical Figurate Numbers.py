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
    for x in all_nums:
        dictionary[x] = []
        for y in all_nums:
            if x[0] != y[0] and x[1] != y[1]:
                if check_property(x[0], y[0]):
                    dictionary[x].append(y)

    return dictionary


def find_route(all_nums, connections):
    # TODO Step 3: https://www.ivl-projecteuler.com/overview-of-problems/20-difficulty/problem-61
    for a in all_nums:
        if a[1] != 8:
            continue

        for b in connections[a]:
            for c in connections[b]:
                for d in connections[c]:
                    for e in connections[d]:
                        for f in connections[e]:
                            if a in connections[f]:

                                if len(set([a[1], b[1], c[1], d[1], e[1], f[1]])) == 6:
                                    return [a, b, c, d, e, f]


def main():
    all_nums = get_nums()
    connections = get_connections(all_nums)
    solution = find_route(all_nums, connections)
    solution = [x[0] for x in solution]
    print(solution)

    return sum(solution)


print(main())

# [8256, 5625, 2512, 1281, 8128, 2882]
