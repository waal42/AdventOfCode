from time import time

start = time()

with open("day02input.txt", "r") as file_in:
    instructions = [[x.split(" ")[0], int(x.split(" ")[1])]
                    for x in file_in.read().rstrip().split("\n")]

# print(instructions)


def part_one():
    hor = 0
    depth = 0
    for instr in instructions:
        if instr[0] == "forward":
            hor += instr[1]
        elif instr[0] == "down":
            depth += instr[1]
        elif instr[0] == "up":
            depth -= instr[1]
    return hor*depth


def part_two():
    hor = 0
    depth = 0
    aim = 0
    for instr in instructions:
        if instr[0] == "forward":
            hor += instr[1]
            depth += aim * instr[1]
        elif instr[0] == "down":
            aim += instr[1]
        elif instr[0] == "up":
            aim -= instr[1]
    return hor*depth


print(part_one())

print(part_two())

print("computed in " + str(time() - start) + " seconds")
