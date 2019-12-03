from time import time
from math import floor

start = time()

with open("day02input.txt", "r") as file_in:
    orig_intcode = [int(x) for x in file_in.read().rstrip().split(",")]

#intcode = [1,1,1,4,99,5,6,0,99]

def intcode_computer(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb
    for opcode in range(0, len(intcode), 4):
        if intcode[opcode] == 1:
            intcode[intcode[opcode + 3]] = intcode[intcode[opcode + 1]] + intcode[intcode[opcode + 2]]
        elif intcode[opcode] == 2:
            intcode[intcode[opcode + 3]] = intcode[intcode[opcode + 1]] * intcode[intcode[opcode + 2]]
        elif intcode[opcode] == 99:
            break
        else:
            print("error")
            break
    return intcode[0]


def part_one():
    intcode = list(orig_intcode)
    print(intcode_computer(intcode, 12, 2))

part_one()

def part_two():
    for noun in range(100):
        for verb in range(100):
            intcode = list(orig_intcode)
            output = intcode_computer(intcode, noun, verb)
            # print(output)
            if output == 19690720:
                print("this is it")
                print(noun, verb, 100 * noun + verb)
                

part_two()





print("computed in " + str(time() - start) + " seconds")
