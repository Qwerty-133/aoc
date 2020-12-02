import re
from pathlib import Path

input_file_name = Path(__file__).with_suffix('.txt').name
with open(Path('2020/inputs') / input_file_name) as f:
    data = []
    for line in f:
        match = re.search(r'(\d+)-(\d+) (\w): (\w*)',  line.rstrip())
        data.append(match)


def func(thing):
    return int(thing[1]) <= thing[4].count(thing[3]) <= int(thing[2])


print(sum(map(func, data)))

# Part Two


def new_func(thing):
    # print(data)
    *_, char, string = thing.groups()
    return (string[int(thing[1])-1] == char) \
        + (string[int(thing[2])-1] == char) == 1


print(sum(map(new_func, data)))
