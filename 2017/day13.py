from time import time
from copy import deepcopy
import re
start = time()

firewall = dict()
last_layer = 0

with open('day13testinput.txt', 'r') as fin:
    layers = fin.read().rstrip().split('\n')
    for layer in layers:
        tmplist = re.findall(r'\d+', layer)
        firewall[int(tmplist[0])] = [0, int(tmplist[1]) - 1, 'down']
        last_layer = max(last_layer, int(tmplist[0]))


other_firewall = dict()


with open('day13input.txt', 'r') as fin:
    layers = fin.read().rstrip().split('\n')
    for layer in layers:
        tmplist = re.findall(r'\d+', layer)
        other_firewall[int(tmplist[0])] = int(tmplist[1]) - 1
        last_layer = max(last_layer, int(tmplist[0]))


def change_direcion(layer):
    if layer[0] == layer[1]:
        layer[2] = 'up'
    elif layer[0] == 0:
        layer[2] = 'down'


def solution():
    packet_position = -1
    caught = list()
    severity = 0
    for i in range(last_layer + 1):
        packet_position += 1
        if packet_position in firewall.keys():
            if firewall[packet_position][0] == 0:
                caught.append(packet_position)
                severity += packet_position * (firewall[packet_position][1] + 1)
        for layer_number in firewall.keys():
            if firewall[layer_number][2] == 'down':
                firewall[layer_number][0] += 1
            elif firewall[layer_number][2] == 'up':
                firewall[layer_number][0] -= 1
            change_direcion(firewall[layer_number])
        # print(packet_position, caught)
        # pprint(firewall)
    print(severity)


def solution_part_two():
    i = 0
    delay = 0
    caught = False
    while i <= last_layer:
        if i in other_firewall.keys():
            if (delay + i) % (2*other_firewall[i]) == 0:
                caught = True
        if caught:
            i = 0
            delay += 1
            caught = False
        else:
            i += 1
    print(delay)


solution_part_two()

print('finished in ' + str(time() - start) + ' seconds')