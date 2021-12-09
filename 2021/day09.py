from time import time
from math import prod

start = time()

in_time = time()
with open("day09input.txt", "r") as file_in:
    heightmap = [line for line in file_in.read().rstrip().split("\n")]
    max_y = len(heightmap)
    max_x = len(heightmap[0])
print("input processed in " + str(time() - in_time) + " seconds")

directions = {
    'right': [1, 0],
    'up': [0, -1],
    'left': [-1, 0],
    'down': [0, 1]
}

low_points = list()


def local_minimum(position):
    local_min = True
    for direction in directions.keys():
        if position[0] + directions[direction][0] in range(max_x) and position[1] + directions[direction][1] in range(max_y):
            if heightmap[position[1]][position[0]] >= heightmap[position[1] + directions[direction][1]][position[0] + directions[direction][0]]:
                local_min = False
                break
    return local_min


def find_basin(current_basin, visited):
    add_to_basin = list()
    add_to_visited = list()
    for position in current_basin:
        if position not in visited:
            for direction in directions.keys():
                if position[0] + directions[direction][0] in range(max_x) and position[1] + directions[direction][1] in range(max_y):
                    if heightmap[position[1] + directions[direction][1]][position[0] + directions[direction][0]] != str(9):
                        add_to_basin.append(
                            (position[0] + directions[direction][0], position[1] + directions[direction][1]))
            add_to_visited.append(position)
    return [add_to_basin, add_to_visited]


def part_one():
    risk_level_sum = 0
    for y in range(max_y):
        for x in range(max_x):
            if local_minimum((x, y)):
                low_points.append((x, y))
                risk_level_sum += int(heightmap[y][x]) + 1
    return risk_level_sum


def part_two():
    basins = list()
    for low_point in low_points:
        basin = [low_point]
        visited = list()
        while(len(set(visited)) < len(set(basin))):
            for position in basin:
                if position not in visited:
                    new_positions = find_basin(basin, visited)
                    basin = list(set(basin + new_positions[0]))
                    visited = list(set(visited + new_positions[1]))
        basins.append(len(set(basin)))
    sorted_basins = sorted(basins, reverse=True)[:3]
    return prod(sorted_basins)


first = time()
print(part_one())
print("part one computed in " + str(time() - first) + " seconds")
second = time()
print(part_two())
print("part two computed in " + str(time() - second) + " seconds")

print("completely computed in " + str(time() - start) + " seconds")
