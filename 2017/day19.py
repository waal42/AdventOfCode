from time import time
start = time()

with open('day19input.txt', 'r') as fin:
    tmp = fin.read().split('\n')
    routing_diagram = list()
    for row in tmp:
        routing_diagram.append(list(row))


def find_start(diagram):
    for i in range(len(diagram[0])):
        if diagram[0][i] == '|':
            return i


def next_step(diagram, x, y, direction, letters):
    if diagram[y][x] == '+':
        if direction == 'up' or direction == 'down':
            if x == 0:
                direction = 'right'
            elif x == len(diagram[y]) - 1:
                direction = 'left'
            elif diagram[y][x+1] == '-' or diagram[y][x+1].isalpha():
                direction = 'right'
            else:
                direction = 'left'
        else:
            if y == 0:
                direction = 'down'
            elif y == len(diagram) - 1:
                direction = 'up'
            elif diagram[y+1][x] == '|' or diagram[y+1][x].isalpha():
                direction = 'down'
            else:
                direction = 'up'
    elif diagram[y][x].isalpha():
        letters.append(diagram[y][x])
    if direction == 'down':
        y += 1
    elif direction == 'up':
        y -= 1
    elif direction == 'left':
        x -= 1
    else:
        x += 1
    return x, y, direction, letters


def solution():
    found_letters = list()
    direction = 'down'
    x = find_start(routing_diagram)
    y = 0
    count_steps = 0
    while 0 <= x <= len(routing_diagram[y]) - 1 and 0 <= y <= len(routing_diagram) - 1:
        count_steps += 1
        # print(x, y, found_letters)
        x, y, direction, found_letters = next_step(routing_diagram, x, y, direction, found_letters)
    print(''.join(found_letters), count_steps - 1)


solution()


print('finished in ' + str(time() - start) + ' seconds')
