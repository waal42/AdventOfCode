from time import time
from pprint import pprint
start = time()

with open('day08input.txt', 'r') as fin:
    instructions = [instruction.split(' ') for instruction in fin.read().rstrip().split('\n')]

registry = dict()


def condition(instr):
    if instr[4] not in registry.keys():
        registry[instr[4]] = 0
    if instr[5] == '<':
        return True if registry[instr[4]] < int(instr[6]) else False
    elif instr[5] == '>':
        return True if registry[instr[4]] > int(instr[6]) else False
    elif instr[5] == '<=':
        return True if registry[instr[4]] <= int(instr[6]) else False
    elif instr[5] == '>=':
        return True if registry[instr[4]] >= int(instr[6]) else False
    elif instr[5] == '==':
        return True if registry[instr[4]] == int(instr[6]) else False
    else:
        return True if registry[instr[4]] != int(instr[6]) else False


def inc(instr):
    if instr[0] not in registry.keys():
        registry[instr[0]] = 0
    if condition(instr):
        registry[instr[0]] += int(instr[2])


def dec(instr):
    if instr[0] not in registry.keys():
        registry[instr[0]] = 0
    if condition(instr):
        registry[instr[0]] -= int(instr[2])


def solution():
    max_held = 0
    for instruction in instructions:
        if instruction[1] == 'inc':
            inc(instruction)
        else:
            dec(instruction)
        max_held = max(max_held, registry[instruction[0]])
        # print(instruction,instruction[0], registry[instruction[0]])
    # pprint(registry)
    max_registry = 0
    for reg in registry.keys():
        max_registry = max(max_registry, registry[reg])
    print(max_held)
    print(max_registry)


solution()
runtime = time() - start
print('finished in ' + str(runtime) + ' seconds')
