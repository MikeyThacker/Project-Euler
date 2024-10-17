def main():
    """
    sum_sums = list where index is n,
        value stored is list of length of sum with starting digit = (n - index)
    e.g., sum_sums[9] = [1, 2, 3, 5, 7, 9, 5, 1], n = 10

    counts = list where nth term is number of ways to express n as a sum
    """

    sum_sums = [[], [], [1], [1, 1], [1, 2, 1], [1, 2, 2, 1]]  # 0 to 5 already filled in
    counts = [0, 0, 1, 2, 4, 6]  # //, No ways to make 0 and 1

    for n in range(6, 101):
        this_count = 0

        # Add previous counts from 1 to n/2
        numbers_to_add = counts[1:(n // 2) + 1]
        numbers_to_add = [number + 1 for number in numbers_to_add]

        # Add counts from n//2 to n
        for start_digit in range((n - 1) // 2, 0, -1):
            to_add = sum_sums[n - start_digit][-start_digit:]
            numbers_to_add.append(sum(to_add))

        # Add this n and its sums to "records"
        sum_sums.append(numbers_to_add)
        counts.append(sum(numbers_to_add))
    return counts[-1]


print(main())
