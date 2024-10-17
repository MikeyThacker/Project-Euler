from math import gcd
from math import sqrt, ceil


def get_lengths():
    """
        Use Euclid's formula:
            A Pythagorean triple can be generated using integers m and n.
            The triple comprises a, b, and c where:
                a = m^2 - n^2
                b = 2mn
                c = m^2 + n^2
            Where m and n are coprime and one is even.
        """

    lengths = [0] * 1_500_000

    # Generate Primitive Triples
    for m in range(2, ceil(sqrt(1_500_000))):
        for n in range(m % 2 + 1, m, 2):
            if gcd(m, n) != 1:
                continue

            # Get a, b, and c
            a = (m ** 2) - (n ** 2)
            b = 2 * m * n
            c = (m ** 2) + (n ** 2)

            length = a + b + c

            for k in range(1, (1_500_000 // length) + 1):
                if k * length > 1_500_000:
                    break
                lengths[(k * length) - 1] += 1

    return lengths


def main():
    # Get list of lengths where index - 1 is the length and the value held is the number of times it appears
    lengths = get_lengths()

    # Return number of lengths that appear once
    return lengths.count(1)


print(main())
