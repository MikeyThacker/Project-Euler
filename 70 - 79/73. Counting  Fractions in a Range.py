from fractions import Fraction
from math import gcd

def middle_fraction(upper, lower):
    return (upper + lower) * Fraction(1,2)

def main():
    d = 12_000
    count = 0 # Number of fractions in range with denominator <= d

    upper = Fraction(1, 2)
    lower = Fraction(1, 3)

    for denominator in range(d, 4, -1):
        for numerator in range((denominator // 3) + 1, (denominator // 2) + 1):
            if gcd(numerator, denominator) != 1:
                # Fraction not in its simplest form, Ignore
                continue

            fraction = Fraction(numerator, denominator)

            if fraction >= upper or fraction <= lower:
                # Fraction not in range of 1/3 to 1/2
                continue

            print(fraction)
            count += 1
    return count



print(main())
