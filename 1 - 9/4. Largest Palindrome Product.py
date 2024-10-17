def main():
    largest_palindrome = 0
    for a in range(11, 1000):
        for b in range(11, 1000):
            product = multiply(a, b)
            if is_palindrome(str(product)) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome


def multiply(a, b):
    return a * b


def is_palindrome(number_as_string):
    if number_as_string == number_as_string[::-1]:
        return True
    return False


print(main())
