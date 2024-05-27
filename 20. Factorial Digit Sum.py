def sum_of_digits(num):
    num = str(num)
    sum = 0
    for digit in num:
        sum += int(digit)
    return sum


def main():
    product = 1
    for i in range(100, 1, -1):
        product *= i
    return sum_of_digits(product)


print(main())
