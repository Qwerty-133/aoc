import re
from pathlib import Path

file = Path('inputs/day03.txt')


def generate(wire):
    instructions = wire.split(',')
    x = y = 0
    increments = {
        'R': (1, 0),
        'D': (0, -1),
        'L': (-1, 0),
        'U': (0, 1)
    }
    coords = []

    for instruction in instructions:
        direction, magn = re.search('(.)(.*)', instruction).groups()
        for _ in range(int(magn)):
            a, b = increments[direction]
            x += a
            y += b
            coords.append((x, y))

    return coords


with open(file) as f:
    w1, w2 = f.read().splitlines()
    gen_1 = generate(w1)
    gen_2 = generate(w2)
    intersected = set(gen_1).intersection(gen_2)

    print(min(abs(x) + abs(y) for x, y in intersected))
    print(min(gen_1.index(c) + gen_2.index(c) for c in intersected) + 2)
