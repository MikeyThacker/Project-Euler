from fractions import Fraction


def main():
    answer, temp = 0, Fraction(1, 2)

    for _ in range(1000):
        temp = Fraction(1, 2 + temp)
        expansion = temp + 1
        numerator, denominator = expansion.numerator, expansion.denominator
        if len(str(numerator)) > len(str(denominator)):
            answer += 1
            print(expansion)
    return answer


print(main())
