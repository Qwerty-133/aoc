import itertools
from pathlib import Path

with open(Path('2019/inputs/day02.txt')) as f:
    intcode = [int(num) for num in f.read().split(',')]


def applyop(intcode, ads):
    int_copy = list(intcode)
    int_copy[1:3] = ads
    iter_ = iter(int_copy)
    for a, b, c, d in itertools.zip_longest(*(iter_ for _ in range(4))):
        if a == 99:
            return int_copy
        elif a == 1:
            int_copy[d] = int_copy[b] + int_copy[c]
        elif a == 2:
            int_copy[d] = int_copy[b] * int_copy[c]


def result(ad1, ad2):
    return applyop(intcode, (ad1, ad2))[0]


print(result(12, 2))

# Part Two

for ad1, ad2 in itertools.product(*(range(100) for _ in range(2))):
    if result(ad1, ad2) == 19690720:
        print(100 * ad1 + ad2)
        break
