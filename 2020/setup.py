import pathlib

_2020 = pathlib.Path('2020')

try:
    latest_day = max(_2020.glob('day??.py'))
    new_day = int(latest_day.stem[-2:]) + 1
except ValueError:
    # No days yet
    new_day = 1

code = """\
from pathlib import Path

input_file_name =  Path(__file__).with_suffix('.txt').name
with open(Path('2020/inputs') / input_file_name) as f:
    f.read()


def func():
    pass


# Part Two
"""

new_day_file_name = f'day{new_day:02}'

# Create input file
with open(_2020 / f'inputs/{new_day_file_name}.txt', 'w') as f:
    pass


with open(_2020 / f'{ new_day_file_name}.py', 'w') as f:
    f.write(code)
