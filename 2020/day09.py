from time import time

start = time()

with open("day09input.txt", "r") as file_in:
    numbers = [int(x) for x in file_in.read().rstrip().split("\n")]


def part_one(preamble_len):
    for index in range(preamble_len, len(numbers)):
        preamble = [number for number in numbers[index-preamble_len:index]]
        sum_from_preamble = False
        for number in preamble:
            if numbers[index] - number in preamble:
                sum_from_preamble = True
        if not sum_from_preamble:
            break
    return numbers[index]

# print(part_one(25))


def part_two():
    invalid_number = part_one(25)
    for index in range(len(numbers)):
        sum = numbers[index]
        for index_to_add in range(index+1, len(numbers)):
            sum += numbers[index_to_add]
            if sum == invalid_number:
                max_num = max(numbers[index:index_to_add+1])
                min_num = min(numbers[index:index_to_add+1])
                return max_num + min_num
            elif sum > invalid_number:
                break


print(part_two())


print("computed in " + str(time() - start) + " seconds")
