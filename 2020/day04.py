import re
from pathlib import Path

input_file_name = Path(__file__).with_suffix('.txt').name
with open(Path('2020/inputs') / input_file_name) as f:
    data = f.read()


def validate():
    thing = [a.replace('\n', ' ') for a in data.split('\n\n')]
    c = 0
    req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    for pass_ in thing:
        fields = re.findall(r'(\w+):[^ ]+', pass_)
        if len(req.intersection(fields)) < 7:
            continue
        c += 1

    print(c)


validate()

# Part Two


def validate_():
    thing = [a.replace('\n', ' ') for a in data.split('\n\n')]
    c = 0
    req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    def hgt(num):
        a, b = re.search(r'(\d+)(.*)', num).groups()
        a = int(a)
        if b == 'cm':
            return 150 <= a <= 193
        elif b == 'in':
            return 59 <= a <= 76
        return False

    conds = {
        'byr': lambda num: 1920 <= int(num) <= 2002,
        'iyr': lambda num: 2010 <= int(num) <= 2020,
        'eyr': lambda num: 2020 <= int(num) <= 2030,
        'hgt': hgt,
        'hcl': lambda num: bool(re.search(r'#[\da-f]{6}', num)),
        'ecl': lambda num: bool(re.search('amb|blu|brn|gry|grn|hzl|oth', num)),
        'pid': lambda num: len(num) == 9 and re.search(r'\d+', num)
    }

    for pass_ in thing:
        fields = re.findall(r'(\w+):[^ ]+', pass_)
        if len(req.intersection(fields)) < 7:
            continue
        maps = dict(re.findall(r'(\w+):([^ ]+)', pass_))
        for r, v in maps.items():
            if r != 'cid' and not conds[r](v):
                break
        else:
            c += 1

    print(c)


validate_()
