def get_repeating_part(decimal, remainders):
    end = remainders[-1]
    for remainder in remainders:
        if remainder == end:
            return (len(remainders) - 1) - remainders.index(remainder)


def get_len(num):
    A = 10
    B = num

    dec = "0."
    remainders = []  # remainders in same order as in decimal

    while True:
        if A < B:
            A *= 10
            dec += "0"
            remainders.append(-1)  # -number signifies remainder smaller than B

        remainder = A % B

        multiple = A - remainder
        A = remainder * 10
        dec += f"{multiple // B}"

        if remainder == 0:
            return 0

        # Remainder used - cycle reached
        if remainder in remainders:
            remainders.append(remainder)
            return get_repeating_part(dec, remainders)
        remainders.append(remainder)


def main():
    longest_recursion = 0
    for i in range(2, 1_000):
        len_recursion = get_len(i)
        longest_recursion = max(len_recursion, longest_recursion)
        if longest_recursion == len_recursion:
            answer = i
        print(f"{i}: {len_recursion}")

    return answer


print(main())
