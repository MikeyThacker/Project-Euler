from itertools import count

def get_primes(MAX):
    all_nums = [True] * MAX
    all_nums[0] = False
    all_nums[1] = False

    for num in range(MAX):
        if all_nums[num]:
            for factor in count(2):
                multiple = factor * num
                if multiple >= MAX:
                    break
                all_nums[multiple] = False
    primes = [number for number, state in enumerate(all_nums) if state]
    return primes

def make_num(n, primes, count):
    usable_primes = [prime for prime in primes if prime <= n]

    for prime in usable_primes:
        if n - prime < 0:
            return 0
        elif n - prime == 0:
            count += 1
            return count
        count = make_num(n-prime, primes[1:], count)


def main():
    n = 9
    index = 0 # Index of first prime
    primes = get_primes(5000)

    while True:
        n += 1
        usable_primes = [prime for prime in primes if prime < n]
        usable_primes.reverse()
        count = make_num(n,usable_primes, 0)



print(main())