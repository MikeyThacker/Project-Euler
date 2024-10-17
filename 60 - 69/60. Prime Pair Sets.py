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
    for prime1 in (x for x in range(3, max_search) if is_prime(x)):
        for prime2 in (x for x in range(3, max_search) if is_prime(x)):

            # Check first two numbers
            if prime1 == prime2 or not check_numbers(prime1, prime2):
                continue

            for prime3 in (x for x in range(3, max_search) if is_prime(x)):

                # Check third number
                if prime1 == prime3 or not (check_numbers(prime1, prime3) and check_numbers(prime2, prime3)):
                    continue

                for prime4 in (x for x in range(3, max_search) if is_prime(x)):
                    # Check fourth number
                    if prime1 == prime4 or not (
                            check_numbers(prime1, prime4) and check_numbers(prime2, prime4) and check_numbers(prime3,
                                                                                                              prime4)):
                        continue

                    for prime5 in (x for x in range(3, max_search) if is_prime(x)):
                        # Check fifth number
                        if prime1 == prime4 or not (
                                check_numbers(prime1, prime5) and check_numbers(prime2, prime5) and check_numbers(
                                prime3,
                                prime5) and check_numbers(
                            prime4, prime5)):
                            continue

                        print([prime1, prime2, prime3, prime4, prime5])
                        return prime1 + prime2 + prime3 + prime4 + prime5


print(main())
