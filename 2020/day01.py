import itertools

from pathlib import Path

input_file_name = Path(__file__).with_suffix('.txt').name
with open(Path('2020/inputs') / input_file_name) as f:
    data = list(map(int, f.read().split()))


def func(nums):
    for num, num2 in itertools.combinations(nums, 2):
        if num + num2 == 2020:
            return num * num2


print(func(data))

# Part Two


def three(nums):
    for num, num2, num3 in itertools.combinations(nums, 3):
        if num + num2 + num3 == 2020:
            return num * num2 * num3


print(three(data))
