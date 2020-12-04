import functools
import operator
from pathlib import Path

input_file_name = Path(__file__).with_suffix('.txt').name
with open(Path('2020/inputs') / input_file_name) as f:
    data = f.readlines()


# def write():
#     with open(Path('2020/inputs') / input_file_name, 'w') as f:
#         for line in data:
#             f.write(line * 20)


# print(write())

# Part Two


def func2(slope):
    with open(Path('2020/inputs') / input_file_name) as f:
        f.readline()
        data = f.read().splitlines()
    count = 0
    for i, _ in enumerate(slope):
        try:
            count += 1 if data[i][_] == '#' else 0
        except IndexError:
            try:
                count += 1 if data[i][_ % len(data[i])] == '#' else 0
            except IndexError:
                break
    return count


a = [func2(range(1, 1000000, 1)), func2(range(3, 100000, 3)),
     func2(range(5, 100000, 5)), func2(range(7, 100000, 7))]


def func3(slope):
    with open(Path('2020/inputs') / input_file_name) as f:
        f.readline()
        f.readline()
        data = f.read().splitlines()
    count = 0
    for i, _ in enumerate(slope):
        try:
            count += 1 if data[2*i][_] == '#' else 0
        except IndexError:
            try:
                count += 1 if data[2*i][_ % len(data[2*i])] == '#' else 0
            except IndexError:
                break
    return count


a.append(func3(range(1, 1000000, 1)))

print(a)
print(functools.reduce(operator.mul, a))
