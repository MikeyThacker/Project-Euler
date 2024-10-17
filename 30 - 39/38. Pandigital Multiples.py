def check_pandigital(num):
    if len(num) != 9:
        return False

    digits = [0 for _ in range(9)]
    correct_digits = [1 for _ in range(9)]
    for digit in num:
        digits[int(digit) - 1] += 1

    if digits == correct_digits:
        return True
    return False


def get_pandigital(num):
    concatenated_product = ""
    n = 0
    while True:
        n += 1
        concatenated_product += str(num * n)
        if check_pandigital(concatenated_product):
            return int(concatenated_product)
        if len(concatenated_product) > 9:
            break
    return 0


def main():
    largest_pandigital = 0
    for i in range(99999):
        largest_pandigital = max(get_pandigital(i), largest_pandigital)
    return largest_pandigital


print(main())
