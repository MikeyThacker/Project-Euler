from math import *


def main():
    count = 0
    number = 0
    max_divisors = 0
    while True:
        count += 1
        number += count
        number_divisors = No_divisors(number)
        max_divisors = max(max_divisors, number_divisors)
        print(max_divisors)
        if number_divisors > 500:
            return number


def No_divisors(num):
    divisors = 2
    i = 2
    while i < ceil(sqrt(num)):
        if num % i == 0:
            # if i^2 = num, only add 1 divisor
            if i ** 2 == num:
                divisors += 1
            # if not, add 2 divisors
            else:
                divisors += 2
        i += 1
    return divisors


print(main())
