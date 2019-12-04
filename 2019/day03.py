from time import time

start = time()

with open("day03input.txt", "r") as file_in:
    instructions = [instr.split(",") for instr in file_in.read().rstrip().split("\n")]

def calculate_step(direction, position):
    if direction == 'L':
        position = (position[0] - 1, position[1])
    elif direction == 'R':
        position = (position[0] + 1, position[1])
    elif direction == 'U':
        position = (position[0], position[1] + 1)
    elif direction == 'D':
        position = (position[0], position[1] - 1)
    return position



def part_one():
    start = (0, 0)
    path_one = [start]
    position = start
    for walk in instructions[0]:
        direction = walk[0]
        for step in range(int(walk[1:])):
            position = calculate_step(direction, position)
            path_one.append(position)
    path_two = [start]
    position = start
    crosses = list()
    for walk in instructions[1]:
        direction = walk[0]
        for step in range(int(walk[1:])):
            position = calculate_step(direction, position)
            if position in path_one:
                crosses.append(position)
            path_two.append(position)
    distances = [abs(cross[0]) + abs(cross[1]) for cross in crosses]
    print(crosses)
    print(distances)
    print(min(distances))

# part_one()

print("computed in " + str(time() - start) + " seconds")
