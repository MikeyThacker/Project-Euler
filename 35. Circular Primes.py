from math import *


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def next_rotation(num):
    num = str(num)
    num = num[1:] + num[0]
    return int(num)


def is_circular_prime(original, num_digits):
    num = str(next_rotation(original)).zfill(num_digits)
    while int(num) != original:
        if not is_prime(int(num)):
            return False
        num = str(next_rotation(num)).zfill(num_digits)
    return True


def main():
    circular_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
    count = 13  # Number of circular primes
    for num in range(101, 1_000_000, 2):
        if "0" in str(num) or "2" in str(num) or "4" in str(num) or "6" in str(num) or "8" in str(num):
            continue
        if is_prime(num):
            if is_circular_prime(num, len(str(num))):
                count += 1
    return count


print(main())
