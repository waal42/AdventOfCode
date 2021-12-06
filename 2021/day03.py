from time import time
from statistics import mode

start = time()

with open("day03input.txt", "r") as file_in:
    diag = [x for x in file_in.read().rstrip().split("\n")]

# print(diag)


def part_one():
    positions = dict()
    for number in diag:
        for pos in range(len(number)):
            if pos in positions.keys():
                positions[pos].append(number[pos])
            else:
                positions[pos] = [number[pos]]
    # print(positions)
    gamma_lst = []
    epsilon_lst = []
    for pos in positions.keys():
        pos_mode = mode(positions[pos])
        gamma_lst.append(pos_mode)
        epsilon_lst.append(str(abs(int(pos_mode)-1)))
    gamma = int(''.join(gamma_lst), 2)
    epsilon = int(''.join(epsilon_lst), 2)
    return gamma * epsilon


def part_two():
    oxygen = diag
    co2 = diag
    for pos in range(len(diag[0])):
        oxy_count = 0
        for number in oxygen:
            oxy_count += int(number[pos])
        co2_count = 0
        for number in co2:
            co2_count += int(number[pos])
        if oxy_count >= len(oxygen)/2:
            oxy_mode = 1
        else:
            oxy_mode = 0
        if co2_count < len(co2)/2:
            co2_antimode = 1
        else:
            co2_antimode = 0
        new_oxygen = list()
        for number in oxygen:
            if len(oxygen) == 1:
                new_oxygen.append(number)
                break
            if int(number[pos]) == oxy_mode:
                new_oxygen.append(number)
        oxygen = new_oxygen
        new_co2 = list()
        for number in co2:
            if len(co2) == 1:
                new_co2.append(number)
                break
            if int(number[pos]) == co2_antimode:
                new_co2.append(number)
        co2 = new_co2
        # print(oxygen, co2)
    return int(''.join(oxygen[0]), 2) * int(''.join(co2[0]), 2)


print(part_one())

print(part_two())

print("computed in " + str(time() - start) + " seconds")
