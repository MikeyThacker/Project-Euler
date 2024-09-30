from math import *


def phi(n):
    count = 1
    for i in range(2, n):
        if lcm(n, i) == n * i:
            count += 1
    return count


def main():
    for n in range(1, 10 ** 7):
        print(f"{n}: {phi(n)}")


print(main())
