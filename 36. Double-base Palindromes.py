def is_palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False


def main():
    sum = 0
    for num in range(1, 1_000_000, 2):
        if is_palindrome(num) and is_palindrome(bin(num)[2:]):
            sum += num
    return sum


print(main())
