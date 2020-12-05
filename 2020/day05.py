from time import time

start = time()

with open("day05input.txt", "r") as file_in:
    boarding_passes = [x for x in file_in.read().rstrip().split("\n")]


def read_row(boarding_pass):
    binary_row = boarding_pass[:7].replace('F', '0').replace('B', '1')
    return int(binary_row, 2)


def read_column(boarding_pass):
    binary_column = boarding_pass[-3:].replace('L', '0').replace('R', '1')
    return int(binary_column, 2)


def part_one():
    max_bpid = 0
    for boarding_pass in boarding_passes:
        max_bpid = max(max_bpid, read_row(boarding_pass)
                       * 8 + read_column(boarding_pass))
    return max_bpid


print(part_one())


def part_two():
    boarding_pass_ids = []
    for boarding_pass in boarding_passes:
        boarding_pass_ids.append(
            read_row(boarding_pass)*8 + read_column(boarding_pass))
    for i in range(min(boarding_pass_ids), max(boarding_pass_ids)):
        if i not in boarding_pass_ids:
            return i


print(part_two())


print("computed in " + str(time() - start) + " seconds")
