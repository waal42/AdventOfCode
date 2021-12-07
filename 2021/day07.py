from time import time
import statistics as stat

start = time()

in_time = time()
with open("day07input.txt", "r") as file_in:
    crabs = [int(x) for x in file_in.readline().split(",")]
print("input processed in " + str(time() - in_time) + " seconds")


def triangular_num(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum


def part_one():
    fuel = 0
    position = int(stat.median(crabs))
    for crab in crabs:
        fuel += abs(crab-position)
    return fuel


def part_two():
    fuels = list()
    position = int(stat.mean(crabs))
    more_positions = [x for x in range(position-2, position+3)]
    for near in more_positions:
        fuel = 0
        for crab in crabs:
            fuel += triangular_num(abs(crab-near))
        fuels.append(fuel)
    return min(fuels)


first = time()
print(part_one())
print("part one computed in " + str(time() - first) + " seconds")
second = time()
print(part_two())
print("part two computed in " + str(time() - second) + " seconds")

print("completely computed in " + str(time() - start) + " seconds")
