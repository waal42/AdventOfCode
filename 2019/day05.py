from time import time
from intcode_computer import load_intcode, run_intcode

start = time()

def part_one():
    print(run_intcode(load_intcode("day05input.txt"), intcode_in=1))

part_one()

def part_two():
    print(run_intcode(load_intcode("day05input.txt"), intcode_in=5))

part_two()


print("computed in " + str(time() - start) + " seconds")
