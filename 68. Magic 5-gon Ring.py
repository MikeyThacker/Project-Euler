from itertools import permutations


def split_set(current_set):
    # Current set = [a, b, c, x, y, z]
    # n -> n-gon ring
    n = len(current_set) // 2
    # Split set = inner, outer
    # Inner = [a, b, c]
    # Outer = [x, y, z]
    inner = [_ for _ in current_set[:n]]
    outer = [_ for _ in current_set[n:]]
    return inner, outer


def create_set(permutation):
    # Current set = [a, b, c, x, y, z]
    check_total = 0
    x = len(permutation) // 2  # Current shape is x-gon
    inner, outer = split_set(permutation)

    current_set = []
    for pos, digit in enumerate(outer):
        current_set.append([digit, inner[(pos + 1) % x], inner[(pos + 2) % x]])
    return current_set


def check_set(current_set):
    sums = [sum(triple) for triple in current_set]
    return sums.count(sums[0]) == len(sums) and check_lowest_node(current_set) and check_16_digits(current_set)

def check_16_digits(current_set):
    total = ""
    for triple in current_set:
        for num in triple:
            total += str(num)
    return len(total) == 16


def list_to_str(current_set):
    total = ""
    for triple in current_set:
        for num in triple:
            total += str(num)
    return total

def check_lowest_node(current_set):
    #Check that the set stars at the lowest external node
    start = current_set[0][0]
    for triple in current_set:
        if triple[0] < start:
            return False
    return True


def main():
    """
    e.g. for a 3-gon ring
               y
              /
    x - a  – b
         \  /
          c
           \
            z
    nodes = [a, b, c, x, y, x]
    """
    all_nums = [i + 1 for i in range(10)]
    perms = [list(_) for _ in permutations(all_nums)]

    largest_string = 0

    for perm in perms:
        current_set = create_set(perm)
        if check_set(current_set):
            largest_string = max(largest_string, int(list_to_str(current_set)))
    return largest_string


print(main())
