def is_palindrome(num):
    num = str(num)

    return num == num[::-1]


def get_reverse(num):
    return int(str(num)[::-1])


def is_lychrel(num):
    for _ in range(50):
        num += get_reverse(num)
        if is_palindrome(num):
            return False
    return True


def main():
    count = 0

    for i in range(10_000):
        if is_lychrel(i):  # If palindrome is reached:
            count += 1
    return count


print(main())
