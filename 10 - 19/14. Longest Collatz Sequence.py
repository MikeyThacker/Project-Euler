def collatz(num):
    steps = 1
    while num != 1:
        steps += 1

        if num % 2 == 0:
            num /= 2
        else:
            num = (3 * num) + 1
    return steps


def main():
    greatest_chain = 0
    GC_number = 0
    for i in range(1, 1_000_001):
        print(i)
        steps = collatz(i)
        if steps > greatest_chain:
            greatest_chain = steps
            GC_number = i
    return GC_number


print(main())
