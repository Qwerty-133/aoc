from pathlib import Path
with open(Path('inputs/day1.txt')) as f:
    masses = [int(mass) for mass in f.read().splitlines()]


def fuel(mass):
    return mass//3 - 2


print(sum(fuel(mass) for mass in masses))

# Part Two

total_fuel = 0

for mass in masses:
    while True:
        curr_fuel = fuel(mass)
        if curr_fuel > 0:
            total_fuel += curr_fuel
            mass = curr_fuel
        else:
            break


print(total_fuel)
