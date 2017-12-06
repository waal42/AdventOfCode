from time import time

start = time()

test_data_input = [0, 2, 7, 0]
data_input = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]

def part_one():
    old_state = test_data_input
    length_of_memory = len(test_data_input)
    memory_states = []
    memory_states.append(old_state)
    next_memory = True
    while next_memory:
        top_memory = old_state[old_state.index(max(old_state))]



runtime = time() - start
print('finished in ' + str(runtime) + ' seconds')