from time import time
from collections import deque
start = time()

'''
def spin(insertions):
    spinlock = deque([0])
    for i in range(1, insertions+1):
        spinlock.rotate(-puzzle)
        spinlock.append(i)
    return spinlock


puzzle = 370
first_spinlock = spin(2017)
second_spinlock = spin(50_000_000)

print(first_spinlock[0])
print(second_spinlock[second_spinlock.index(0) + 1])
'''


def part_one(steps):
    spinlock = [0]
    position = 0
    for spin in range(1, 2018):
        position = (position + steps) % spin + 1
        spinlock.insert(position, spin)
    return spinlock[position + 1]


def part_two(steps):
    after_zero = list()
    position = 0
    for spin in range(1, 50000001):
        position = (position + steps) % spin
        if position == 0:
            after_zero.append(spin)
        position += 1
    return after_zero


print(part_one(370))
print(part_two(370))

print('finished in ' + str(time() - start) + ' seconds')