def digit_sum(num):
    num = str(num)

    sum = 0
    for digit in num:
        sum += int(digit)
    return sum


def main():
    highest_sum = 0

    for a in range(2, 100):
        for b in range(1, 100):
            highest_sum = max(highest_sum, digit_sum(a ** b))
    return highest_sum


print(main())
