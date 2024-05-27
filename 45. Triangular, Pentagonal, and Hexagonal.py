from math import *


def get_triangle(n): return (n * (n + 1)) // 2


def is_pentagonal(n): return (1 + sqrt(1 + 24 * n)) % 6 == 0


def is_hexagonal(n): return (1 + sqrt(1 + 8 * n)) % 4 == 0


def main():
    i = 285
    while True:
        i += 1
        num = get_triangle(i)
        if is_pentagonal(num) and is_hexagonal(num):
            return num


print(main())
