from statistics import *
from math import *


def get_hypotenuse(a, b):
    hypotenuse = a ** 2
    hypotenuse += b ** 2
    hypotenuse = sqrt(hypotenuse)
    return hypotenuse


def get_triples():
    triples = []
    for a in range(1, 998):
        for b in range(a, 998):
            c = get_hypotenuse(a, b)
            if int(c) != c:
                continue
            triples.append([a, b, int(c)])
    return triples


def main():
    triples = get_triples()

    sums = []
    for triple in triples:
        p = sum(triple)
        if p < 1001:
            sums.append(p)
    return mode(sums)


print(main())
