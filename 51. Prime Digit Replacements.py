from math import *


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def has_three_repeated(num):
    num = str(num)

    digits_count = [0 for _ in range(10)]
    for digit in num:
        digit = int(digit)

        digits_count[digit] += 1
    return max(digits_count) > 2


def get_replacements(num):
    num = str(num)

    all_generated = []
    for replacing in [str(x) for x in range(10) if num.count(str(x)) > 1]:

        current_generated = []
        for replacement in [str(x) for x in range(10)]:
            current_generated.append(num.replace(replacing, replacement))
        all_generated.append(current_generated)
    return all_generated


def get_primes_in_list(l, primes):
    checked = [num for num in l]
    generated_primes = [num for num in l if int(num) in primes]
    return checked, generated_primes


def main(max_number=1_000_000):
    primes = [x for x in range(2, max_number) if is_prime(x) and has_three_repeated(x)]

    checked_nums = []

    for prime in primes:
        if prime in checked_nums:
            continue

        for list in get_replacements(prime):
            checked, generated_primes = get_primes_in_list(list, primes)

            if len(generated_primes) == 8:
                return generated_primes[0]

            for num in checked:
                checked_nums.append(num)


print(main())
