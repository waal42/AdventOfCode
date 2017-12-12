from time import time

start = time()
data = dict()

with open('day07input.txt', 'r') as fin:
    data_input = fin.read().rstrip().split('\n')
    for line in data_input:
        row = line.replace(',', '').split(' ')
        data[row[0]] = (int(row[1].replace('(', '').replace(')', '')), [row[x] for x in range(3, len(row))])


def part_one():
    held = list()
    holders = list()
    for item in data.keys():
        if data[item][1]:
            holders.append(item)
            held += data[item][1]
    for item in holders:
        if item not in held:
            print(item)


def is_last_level(program):
    if not data[program][1]:
        return True
    else:
        return False


def weight_above(program):
    if is_last_level(program):
        return data[program][0]
    else:
        total = data[program][0]
        for subprogram in data[program][1]:
            total += weight_above(subprogram)
        return total


def get_children(program):
    for subprogram in data[program][1]:
        print(program, data[program], subprogram, data[subprogram])


def part_two():
    for program in data.keys():
        if not is_last_level(program):
            check_weight = list()
            for subprogram in data[program][1]:
                check_weight.append((subprogram, weight_above(subprogram)))
            total = 0
            for subprogram in check_weight:
                total += subprogram[1]
            if total // len(check_weight) != check_weight[0][1]:
                print(program, check_weight)


part_two()
get_children('gveca')
runtime = time() - start
print('finished in ' + str(runtime) + ' seconds')