from time import time
from math import gcd
from itertools import cycle

start = time()

with open("day10testinput.txt", "r") as fin:
    region = [line.rstrip("\n") for line in fin]
    max_y = len(region) - 1
    max_x = len(region[0]) - 1
    #print(region)

def part_one():
    asteroids = list()
    visible_asteroids = dict()
    for y in range(max_y):
        for x in range(max_x):
            if region[y][x] == '#':
                asteroids.append((x,y))
    for asteroid in asteroids:
        visible_asteroids[asteroid] = 0
        for other in asteroids:
            if asteroid != other:
                vector = (other[0] - asteroid[0], other[1] - asteroid[1])
                step = gcd(vector[0], vector[1])
                normalized = [int(x/step) for x in vector]
                index = 1
                while((asteroid[0] + index * normalized[0]) >= 0 and (asteroid[1] + index * normalized[1]) >= 0 and (asteroid[0] + index * normalized[0]) <= max_x and (asteroid[1] + index * normalized[1]) <= max_y):
                    if region[asteroid[1] + index * normalized[1]][asteroid[0] + index * normalized[0]] == "#":
                        if (asteroid[0] + index * normalized[0] == other[0] and asteroid[1] + index * normalized[1] == other[1]):
                            visible_asteroids[asteroid] += 1
                        break
                    index += 1
    #print(visible_asteroids)
    most_asteroids = [(0,0), 0]
    for asteroid in visible_asteroids.keys():
        if visible_asteroids[asteroid] > most_asteroids[1]:
            most_asteroids = [asteroid, visible_asteroids[asteroid]]
    return(most_asteroids)


# print(part_one())

def part_two(base):
    laser_direction = {
        'up'    : ((0, 0), (max_x, 0)),
        'right' : ((max_x, 0), (max_x, max_y)),
        'down'  : ((0, max_y), (max_x, max_y)),
        'left'  : ((0, 0), (0, max_y))
    }
    pointer = [base[0], 0]
    counter = 0
    for direction in cycle(laser_direction.keys()):
        corn1, corn2 = laser_direction[direction][0], laser_direction[direction][1]
        print(corn1, corn2)
        while(corn1[0] <= pointer[0] and corn1[1] <= pointer[1] and pointer[0] <= corn2[0] and pointer[1] <= corn2[1]):
            print(pointer)
            if direction == 'up':
                pointer = [pointer[0] + 1, pointer[1]]
            elif direction == 'right':
                pointer = [pointer[0], pointer[1] + 1]
            elif direction == 'down':
                pointer = [pointer[0] - 1, pointer[1]]
            elif direction == 'left':
                pointer = [pointer[0], pointer[1] - 1]
        if direction == 'left':
            break




part_two(part_one()[0])


print("computed in " + str(time() - start) + " seconds")
