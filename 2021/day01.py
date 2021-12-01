from time import time

start = time()

with open("day01input.txt", "r") as file_in:
    depths = [int(x) for x in file_in.read().rstrip().split("\n")]

# print(depths)

def part_one(list_of_depths):
    increases = 0
    for i in range(len(list_of_depths) - 1):
        if (list_of_depths[i+1] - list_of_depths[i] > 0):
            increases += 1
    return increases

def part_two():
    triplets_of_depths = list()
    for i in range(len(depths) - 2):
        triplets_of_depths.append(depths[i] + depths[i+1] + depths[i+2])
    return part_one(triplets_of_depths)


print(part_one(depths))

print(part_two())

print("computed in " + str(time() - start) + " seconds")
