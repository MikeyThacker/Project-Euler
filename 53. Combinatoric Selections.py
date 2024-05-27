from math import *


def nCr(n, r):
    return (factorial(n)) // (factorial(r) * factorial(n - r))


def main():
    count = 0

    for n in range(23, 101):
        for r in range(2, n):
            if nCr(n, r) > 1_000_000:
                count += 1
    return count


print(main())
