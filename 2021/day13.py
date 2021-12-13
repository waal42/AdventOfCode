from time import perf_counter
from copy import deepcopy

start = perf_counter()

in_time = perf_counter()
with open("day13input.txt", "r") as file_in:
    [raw_dots, raw_folds] = [[x for x in block.split(
        "\n")] for block in file_in.read().rstrip().split("\n\n")]
    dots = [{'x': int(dot.split(',')[0]), 'y': int(dot.split(',')[1])}
            for dot in raw_dots]
    folds = [fold.split(" ")[2].split("=") for fold in raw_folds]
print("input processed in " + str(perf_counter() - in_time) + " seconds")

# print(dots, folds)


def part_one():
    new_dots = list()
    count = 0
    first_fold = folds[0]
    other = 'x' if first_fold[0] == 'y' else 'y'
    for dot in dots:
        if dot[first_fold[0]] < int(first_fold[1]):
            new_dot = {other: dot[other], first_fold[0]: dot[first_fold[0]]}
        else:
            new_dot = {other: dot[other], first_fold[0]: 2*int(first_fold[1]) - dot[first_fold[0]]}
        if new_dot not in new_dots:
            count += 1
            new_dots.append(new_dot)
    return count


def part_two():
    global dots
    this_dots = deepcopy(dots)
    for fold in folds:
        new_dots = list()
        fold_coord = fold[0]
        fold_value = int(fold[1])
        other_coord = 'x' if fold_coord == 'y' else 'y'
        for dot in this_dots:
            if dot[fold_coord] < fold_value:
                new_dot = {
                    other_coord: dot[other_coord], fold_coord: dot[fold_coord]}
            else:
                new_dot = {other_coord: dot[other_coord],
                           fold_coord: 2*fold_value - dot[fold_coord]}
            if new_dot not in new_dots:
                new_dots.append(new_dot)
        this_dots = new_dots
    max_x = 0
    max_y = 0
    simple_dots = list()
    for dot in this_dots:
        max_x = max(max_x, dot['x'])
        max_y = max(max_y, dot['y'])
        simple_dots.append([dot['x'], dot['y']])
    for line in range(max_y+1):
        print_line = list()
        for char in range(max_x+1):
            if [char, line] in simple_dots:
                print_line.append('#')
            else:
                print_line.append(' ')
        print(''.join(print_line))


first = perf_counter()
print(part_one())
print("part one computed in " + str(perf_counter() - first) + " seconds")
second = perf_counter()
print(part_two())
print("part two computed in " + str(perf_counter() - second) + " seconds")

print("completely computed in " + str(perf_counter() - start) + " seconds")
