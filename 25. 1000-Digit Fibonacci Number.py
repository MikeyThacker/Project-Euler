def next_number(n1, n2):
    return n1 + n2


def fibonacci(n1, n2):
    index = 2
    while True:
        if len(str(n2)) > 999:
            return index
        n1, n2 = n2, next_number(n1, n2)
        index += 1


def main():
    return fibonacci(1, 1)


print(main())
