import re
from pathlib import Path


def validate(password, pattern):
    num_str = str(password)

    if len(num_str) != 6:
        return False

    if not re.search(pattern, num_str):
        return False

    curr = 0
    for dig in num_str:
        int_dig = int(dig)
        if curr > int_dig:
            return False
        curr = int_dig

    return True


with open(Path('inputs/day04.txt')) as f:
    lower, upper = (int(num) for num in f.read().rstrip().split('-'))

    print(sum(validate(password, r'(\d)\1')
              for password in range(lower, upper+1)))

    print(sum(validate(password, r'(\d)(?<!\1\1)\1(?!\1)')
              for password in range(lower, upper+1)))
