from time import time
from re import findall
start = time()

pipes = dict()

with open('day12input.txt', 'r') as fin:
    pipes_list = fin.read().rstrip().split('\n')
    pipes_stripped = list()
    for pipe in pipes_list:
        tmplist = findall(r'\d+', pipe)
        pipes[tmplist[0]] = tmplist[1:]


def add_connected(node):
    to_be_added = list()
    is_something_added = False
    for connected_node in pipes[node]:
        for other_connected_node in pipes[connected_node]:
            if other_connected_node != node and other_connected_node not in pipes[node] and other_connected_node not in to_be_added:
                to_be_added.append(other_connected_node)
                is_something_added = True
    pipes[node] += to_be_added
    return is_something_added


def solution():
    added = False
    for node in pipes.keys():
        added = add_connected(node)
        while added:
            added = add_connected(node)
    print(len(pipes['0']) + 1, pipes['0'])
    groups = ['0']
    for i in range(len(pipes.keys())):
        already_in_group = False
        for group in groups:
            if str(i) in pipes[group]:
                already_in_group = True
        if not already_in_group:
            groups.append(str(i))
    print(len(groups), groups)

solution()

print('finished in ' + str(time() - start) + ' seconds')