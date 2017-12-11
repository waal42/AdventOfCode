from time import time
from copy import deepcopy
# from pprint import pprint

start = time()
data = dict()

with open('day07input.txt', 'r') as fin:
    data_input = fin.read().rstrip().split('\n')
    for line in data_input:
        row = line.replace(',', '').split(' ')
        data[row[0]] = (int(row[1].replace('(', '').replace(')', '')), [row[x] for x in range(3, len(row))])


def part_one():
    held = list()
    holders = list()
    for item in data.keys():
        if data[item][1]:
            holders.append(item)
            held += data[item][1]
    for item in holders:
        if item not in held:
            print(item)


def part_two():
    check = True
    while check:
        copy_of_data = deepcopy(data)


part_two()
runtime = time() - start
print('finished in ' + str(runtime) + ' seconds')