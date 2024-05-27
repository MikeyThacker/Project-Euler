def main():
    sum = 0
    for i in range(1, 1001):
        sum += i**i
    return str(sum)[-10:]


print(main())
