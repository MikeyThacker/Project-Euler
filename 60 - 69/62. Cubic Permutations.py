def main():
    x = 0  # Number to Cube
    cubes = []  # List of cubes with digits sorted
    while True:
        print(x)

        cube = sorted(str(x ** 3))
        cubes.append(cube)

        if cubes.count(cube) == 5:
            return (cubes.index(cube)) ** 3  # Index is cube root of first number with that series of digits

        x += 1


print(main())

# Answer: 5027^3 , 127,035,954,683
