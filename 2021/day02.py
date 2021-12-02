from time import time

start = time()

with open("day02input.txt", "r") as file_in:
    instructions = [[x.split(" ")[0], int(x.split(" ")[1])]
                    for x in file_in.read().rstrip().split("\n")]

# print(instructions)


def part_one():
    hor = 0
    depth = 0
    for instr, val in instructions:
        if instr == "forward":
            hor += val
        elif instr == "down":
            depth += val
        elif instr == "up":
            depth -= val
    return hor*depth


def part_two():
    hor = 0
    depth = 0
    aim = 0
    for instr, val in instructions:
        if instr == "forward":
            hor += val
            depth += aim * val
        elif instr == "down":
            aim += val
        elif instr == "up":
            aim -= val
    return hor*depth


print(part_one())

print(part_two())

print("computed in " + str(time() - start) + " seconds")
