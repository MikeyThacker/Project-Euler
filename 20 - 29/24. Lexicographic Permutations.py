from itertools import permutations


def get_permutations():
    return list(permutations(range(0, 10)))


def main():
    permutations = get_permutations()
    permutations_as_integers = []
    for permutation in permutations:
        num = ""
        for digit in permutation:
            num += str(digit)
        num = int(num)
        permutations_as_integers.append(num)
    permutations_as_integers.sort()
    return permutations_as_integers[1_000_000 - 1]


print(main())
