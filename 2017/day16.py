from time import time
import re
start = time()

original_dancers = 'abcdefghijklmnop'
instructions = list()
test_dancers = 'abcde'
test_instructions = ['s1', 'x3/4', 'pe/b']


with open('day16input.txt', 'r') as fin:
    instrs = fin.read().rstrip().split(',')
    for instr in instrs:
        tmplist = [instr[0]]
        tmplist += re.findall(r'\w+', instr[1:])
        instructions.append(tmplist)

# print(instructions)


def dance(instruction, dancers):
    if instruction[0] == 's':
        move = int(instruction[1])
        return dancers[-move:] + dancers[:len(dancers)-move]
    elif instruction[0] == 'x':
        dancers_list = [x for x in dancers]
        temp = dancers_list[int(instruction[1])]
        dancers_list[int(instruction[1])] = dancers_list[int(instruction[2])]
        dancers_list[int(instruction[2])] = temp
        return ''.join(dancers_list)
    elif instruction[0] == 'p':
        dancers_list = [x for x in dancers]
        indices = [dancers_list.index(instruction[1]), dancers_list.index(instruction[2])]
        temp = dancers_list[indices[0]]
        dancers_list[indices[0]] = dancers_list[indices[1]]
        dancers_list[indices[1]] = temp
        return ''.join(dancers_list)


def solution():
    dancers = original_dancers
    len_instructions = len(instructions)
    for i in range (len_instructions):
        dancers = dance(instructions[i], dancers)
        # print(dancers)
    return dancers


print('finished in ' + str(time() - start) + ' seconds')