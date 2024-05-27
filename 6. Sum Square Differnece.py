def main():
    list = make_list(100)
    sum_of_squares = get_sum_of_squares(list)
    square_of_sum = get_square_of_sum(list)
    return square_of_sum - sum_of_squares


def get_sum_of_squares(list):
    square_list = []
    for num in list:
        square_list.append(num ** 2)
    return sum_of_list(square_list)


def get_square_of_sum(list):
    sum = sum_of_list(list)
    return sum ** 2


def sum_of_list(list):
    return sum(list)


def make_list(max):
    list = []
    for i in range(1, max + 1):
        list.append(i)
    return list


print(main())
