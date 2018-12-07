from time import time
from pprint import pprint

start = time()
coordinates = dict()

with open("day06testinput.txt") as fin:
    i = 1
    min_x = 1000
    min_y = 1000
    max_x = 0
    max_y = 0
    for line in fin.read().strip().split("\n"):
        coordinates[i] = {"coords": tuple([int(x) for x in line.split(", ")])}
        this_x, this_y = coordinates[i]["coords"][0], coordinates[i]["coords"][1]
        min_x = min(min_x, this_x)
        min_y = min(min_y, this_y)
        max_x = max(max_x, this_x)
        max_y = max(max_y, this_y)
        i += 1
    for i in coordinates.keys():
        this_x, this_y = coordinates[i]["coords"][0], coordinates[i]["coords"][1]
        if this_x == min_x or this_x == max_x or this_y == min_y or this_y == max_y:
            coordinates[i]["border"] = True
        else:
            coordinates[i]["border"] = False

# def part_one():


print("computed in " + str(time() - start) + " seconds")
