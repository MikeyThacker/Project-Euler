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


def get_prime_factors(n, primes, known_factors):
    original_n = n
    factors = []
    prime_index = 0

    if n in primes:
        factors.append(n)

        known_factors[original_n] = factors
        return known_factors

    while n != 1:

        prime = primes[prime_index]
        if n % prime == 0:
            factors.append(prime)
            n //= prime

            if n in known_factors:
                factors.extend(known_factors[n])

                known_factors[original_n] = factors
                return known_factors

            if n in primes:
                factors.append(n)

                known_factors[original_n] = factors
                return known_factors

        else:
            prime_index += 1

    known_factors[original_n] = factors
    return known_factors


def phi(factors):
    product = 1

    while len(factors) > 0:
        p = factors[0]
        k = factors.count(p)
        product *= (p ** (k - 1)) * (p - 1)
        factors = [factor for factor in factors if factor != p]
    return product


def main():
    """
    From wikipedia:
        "Farey sequence of order n is the sequence of completely reduced fractions,
        either between 0 and 1 [...] which have denominators less than or equal
         to n, arranged in order of increasing size"
        https://en.wikipedia.org/wiki/Farey_sequence

    The length of the sequence with the largest denominator of n is :
        |Fn| = 1 + sum( phi(x)) x = 1 -> n
    As I do not need to consider 0/1 and 1/1, x can start at 2
    """

    # Keep dictionary of prime factors to reference later so smaller numbers not being calculated lots of times
    known_factors = {}

    d = 1_000_000
    primes = get_primes(d)

    for x in range(2, d + 1):
        print(x)
        known_factors = get_prime_factors(x, primes, known_factors)

    count = sum([phi(factors) for factors in known_factors.values()])


    return count

print(main())

# Old Method
# 366663327241
# 325714454051
# 354256844782
# 377165084807
# 377164511818
# 303964043372
# 273877754256
# 303963043472
# 303964043372

# New Method
# 303963152391
# 303963552391

