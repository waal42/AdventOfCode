from time import time

start = time()

with open("day14input.txt", "r") as file_in:
    program = [x for x in file_in.read().rstrip().split("\n")]


def part_one():
    memory = {}
    mask = ['0' for x in range(36)]
    for line in program:
        instruction, value = line.split(' = ')
        if instruction == "mask":
            mask = list(value)
        else:
            mem = int(''.join(filter(str.isdigit, instruction)))
            bin_value = list(bin(int(value))[2:])
            bin_value_full = ['0' for x in range(36 - len(bin_value))] + bin_value
            result = []
            for index in range(len(mask)):
                if mask[index] == 'X':
                    result.append(bin_value_full[index])
                else:
                    result.append(mask[index])
            memory[mem] = int(''.join(result), 2)
    total = 0
    for val in memory:
        total += memory[val]
    return total
    
print(part_one())


def part_two():
    memory = {}
    mask = ['0' for x in range(36)]
    for line in program:
        instruction, value = line.split(' = ')
        if instruction == "mask":
            mask = list(value)
        else:
            address = int(''.join(filter(str.isdigit, instruction)))
            bin_address = list(bin(int(address))[2:])
            bin_address_full = ['0' for x in range(36 - len(bin_address))] + bin_address
            masked_address = []
            for index in range(len(mask)):
                if mask[index] == '0':
                    masked_address.append(bin_address_full[index])
                else:
                    masked_address.append(mask[index])
            count_exes = masked_address.count('X')
            for x in range(2**count_exes):
                bin_x = list(bin(x)[2:])
                bin_x_full = ['0' for zero in range(count_exes - len(bin_x))] + bin_x
                current_ex = 0
                final_address = []
                for symbol in masked_address:
                    if symbol == 'X':
                        final_address.append(bin_x_full[current_ex])
                        current_ex += 1
                    else:
                        final_address.append(symbol)
                memory[int(''.join(final_address), 2)] = int(value)
    total = 0
    for val in memory:
        total += memory[val]
    return total


print(part_two())


print("computed in " + str(time() - start) + " seconds")
