from math import *


def is_pentagonal(n): return (1 + sqrt(1 + 24 * n)) % 6 == 0


def get_pentagonal(n): return n * ((3 * n) - 1) // 2


def main():
    i = 0
    while True:
        i += 1
        num1 = get_pentagonal(i)

        for j in range(1, i):
            num2 = get_pentagonal(j)

            if is_pentagonal(num1 + num2) and is_pentagonal(num1 - num2):
                return num1 - num2


print(main())
