def main():
    num = 2 ** 1000
    total = 0
    for n in str(num):
        total += int(n)
    return total


print(main())
