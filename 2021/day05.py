from time import time
from copy import deepcopy
from typing import overload

start = time()

with open("day05input.txt", "r") as file_in:
    coords = list()
    for line in file_in.readlines():
        endpoints = list()
        for endpoint in line.rstrip("\n").split(" -> "):
            endpoints.append([int(x) for x in endpoint.split(",")])
        coords.append(endpoints)


def get_all_points(line):
    all_points = [line[1]]
    vector = [line[0][0] - line[1][0], line[0][1] - line[1][1]]
    steps = max([abs(x) for x in vector])
    orientation = [int(x/steps) for x in vector]
    new_point = deepcopy(line[1])
    i = 0
    while(i < steps):
        i += 1
        for j in range(len(new_point)):
            new_point[j] += orientation[j]
        all_points.append(deepcopy(new_point))
    return all_points


def part_one():
    points = dict()
    for line in coords:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            for point in get_all_points(line):
                x, y = point[0], point[1]
                if (x, y) not in points.keys():
                    points[x, y] = 1
                else:
                    points[x, y] += 1
    overlaps = 0
    for point in points.keys():
        if points[point] > 1:
            overlaps += 1
    return overlaps


def part_two():
    points = dict()
    for line in coords:
        for point in get_all_points(line):
            x, y = point[0], point[1]
            if (x, y) not in points.keys():
                points[x, y] = 1
            else:
                points[x, y] += 1
    overlaps = 0
    for point in points.keys():
        if points[point] > 1:
            overlaps += 1
    return overlaps


print(part_one())

print(part_two())

print("computed in " + str(time() - start) + " seconds")
