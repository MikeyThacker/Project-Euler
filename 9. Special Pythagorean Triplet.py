from math import *


def main():
    square_numbers = get_square_numbers()
    pythagorean_triples = get_pythagorean_triples(square_numbers)
    target_triplet = find_sum_1000(pythagorean_triples)
    return multiply(target_triplet)



def get_square_numbers():
    return [i**2 for i in range(1, 1000)]


def get_pythagorean_triples(squares):
    triples = []
    for squareA in squares:
        for squareB in squares:
            if squareA + squareB in squares:
                A = int(sqrt(squareA))
                B = int(sqrt(squareB))
                C = int(sqrt(squareA + squareB))
                triples.append([A, B, C])
        squares = squares[1:]
    return triples


def find_sum_1000(triples):
    for triple in triples:
        if sum(triple) == 1000:
            return triple


def multiply(triple):
    return prod(triple)


print(main())
