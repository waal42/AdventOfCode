from time import perf_counter

start = perf_counter()

in_time = perf_counter()
with open("day11input.txt", "r") as file_in:
    octopuses = [[int(x) for x in line]
                 for line in file_in.read().rstrip().split("\n")]
print("input processed in " + str(perf_counter() - in_time) + " seconds")

neighbors = [[-1, -1], [-1, 0], [-1, 1],
             [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def increase_neighbors(row, col):
    for neighbor in neighbors:
        (y, x) = neighbor
        if row+y in range(10) and col+x in range(10):
            octopuses[row+y][col+x] += 1


def check_neighbors_for_blink(row, col, will_blink):
    new_blinks = list()
    for neighbor in neighbors:
        (y, x) = neighbor
        if row+y in range(10) and col+x in range(10):
            if octopuses[row+y][col+x] > 9 and [row+y, col+x] not in will_blink:
                new_blinks.append([row+y, col+x])
    return new_blinks


def part_one():
    count_flashes = 0
    for i in range(100):
        will_blink = list()
        for row in range(len(octopuses)):
            for col in range(len(octopuses[0])):
                octopuses[row][col] += 1
                if octopuses[row][col] > 9:
                    will_blink.append([row, col])
        blinked = list()
        while sorted(will_blink) != sorted(blinked):
            for octopus in will_blink:
                if octopus not in blinked:
                    count_flashes += 1
                    increase_neighbors(octopus[0], octopus[1])
                    will_blink += check_neighbors_for_blink(
                        octopus[0], octopus[1], will_blink)
                    blinked.append(octopus)
        for octopus in blinked:
            octopuses[octopus[0]][octopus[1]] = 0
    return count_flashes


def part_two():
    flashes = 0
    count_steps = 100
    while(flashes != 100):
        count_steps += 1
        flashes = 0
        will_blink = list()
        for row in range(len(octopuses)):
            for col in range(len(octopuses[0])):
                octopuses[row][col] += 1
                if octopuses[row][col] > 9:
                    will_blink.append([row, col])
        blinked = list()
        while sorted(will_blink) != sorted(blinked):
            for octopus in will_blink:
                if octopus not in blinked:
                    flashes += 1
                    increase_neighbors(octopus[0], octopus[1])
                    will_blink += check_neighbors_for_blink(
                        octopus[0], octopus[1], will_blink)
                    blinked.append(octopus)
        for octopus in blinked:
            octopuses[octopus[0]][octopus[1]] = 0
    return count_steps


first = perf_counter()
print(part_one())
print("part one computed in " + str(perf_counter() - first) + " seconds")
second = perf_counter()
print(part_two())
print("part two computed in " + str(perf_counter() - second) + " seconds")

print("completely computed in " + str(perf_counter() - start) + " seconds")
