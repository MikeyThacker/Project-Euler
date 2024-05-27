from math import *
from time import *


def is_abundant(n):
    if n == 4:
        return 3
    sum_divisors = 1

    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0 and (i != n / i):
            sum_divisors += i
            sum_divisors += n / i
    if sum_divisors > n:
        return True
    return False


def get_abundant_numbers():
    abundant_numbers = []
    for i in range(1, 28124 - 12):
        if is_abundant(i):
            abundant_numbers.append(i)
    return abundant_numbers


def get_non_abundant_sums(abundant_numbers):
    non_abundant_sums = [_ for _ in range(1, 28124)]
    while len(abundant_numbers) > 0:
        tic = time()
        num1 = abundant_numbers[0]

        for num2 in abundant_numbers:
            sum = num1 + num2
            try:
                non_abundant_sums.remove(sum)
            except ValueError:
                pass
        abundant_numbers.pop(0)

        toc = time()
        print(f"{num1}: {toc - tic}")

    return non_abundant_sums


def main():
    toc = time()
    abundant_numbers = get_abundant_numbers()
    non_abundant_sums = get_non_abundant_sums(abundant_numbers)
    tic = time()
    print(f"Total time: {tic - toc}")
    return sum(non_abundant_sums)


print(main())
