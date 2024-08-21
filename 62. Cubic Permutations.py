from itertools import permutations
from math import cbrt


def is_cube_root(num):
    root = cbrt(num)
    return root % 1 == 0


def get_permutations(num):
    perms = [int(''.join(p)) for p in permutations(str(num))]  # Get Permutations
    perms = list(set(perms))  # Remove Duplicates (if any)
    perms = [x for x in perms if x >= num]  # Remove any numbers smaller, as any cubes have already been checked
    return perms


def check_num_cubes(perms):
    is_roots = [is_cube_root(num) for num in perms]
    if is_roots.count(True) == 4:
        return True
    return False


def main():
    x = 1  # Number to Cube
    while True:
        x += 1
        print(x)
        y = x ** 3  # Cube to Check permutations of
        perms = get_permutations(y)
        if check_num_cubes(perms):
            return y


print(main())
