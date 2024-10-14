from math import factorial

def digit_factorial(n):
    return sum([factorial(int(digit)) for digit in str(n)])

def get_len_chain(n, all_chain_lengths):
    og_n = n
    used_nums = set([])

    while n not in used_nums:
        if n in all_chain_lengths:
            used_nums.update(all_chain_lengths[n])
            all_chain_lengths[og_n] = used_nums
            return len(used_nums), all_chain_lengths

        used_nums.add(n)
        n = digit_factorial(n)

    all_chain_lengths[og_n] = used_nums
    return len(used_nums), all_chain_lengths


def main():
    n_max= 1_000_000
    count = 0

    all_chain_lengths = {}

    for n in range(1, n_max + 1):

        chain_length , all_chain_lengths = get_len_chain(n, all_chain_lengths)
        if chain_length == 60:
            count += 1

        print(n, chain_length, all_chain_lengths[n])
    return count

print(main())