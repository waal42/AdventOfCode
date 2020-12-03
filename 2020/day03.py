from time import time
from math import floor

start = time()

with open("day03input.txt", "r") as file_in:
    map_of_trees = [x for x in file_in.read().rstrip().split("\n")]


def part_one():
    x = 0
    trees = 0
    for row in map_of_trees:
        if row[x] == '#':
            trees += 1
        x = (x + 3) % len(row)
    return trees

# print(part_one())

def part_two():
    height = len(map_of_trees)
    width = len(map_of_trees[0])
    product = 1
    slopes = [
        {'x' : 1, 'y' : 1, 'trees' : 0},
        {'x' : 3, 'y' : 1, 'trees' : 0},
        {'x' : 5, 'y' : 1, 'trees' : 0},
        {'x' : 7, 'y' : 1, 'trees' : 0},
        {'x' : 1, 'y' : 2, 'trees' : 0}]
    for slope in slopes:
        x, y = 0, 0
        while y < height:
            if map_of_trees[y][x] == '#':
                slope['trees'] += 1
            x = (x + slope['x']) % width
            y = (y + slope['y'])
        product *= slope['trees']
    return product



print(part_two())

print("computed in " + str(time() - start) + " seconds")
