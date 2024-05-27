def get_factorial(num):
    product = 1
    for i in range(num, 1, -1):
        product *= i
    return product


def main():
    valid_nums = []
    for i in range(3, 99_999):
        running_sum = 0
        for digit in str(i):
            if running_sum > i:
                break
            running_sum += get_factorial(int(digit))
        if running_sum == i:
            valid_nums.append(i)

    return sum(valid_nums)


print(main())
