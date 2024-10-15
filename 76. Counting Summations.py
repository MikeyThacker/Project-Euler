def get_natural_sum(n):
    """
    Returns sum of every natural number <= n

    Sum of natural numbers < n: n(n - 1)*0.5
    Sum of natural numbers <= n: n + n(n - 1)*0.5
        By rearranging:
            Sum = n(n + 1)*0.5
    """
    return n * (n + 1) * 0.5


def get_count(n, previous_count):
    return previous_count + get_natural_sum((n//2) - 1) + 1


def main():
    count = 6 # Count when n = 5
    for n in range(6, 101):
        count = get_count(n, count)
    return count


print(main())
