from time import time
from math import factorial

start = time()

with open("day10input.txt", "r") as file_in:
    joltages = list(set([int(x) for x in file_in.read().rstrip().split("\n")]))

# print(joltages)


def part_one():
    if joltages[0] == 1:
        one = 1
        three = 1
    else:
        one = 0
        three = 3
    for index in range(len(joltages)-1):
        if joltages[index + 1] - joltages[index] == 3:
            three += 1
        elif joltages[index + 1] - joltages[index] == 1:
            one += 1
        else:
            print("wtf")
    return one*three

# print(part_one())


def list_differences(joltages):
    previous = 0
    differences = list()
    for joltage in joltages:
        differences.append(joltage - previous)
        previous = joltage
    differences.append(3)
    return differences


def ones_sequence(n):
    if n == -3 or n == -2 or n == -1:
        return 0
    elif n == 0:
        return 1
    else:
        return ones_sequence(n-1) + ones_sequence(n-2) + ones_sequence(n-3)


def part_two():
    differences = ''.join([str(x) for x in list_differences(joltages)]).split('3')
    arrangements = 1
    for ones in differences:
        n = len(ones)
        if n>0:
            arrangements *= ones_sequence(n)
    return arrangements


print(part_two())


print("computed in " + str(time() - start) + " seconds")
