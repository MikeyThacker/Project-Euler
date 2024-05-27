def is_sum_powers(num):
    sum = 0
    for digit in str(num):
        digit = int(digit)
        sum += digit ** 5
        if sum > num:
            return False
    if sum == num:
        return True
    return False


def main():
    num = 1
    works = []
    while num < 999_999:
        num += 1
        if is_sum_powers(num):
            works.append(num)
    return sum(works)

print(main())

