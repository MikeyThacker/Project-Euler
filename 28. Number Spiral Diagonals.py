def main():
    num = 1
    diagonals = [1]
    for num_to_add in range(2, 1001, 2):
        for _ in range(4):
            num += num_to_add
            diagonals.append(num)
    return sum(diagonals)


print(main())
