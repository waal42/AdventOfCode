"""contains lose/gain; match '\d+'"""

import itertools
from time import time

start = time()

with open('day13input.txt') as file:
    inputs = file.read().rstrip().split('\n')

people = []
relations = {}


def parse_input(arguments):
    args = arguments[0:-1].split()
    value = int(args[3])
    if args[2] == 'lose':
        value *= -1
    subject = args[0]
    neighbor = args[-1]
    if subject not in people:
        people.append(subject)
    relations[(subject, neighbor)] = value


for arguments in inputs:
    parse_input(arguments)


def calculate_total(order):
    length = len(order)
    happiness = 0
    for n in range(length):
        person1 = order[n]
        person2 = order[(n+1) % length]
        happiness += relations[(person1, person2)]
        happiness += relations[(person2, person1)]
    return happiness

people.append('me')
for person in people:
    relations[('me', person)] = 0
    relations[(person, 'me')] = 0


first_person = people.pop(0)
orders = itertools.permutations(people)
max_happiness = 0

for order in orders:
    max_happiness = max(max_happiness, calculate_total([first_person] + list(order)))

print("Maximum happiness at the table is: " + str(max_happiness))

runtime = time() - start
print("computed in " + str(runtime) + " seconds")