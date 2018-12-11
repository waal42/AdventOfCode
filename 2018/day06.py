from time import time
from pprint import pprint

start = time()
coordinates = dict()

with open("day06input.txt") as fin:
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
        coordinates[i]["closest"] = list()


def part_one():
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            distance = float("inf")
            occurances = 0
            closest = 0
            for i in coordinates.keys():
                this_distance = abs(x - coordinates[i]["coords"][0]) + abs(
                    y - coordinates[i]["coords"][1]
                )
                if this_distance == distance:
                    occurances += 1
                    closest = 0
                elif this_distance < distance:
                    distance = this_distance
                    occurances = 1
                    closest = i
            if closest in coordinates.keys():
                coordinates[closest]["closest"].append((x, y))
                if x == min_x or x == max_x or y == min_y or y == max_y:
                    coordinates[closest]["border"] = True
    print(min_x, min_y)
    print(max_x, max_y)
    most_closest_number = 0
    for i in coordinates.keys():
        if coordinates[i]["border"] == False:
            if len(coordinates[i]["closest"]) > most_closest_number:
                most_closest_number = len(coordinates[i]["closest"])
    print("largest area is " + str(most_closest_number))


def part_two():
    # safe = list()
    safe = 0
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            cummulative_distance = 0
            for i in coordinates.keys():
                cummulative_distance += abs(x - coordinates[i]["coords"][0]) + abs(
                    y - coordinates[i]["coords"][1]
                )
            if cummulative_distance < 10000:
                # safe.append((x, y))
                safe += 1
    # print("safe area is " + str(len(safe)))
    print("safe area is " + str(safe))


part_one()
part_two()


print("computed in " + str(time() - start) + " seconds")
