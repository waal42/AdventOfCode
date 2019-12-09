from time import time

start = time()

with open("day03input.txt", "r") as file_in:
    instructions = [instr.split(",") for instr in file_in.read().rstrip().split("\n")]


def new_position(direction, x, y):
    if direction == 'L':
        x -= 1
    elif direction == 'R':
        x += 1
    elif direction == 'U':
        y += 1
    elif direction == 'D':
        y -= 1
    return x, y

def part_one():
    x, y = 0, 0
    path_one = {y:[x]}
    for walk in instructions[0]:
        direction = walk[0]
        for step in range(int(walk[1:])):
            x, y = new_position(direction, x, y)
            if y in path_one.keys():
                path_one[y].append(x)
            else:
                path_one[y] = [x]
    x, y = 0, 0
    crosses = dict()
    second_steps = 0
    for walk in instructions[1]:
        direction = walk[0]
        for step in range(int(walk[1:])):
            x, y = new_position(direction, x, y)
            second_steps += 1
            if y in path_one.keys():
                if x in path_one[y]:
                    if (x,y) not in crosses.keys():
                        crosses[(x,y)] = second_steps
    distances = [abs(cross[0]) + abs(cross[1]) for cross in crosses]
    print(crosses)
    print(distances)
    print(min(distances))
    return crosses


def part_two():
    crosses = part_one()
    x, y = 0, 0
    first_steps = 0
    cross_distances = list()
    for walk in instructions[0]:
        direction = walk[0]
        for step in range(int(walk[1:])):
            x, y = new_position(direction, x, y)
            first_steps += 1
            if (x,y) in crosses.keys():
                cross_distances.append(first_steps + crosses[x,y])
    print(cross_distances)
    print(min(cross_distances))

part_two()

print("computed in " + str(time() - start) + " seconds")
