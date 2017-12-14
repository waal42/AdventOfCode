from time import time
start = time()

with open('day11input.txt', 'r') as fin:
    dirs = fin.read().rstrip().split(',')


def move(instruction):
    dx, dy, dz = 0, 0, 0
    if instruction == 'n':
        dy += 1
        dz -= 1
    elif instruction == 's':
        dy -= 1
        dz += 1
    elif instruction == 'nw':
        dx -= 1
        dy += 1
    elif instruction == 'se':
        dx += 1
        dy -= 1
    elif instruction == 'ne':
        dx += 1
        dz -= 1
    elif instruction == 'sw':
        dx -= 1
        dz += 1
    return [dx, dy, dz]


def solution(directions):
    most_steps = 0
    position = [0, 0, 0]
    for instr in directions:
        moved = move(instr)
        for i in range(3):
            position[i] += moved[i]
            most_steps = max(most_steps, abs((max(position))))
        # print(position)
    print(abs(max(position)), most_steps)


solution(dirs)


print('finished in ' + str(time() - start) + ' seconds')