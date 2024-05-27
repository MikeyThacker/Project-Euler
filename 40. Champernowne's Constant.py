def main():
    number = "0."
    i = 0

    while len(number) < 1_000_000:
        i += 1
        number += str(i)
    i += 1
    number += str(i)
    number = number[2:]
    d1 = int(number[0])
    d10 = int(number[9])
    d100 = int(number[99])
    d1000 = int(number[999])
    d10000 = int(number[9_999])
    d100000 = int(number[99_999])
    d1000000 = int(number[999_999])

    return d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000


print(main())
