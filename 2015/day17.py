from time import time
start = time()

import itertools

containers = list(map(int, open('day17input.txt', 'r').read().strip().split('\n')))
eggnog = 150


def part_one():
    total = 0
    for i in range(len(containers)):
        subtotal = 0
        for combination in itertools.combinations(containers, i):
            if sum(combination) == eggnog:
                subtotal += 1
        total += subtotal
        print(subtotal)
    print(total)


def part_two():
    ans = 0
    for i in range(1, len(containers) + 1):
        for combination in itertools.combinations(containers, i):
            if sum(combination) == eggnog:
                ans += 1
        if ans:
            break
    print(ans)


part_one()
part_two()

runtime = time() - start
print("computed in " + str(runtime) + " seconds")