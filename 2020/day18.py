from time import time

total_time = time()
parse_time = time()

with open("day18testinput.txt", "r") as file_in:
    data = [x for x in file_in.read().rstrip().split("\n")]


print("parse time: " + str(time() - parse_time) + " seconds")


part_one_time = time()

def part_one():
    pass



print(part_one())

# part one test: sum([71, 26, 437, 12240, 13632]) = 26406

print("part one time: " + str(time() - part_one_time) + " seconds")

part_two_time = time()

def part_two():
    pass

print(part_two())

print("part two time: " + str(time() - part_two_time) + " seconds")


print("total time: " + str(time() - total_time) + " seconds")
