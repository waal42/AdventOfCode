from time import time
from math import ceil
from copy import deepcopy
start = time()

test_data_input = [0, 2, 7, 0]
data_input = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]


def part_one():
    old_state = data_input
    length_of_memory = len(old_state)
    memory_states = list()
    memory_states.append(old_state)
    next_memory = True
    while next_memory:
        biggest_memory = max(old_state)
        index_biggest_memory = old_state.index(biggest_memory)
        new_state = deepcopy(old_state)
        new_state[index_biggest_memory] = 0
        index = index_biggest_memory
        while biggest_memory > 0:
            index += 1
            if index == length_of_memory:
                index = 0
            new_state[index] += 1
            biggest_memory -= 1
        if new_state in memory_states:
            next_memory = False
        else:
            memory_states.append(new_state)
        old_state = new_state
    print(len(memory_states), len(memory_states) - memory_states.index(new_state))


part_one()

runtime = time() - start
print('finished in ' + str(runtime) + ' seconds')