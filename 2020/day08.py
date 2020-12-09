from time import time

start = time()

with open("day08input.txt", "r") as file_in:
    instructions = [x.split(" ") for x in file_in.read().rstrip().split("\n")]


def part_one():
    accumulator = 0
    index = 0
    index_lst = []
    while index not in index_lst:
        index_lst.append(index)
        if instructions[index][0] == "acc":
            if instructions[index][1][0] == "+":
                accumulator += int(instructions[index][1][1:])
            else:
                accumulator -= int(instructions[index][1][1:])
            index += 1
        elif instructions[index][0] == 'jmp':
            if instructions[index][1][0] == "+":
                index += int(instructions[index][1][1:])
            else:
                index -= int(instructions[index][1][1:])
        elif instructions[index][0] == "nop":
            index += 1
    return (accumulator)
            

# print(part_one())


def part_two():
    for inst_index in range(len(instructions)):
        if instructions[inst_index][0] == 'jmp':
            previous = 'jmp'
            instructions[inst_index][0] = 'nop'
        elif instructions[inst_index][0] == 'nop':
            previous = 'nop'
            instructions[inst_index][0] = 'jmp'
        accumulator = 0
        index = 0
        index_lst = []
        while index not in index_lst:
            index_lst.append(index)
            if instructions[index][0] == "acc":
                if instructions[index][1][0] == "+":
                    accumulator += int(instructions[index][1][1:])
                else:
                    accumulator -= int(instructions[index][1][1:])
                index += 1
            elif instructions[index][0] == 'jmp':
                if instructions[index][1][0] == "+":
                    index += int(instructions[index][1][1:])
                else:
                    index -= int(instructions[index][1][1:])
            elif instructions[index][0] == "nop":
                index += 1
            if index == len(instructions):
                return accumulator
        if instructions[inst_index][0] != 'acc':
            instructions[inst_index][0] = previous
        

print(part_two())


print("computed in " + str(time() - start) + " seconds")
