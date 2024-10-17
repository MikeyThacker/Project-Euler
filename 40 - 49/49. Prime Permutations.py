from math import *


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def is_permutations(num1, num2, num3):
    list1 = [digit for digit in str(num1)]
    list2 = [digit for digit in str(num2)]
    list3 = [digit for digit in str(num3)]

    list1.sort()
    list2.sort()
    list3.sort()

    return list1 == list2 and list2 == list3


def main():
    for num1 in range(1000, 6670):
        num2 = num1 + 3330
        num3 = num2 + 3330

        if not is_prime(num1) or not is_prime(num2) or not is_prime(num3):
            continue

        if num1 == 1487:
            continue

        if is_permutations(num1, num2, num3):
            return f"{num1}{num2}{num3}"


print(main())
