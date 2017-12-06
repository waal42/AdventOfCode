from time import time
from copy import deepcopy
# from pprint import pprint
start = time()




'''
prvně načtu input do mřížky
budu postupně procházet po řádcích a do nové mřížky zapisovat stav
každou buňku bude řešit počítadlo sousedů - důležitá kontrola hranic celé sítě

'''

lights = []
minx = 0
maxx = 99

with open('day18input.txt') as fin:
    for line in fin:
        lights.append(list(line.strip('\n')))


def count_neighbors(lights_config, x, y):
    neighbors = 0
    for i in range(max(x-1, minx), min(x+2, maxx+1)):
        for j in range(max(y-1, minx), min(y+2, maxx+1)):
            if '#' in lights_config[i][j]:
                if not (i == x and j == y):
                    # print('#')
                    neighbors += 1
    # print(x, y, neighbors)
    return neighbors


def one_step(lights_config):
    # pprint(lightsConfig)
    new_lights_config = deepcopy(lights_config)
    lights_on = 0
    len_of_line = len(lights_config)
    area = len_of_line * len(lights_config[0])
    for k in range(area):
        i = k // len_of_line
        j = k % len_of_line
        if (i == minx and j == minx) or (i == minx and j == maxx) or (i == maxx and j == minx) or (i == maxx and j == maxx):
            new_lights_config[i][j] = '#'
            lights_on += 1
        else:
            neighbors = count_neighbors(lights_config, i, j)
            if lights_config[i][j] == '#':
                if neighbors == 2 or neighbors == 3:
                    new_lights_config[i][j] = '#'
                    lights_on += 1
                else:
                    new_lights_config[i][j] = '.'
            else:
                if neighbors == 3:
                    new_lights_config[i][j] = '#'
                    lights_on += 1
                else:
                    new_lights_config[i][j] = '.'
    print('lights on: ' + str(lights_on))
    # pprint(new_lights_config)
    return new_lights_config


def part_one(lights_config):
    # pprint(lights_config)
    for i in range(100):
        print('step ' + str(i + 1))
        lights_config = one_step(lights_config)


part_one(lights)
'''
for i in range(6):
    for j in range(6):
        count_neighbors(lights, i, j)
'''

runtime = time() - start
print("computed in " + str(runtime) + " seconds")