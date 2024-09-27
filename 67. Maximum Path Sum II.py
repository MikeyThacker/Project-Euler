def get_triangle():
    triangle = []
    with open("triangle.txt") as file:
        for line in file:
            line = line.split()
            triangle.append([int(num) for num in line])
    triangle.reverse()
    return triangle


def main():
    triangle = get_triangle()
    while len(triangle) > 1:
        row1 = triangle[0]
        row2 = triangle[1]
        new_row = []
        for index, item in enumerate(row2):
            num1 = item + row1[index]
            num2 = item + row1[index + 1]
            new_row.append(max(num1, num2))
        triangle = [new_row] + triangle[2:]
    return triangle[0][0]


print(main())
