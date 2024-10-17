from math import *


def d(n):
    # Returns the sum of proper divisors of n
    sum_divisors = 1

    for i in range(2, ceil(sqrt(n))):
        if n % i == 0 and (i != n / i):
            sum_divisors += i
            d = n / i
            sum_divisors += d
    return sum_divisors


def main():
    divisor_sums = {}
    for i in range(2, 10_000):
        divisor_sum = d(i)
        divisor_sums[i] = divisor_sum

    amicable_sum = 0
    for item in divisor_sums:
        num1 = item
        num2 = divisor_sums[num1]
        try:
            if divisor_sums[num2] == num1 and num1 != num2:
                amicable_sum += num1
        except KeyError:
            continue
    return amicable_sum


print(main())
