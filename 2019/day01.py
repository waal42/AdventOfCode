from time import time
from math import floor

start = time()

with open("day01input.txt", "r") as file_in:
    masses = [int(x) for x in file_in.read().rstrip().split("\n")]

def part_one():
    total = 0
    for mass in masses:
        total += floor(mass/3)-2
    print(total)

# part_one()

def part_two():
    total = 0
    for mass in masses:
        total_replacement = 0
        replacement = 1
        while (replacement > 0):
            replacement = floor(mass/3)-2
            if replacement > 0:
                total_replacement += replacement
                mass = replacement
        total += total_replacement
    print(total)
        
part_two()



print("computed in " + str(time() - start) + " seconds")
