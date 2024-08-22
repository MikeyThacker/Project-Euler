def main():
    count = 0
    for x in range(1, 10):
        for y in range(1, 100):  # x^y where y is also number of digits
            num = x ** y
            length = len(str(num))

            if length > y:
                break
            if length == y:
                count += 1
    return count


print(main())

# x^3 when x = 10
# x^4 when x = 10
