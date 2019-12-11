from time import time
from intcode_computer import load_intcode, run_intcode
from itertools import permutations

start = time()

def part_one():
    max_out = 0
    for permutation in permutations(range(5)):
        intcode = load_intcode("day07input.txt")
        out1 = run_intcode(list(intcode), intcode_in=[permutation[0], 0])
        out2 = run_intcode(list(intcode), intcode_in=[permutation[1], out1])
        out3 = run_intcode(list(intcode), intcode_in=[permutation[2], out2])
        out4 = run_intcode(list(intcode), intcode_in=[permutation[3], out3])
        out5 = run_intcode(list(intcode), intcode_in=[permutation[4], out4])
        if out5 > max_out:
            max_out = out5
            max_perm = permutation
    print(max_out, max_perm)

# part_one()


def part_two():
    max_out = 0
    out = 0
    # intcode = load_intcode("day07input.txt")
    intcode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    for permutation in permutations(range(5, 10)):
        for element in permutation:
            out = run_intcode(list(intcode), intcode_in=[element, out], wait=True)
            print(out)
        if out > max_out:
            max_out = out
            max_perm = permutation
    print(max_out, max_perm)

part_two()

print("computed in " + str(time() - start) + " seconds")
