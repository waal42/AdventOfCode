from time import time
from intcode_computer import IntcodeComputer

start = time()

with open("day09input.txt", "r") as fin:
    intcode = [int(x) for x in fin.read().rstrip().split(",")]


def part_one():
    intcode_input = 1
    int_comp_output = list()
    int_comp = IntcodeComputer(intcode=intcode, intcode_input=intcode_input)
    while(int_comp.computer_state() != "halted"):
        int_comp.execute_opcode()
        if int_comp.new_output():
            int_comp_output.append(int_comp.new_output())
    print(int_comp_output)


#part_one()


def part_two():
    intcode_input = 2
    int_comp_output = list()
    int_comp = IntcodeComputer(intcode=intcode, intcode_input=intcode_input)
    while(int_comp.computer_state() != "halted"):
        int_comp.execute_opcode()
        if int_comp.new_output():
            int_comp_output.append(int_comp.new_output())
    print(int_comp_output)


part_two()
    


print("computed in " + str(time() - start) + " seconds")
