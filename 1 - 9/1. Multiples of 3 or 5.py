def main():
    multiples = []
    for i in range(1000):
        if is_multiple_of_3_or_5(i):
            multiples.append(i)
    sum = sum_of_list(multiples)
    print(sum)


def is_multiple_of_3_or_5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    return False


def sum_of_list(list):
    return sum(list)


main()
