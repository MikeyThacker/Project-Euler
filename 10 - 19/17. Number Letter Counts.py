def six():
    return 3


def seven():
    return 5


def eight():
    return 5


def nine():
    return 4


def ten():
    return 3


def eleven():
    return 6


def twelve():
    return 6


def thirteen():
    return 8


def fourteen():
    return 8


def fifteen():
    return 7


def sixteen():
    return 7


def seventeen():
    return 9


def eighteen():
    return 8


def nineteen():
    return 8


def twenty():
    return 6


def thirty():
    return 6


def forty():
    return 5


def fifty():
    return 5


def sixty():
    return 5


def seventy():
    return 7


def eighty():
    return 6


def ninety():
    return 6


def hundred():
    return 7


def And():
    return 3


def one_thousand():
    return 11


def main():
    count = 19
    # Get count of 1 to 19
    count += six()
    count += seven()
    count += eight()
    count += nine()
    one_to_nine = count

    count += ten()
    count += eleven()
    count += twelve()
    count += thirteen()
    count += fourteen()
    count += fifteen()
    count += sixteen()
    count += seventeen()
    count += eighteen()
    count += nineteen()

    count += 10 * twenty()
    count += 10 * thirty()
    count += 10 * forty()
    count += 10 * fifty()
    count += 10 * sixty()
    count += 10 * seventy()
    count += 10 * eighty()
    count += 10 * ninety()

    one_to_ninety_nine = count + (8 * one_to_nine)
    count += (9 * one_to_ninety_nine)

    # All instances of (1-9) hundred
    count += 100 * (one_to_nine + (9 * hundred()))

    # All ands - numbers after 100 excluding multiples of
    count += (9 * 99 * And())

    count += one_thousand()

    return count


print(main())
