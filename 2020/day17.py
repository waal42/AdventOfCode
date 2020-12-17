from time import time

total_time = time()

init_active_cubes = []
init_active_hypercubes = []

parse_time = time()

with open("day17input.txt", "r") as file_in:
    initial_state = [x for x in file_in.read().rstrip().split("\n")]
    for y in range(len(initial_state)):
        for x in range(len(initial_state[0])):
            if initial_state[y][x] == '#':
                init_active_cubes.append((x, y, 0))
                init_active_hypercubes.append((x, y, 0, 0))

print("parse time: " + str(time() - parse_time) + " seconds")

def count_neighbors(cube, active_cubes):
    neighbors = 0
    for active in active_cubes:
        is_neighbor = True
        if active == cube:
            continue
        for dimension in range(len(cube)):
            if not -1 <= cube[dimension] - active[dimension] <= 1:
                is_neighbor = False
                break
        if is_neighbor:
            neighbors += 1
    return neighbors

part_one_time = time()

def part_one():
    active_cubes = init_active_cubes
    init_max_y = len(initial_state)
    init_max_x = len(initial_state[0])
    for cycle in range(1, 7):
        new_active_cubes = []
        for z in range(-cycle, cycle+1):
            for y in range(-cycle, init_max_y + cycle + 1):
                for x in range(-cycle, init_max_x + cycle + 1):
                    neighbors = count_neighbors((x, y, z), active_cubes)
                    if (x, y, z) in active_cubes and neighbors in [2, 3]:
                        new_active_cubes.append((x, y, z))
                    if (x, y, z) not in active_cubes and neighbors == 3:
                        new_active_cubes.append((x, y, z))
        active_cubes = new_active_cubes
    return len(active_cubes)


print(part_one())

print("part one time: " + str(time() - part_one_time) + " seconds")

part_two_time = time()

def part_two():
    active_hypercubes = init_active_hypercubes
    init_max_y = len(initial_state)
    init_max_x = len(initial_state[0])
    for cycle in range(1, 7):
        new_active_hypercubes = []
        for w in range(-cycle, cycle+1):
            for z in range(-cycle, cycle+1):
                for y in range(-cycle, init_max_y + cycle + 1):
                    for x in range(-cycle, init_max_x + cycle + 1):
                        neighbors = count_neighbors((x, y, z, w), active_hypercubes)
                        if (x, y, z, w) in active_hypercubes and neighbors in [2, 3]:
                            new_active_hypercubes.append((x, y, z, w))
                        if (x, y, z, w) not in active_hypercubes and neighbors == 3:
                            new_active_hypercubes.append((x, y, z, w))
        active_hypercubes = new_active_hypercubes
    return len(active_hypercubes)

print(part_two())

print("part two time: " + str(time() - part_two_time) + " seconds")


print("total time: " + str(time() - total_time) + " seconds")
