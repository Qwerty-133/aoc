import itertools
import functools
import operator
from pathlib import Path

input_file_name = Path(__file__).with_suffix('.txt').name
with open(Path('2020/inputs') / input_file_name) as f:
    data = list(map(int, f.read().split()))


def sum_to_2020(nums, count):
    return next(functools.reduce(operator.mul, nums)
                for nums in itertools.combinations(nums, count)
                if sum(nums) == 2020)


print(sum_to_2020(data, 2))

# Part Two

print(sum_to_2020(data, 3))
