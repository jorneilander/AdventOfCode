from math import floor
from os import chdir

chdir("./2019/Day 1 - The Tyranny of the Rocket Equation/")


def required_fuel(mass):
    fuel = (floor(int(mass)/3)-2)
    if fuel > 0:
        return fuel + required_fuel(fuel)
    return 0


with open("./input.txt", "r") as file:
    input = file.readlines()

print(sum(list(map(required_fuel, input))))
