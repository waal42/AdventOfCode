from time import time
from intcode_computer import load_intcode, run_intcode

start = time()

with open("day02input.txt", "r") as file_in:
    orig_intcode = [int(x) for x in file_in.read().rstrip().split(",")]

#intcode = [1,1,1,4,99,5,6,0,99]

def part_one():
    print(run_intcode(load_intcode("day02input.txt"), 12, 2))

part_one()

def part_two():
    orig_intcode = load_intcode("day02input.txt")
    for noun in range(100):
        for verb in range(100):
            intcode = list(orig_intcode)
            output = run_intcode(intcode, noun, verb)
            if output == 19690720:
                print("this is it")
                print(noun, verb, 100 * noun + verb)
                

part_two()





print("computed in " + str(time() - start) + " seconds")
