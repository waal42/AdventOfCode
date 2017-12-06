from time import time
from pprint import pprint
start = time()

puzzle_input = 312051


def count_distance(num):
    if num == 1:
        return 0
    x = num ** 0.5 + 1 if int(num ** 0.5) ** 2 != num else num ** 0.5
    side = int(x) if int(x) % 2 == 1 else int(x) + 1
    right_corner = side ** 2
    i = 0
    while right_corner - i*(side-1) >= num:
        i += 1
    return (side//2) + abs(right_corner-i*(side-1) + (side//2) - num)


'''
pozici drzet v dictionary, pruchod rizen smerem a kontrolou, ze pole okolo jsou prazdna;
ukladam jako souradnice (klic) se souctem (hodnota)
'''
def part_two():
    positions = dict()
    x = 0
    y = 0
    positions[(x,y)] = 1
    last_cell = 1
    direction = 'right'
    end_cycle = False
    while not end_cycle:
        if direction == 'right':
            x += 1
            value = 0
            if (x-1, y) in positions.keys():
                value += positions[(x-1, y)]
            if (x-1, y+1) in positions.keys():
                value += positions[(x-1, y+1)]
            if (x+1, y+1) in positions.keys():
                value += positions[(x+1, y+1)]
            if (x, y+1) in positions.keys():
                value += positions[(x, y+1)]
            else:
                direction = 'up'
            positions[(x, y)] = value
        elif direction == 'up':
            y += 1
            value = 0
            if (x, y-1) in positions.keys():
                value += positions[(x, y-1)]
            if (x-1, y-1) in positions.keys():
                value += positions[(x-1, y-1)]
            if (x-1, y+1) in positions.keys():
                value += positions[(x-1, y+1)]
            if (x-1, y) in positions.keys():
                value += positions[(x-1, y)]
            else:
                direction = 'left'
            positions[(x, y)] = value
        elif direction == 'left':
            x -= 1
            value = 0
            if (x+1, y) in positions.keys():
                value += positions[(x+1, y)]
            if (x-1, y-1) in positions.keys():
                value += positions[(x-1, y-1)]
            if (x+1, y-1) in positions.keys():
                value += positions[(x+1, y-1)]
            if (x, y-1) in positions.keys():
                value += positions[(x, y-1)]
            else:
                direction = 'down'
            positions[(x, y)] = value
        elif direction == 'down':
            y -= 1
            value = 0
            if (x, y+1) in positions.keys():
                value += positions[(x, y+1)]
            if (x+1, y+1) in positions.keys():
                value += positions[(x+1, y+1)]
            if (x+1, y-1) in positions.keys():
                value += positions[(x+1, y-1)]
            if (x+1, y) in positions.keys():
                value += positions[(x+1, y)]
            else:
                direction = 'right'
            positions[(x, y)] = value
        last_cell = positions[(x, y)]
        if last_cell > puzzle_input:
            end_cycle = True
        # pprint(positions)
        print(last_cell)


# print(count_distance(puzzle_input))
part_two()

runtime = time() - start
print('finished in ' + str(runtime) + ' seconds')