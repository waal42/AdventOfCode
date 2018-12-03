from time import time
from itertools import cycle

start = time()

with open("day01input.txt", "r") as file_in:
    instructions = [int(x) for x in file_in.read().rstrip().split("\n")]


def part_one():
    print(sum(instructions))


def part_two():
    freq = 0
    freq_list = list()
    for instr in cycle(instructions):
        freq += instr
        # print(freq, freq_list)
        if freq in freq_list:
            print(freq)
            break
        else:
            freq_list.append(freq)


part_two()

print("computed in " + str(time() - start) + " seconds")
