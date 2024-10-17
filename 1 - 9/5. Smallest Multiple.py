def is_factor(a, b):
    if a % b == 0:
        return True
    return False


def find_factors(num):
    for i in range(1, 21):
        if not is_factor(num, i):
            return False
    return True


def main():
    num = 19
    while True:
        num += 1
        if find_factors(num):
            break
    return num


print(main())
