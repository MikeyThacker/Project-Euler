def is_pandigital(numbers):
    # Numbers: List of [Multiplicand, Multiplier, Product]
    digits = [0 for _ in range(9)]
    for number in numbers:
        num_as_string = str(number)
        for digit in num_as_string:
            if digit == "0":
                return False
            digits[int(digit) - 1] += 1
    if digits == [1 for _ in range(9)]:
        return True
    return False


def main():
    pandigital_products = set([])
    for i in range(1, 9999):
        print(f"Current: {i}, Left: {9999 - i}")
        for j in range(1, 99):
            product = i * j
            if is_pandigital([i, j, product]):
                pandigital_products.add(product)

    pandigital_products = sorted(pandigital_products)

    return sum(pandigital_products)


print(main())
