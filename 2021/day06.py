from time import time
from pprint import pprint

start = time()


with open("day06input.txt", "r") as file_in:
    lanternfish = [int(x) for x in file_in.readline().split(",")]
    catalog = dict()
    for i in range(0, 9):
        catalog[i] = 0
    for fish in lanternfish:
        catalog[fish] += 1

print(catalog)


def part_one():
    global lanternfish
    days = 0
    while (days < 80):
        days += 1
        new_fish = list()
        old_fish = list()
        for fish in lanternfish:
            if fish == 0:
                old_fish.append(6)
                new_fish.append(8)
            else:
                old_fish.append(fish - 1)
        lanternfish = old_fish + new_fish
        # print(lanternfish)
    return(len(lanternfish))


def part_two():
    days = 0
    while (days < 256):
        days += 1
        zeroes = catalog[0]
        for age in catalog.keys():
            if age:
                catalog[age-1] = catalog[age]
        catalog[8] = zeroes
        catalog[6] += zeroes
    return sum(catalog.values())


first = time()
print(part_one())
print("part one computed in " + str(time() - first) + " seconds")
second = time()
print(part_two())
print("part two computed in " + str(time() - second) + " seconds")

print("completely computed in " + str(time() - start) + " seconds")
