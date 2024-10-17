def main():
    total = 0

    a = 1
    b = 2
    while b <= 4_000_000:
        if b % 2 == 0:
            total += b
        
        a, b = b, get_next_num(a,b)

    print(total)


def get_next_num(a, b):
    return a + b

main()