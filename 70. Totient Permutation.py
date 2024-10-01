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


def is_permutation(num1, num2):
    if sorted(str(num1)) == sorted(str(num2)):
        return True
    return False


def main():
    permutations = []
    primes = get_primes(10 ** 5)

    # Number is prime
    # phi() of a prime number will always be 1 less than that number
    # This can never be a permutation so skip
    # Numbers with small amounts of large prime factors produce smaller ratio values

    # Used https://martin-ueding.de/posts/project-euler-solution-70-totient-permutation/ to help narrow down possibilities
    # Was never going to finish in one sitting

    for prime1 in primes:
        for prime2 in primes:
            if prime1 == prime2:
                break
            product = prime1 * prime2
            if product > 10 ** 7:
                break
            totient = (prime1 - 1) * (prime2 - 1)
            if is_permutation(totient, product):
                permutations.append([product / totient, product])

    return min(permutations)[1]


print(main())
