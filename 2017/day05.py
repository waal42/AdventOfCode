from time import time

start = time()

with open("day05input.txt", "r") as fin:
    data_input = [int(x) for x in fin.read().rstrip().split("\n")]


def part_one():
    position = 0
    jumps = 0
    len_data = len(data_input)
    while 0 <= position < len_data:
        current_position = position
        position += data_input[current_position]
        data_input[current_position] += 1
        jumps += 1
    print(jumps)


def part_two():
    position = 0
    jumps = 0
    len_data = len(data_input)
    while 0 <= position < len_data:
        current_position = position
        position += data_input[current_position]
        if data_input[current_position] >= 3:
            data_input[current_position] -= 1
        else:
            data_input[current_position] += 1
        jumps += 1
    print(jumps)


# part_one()

part_two()

runtime = time() - start
print("finished in " + str(runtime) + " seconds")

