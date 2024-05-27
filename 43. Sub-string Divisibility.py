import itertools


def get_permutations():
    all_permutations = itertools.permutations([x for x in range(10)])
    permutations_as_int = []
    for permutation in all_permutations:
        number = ""
        for digit in permutation:
            number += str(digit)
        permutations_as_int.append(number)
    return permutations_as_int


def is_pandigital(num):
    digits = [0 for _ in range(len(num))]
    correct_digits = [1 for _ in range(len(num))]
    for digit in num:
        if int(digit) > len(num):
            return False
        digits[int(digit) - 1] += 1

    if digits == correct_digits:
        return True
    return False


def has_property(number):
    if len(number) == 9:
        number = "0" + number
    primes = [2, 3, 5, 7, 11, 13, 17]

    for start in range(1, 8):
        n1 = number[start]
        n2 = number[start + 1]
        n3 = number[start + 2]
        if int(n1 + n2 + n3) % primes[start - 1] != 0:
            return False
    return True


def main():
    permutations = get_permutations()
    sum = 0

    for number in permutations:
        if has_property(number):
            sum += int(number)

    return sum


print(main())
