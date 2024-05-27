def num_as_list(num):
    num = str(num)

    num_as_list = []
    for digit in num:
        num_as_list.append(int(digit))
    return num_as_list


def is_same(num1, num2, num3, num4, num5, num6):
    num1 = num_as_list(num1)
    num2 = num_as_list(num2)
    num3 = num_as_list(num3)
    num4 = num_as_list(num4)
    num5 = num_as_list(num5)
    num6 = num_as_list(num6)

    num1.sort()
    num2.sort()
    num3.sort()
    num4.sort()
    num5.sort()
    num6.sort()

    return num1 == num2 == num3 == num4 == num5 == num6


def main():
    x = 0
    while True:
        x += 1
        x2 = 2 * x
        x3 = 3 * x
        x4 = 4 * x
        x5 = 5 * x
        x6 = 6 * x

        if is_same(x, x2, x3, x4, x5, x6):
            return x


print(main())
