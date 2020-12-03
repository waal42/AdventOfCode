from time import time
from math import floor

start = time()

with open("day01input.txt", "r") as file_in:
    expenses = [int(x) for x in file_in.read().rstrip().split("\n")]


def part_one():
    size = len(expenses)
    for x in range(size):
        for y in range(x, size):
            # print(expenses[x], expenses[y])
            if expenses[x] + expenses[y] == 2020:
                return (expenses[x], expenses[y], expenses[x] * expenses[y])


def part_two():
    size = len(expenses)
    for x in range(size):
        for y in range(x, size):
            for z in range(y, size):
                if expenses[x] + expenses[y] + expenses[z] == 2020:
                    return(expenses[x], expenses[y], expenses[z], expenses[x] * expenses[y] * expenses[z])


# print(part_one())

print(part_two())

print("computed in " + str(time() - start) + " seconds")
