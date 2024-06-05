from math import *


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0 and i != num:
            return False
    return True


def check_numbers(num1: int, num2: int) -> bool:
    one_plus_two = int(str(num1) + str(num2))
    two_plus_one = int(str(num2) + str(num1))
    return is_prime(one_plus_two) and is_prime(two_plus_one)


def main() -> int:
    max_search = 10_000
    for p1 in (x for x in range(3, max_search) if is_prime(x)):
        for p2 in (x for x in range(3, max_search) if is_prime(x)):

            # Check first two numbers
            if p1 == p2 or not check_numbers(p1, p2):
                continue

            for p3 in (x for x in range(3, max_search) if is_prime(x)):

                # Check third number
                if p1 == p3 or not (check_numbers(p1, p3) and check_numbers(p2, p3)):
                    continue

                for p4 in (x for x in range(3, max_search) if is_prime(x)):
                    # Check fourth number
                    if p1 == p4 or not (check_numbers(p1, p4) and check_numbers(p2, p4) and check_numbers(p3, p4)):
                        continue

                    for p5 in (x for x in range(3, max_search) if is_prime(x)):
                        # Check fifth number
                        if p1 == p4 or not (check_numbers(p1, p5) and check_numbers(p2, p5) and check_numbers(p3,
                                                                                                              p5) and check_numbers(
                            p4, p5)):
                            continue

                        print([p1, p2, p3, p4, p5])
                        return p1 + p2 + p3 + p4 + p5


print(main())
