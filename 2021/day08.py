from time import time
from itertools import permutations
from pprint import pprint

start = time()

in_time = time()
with open("day08input.txt", "r") as file_in:
    signals = [[y.split(" ") for y in line.split(" | ")]
               for line in file_in.read().rstrip().split("\n")]
print("input processed in " + str(time() - in_time) + " seconds")


segments = {
    '1': [0, 2, 3, 5, 6, 7, 8, 9],
    '2': [0, 4, 5, 6, 8, 9],
    '3': [0, 1, 2, 3, 4, 7, 8, 9],
    '4': [2, 3, 4, 5, 6, 8, 9],
    '5': [0, 2, 6, 8],
    '6': [0, 1, 3, 4, 5, 6, 7, 8, 9],
    '7': [0, 2, 3, 5, 6, 8, 9]
}

numbers = dict()
for num in range(10):
    numbers[num] = []
    for segment in segments.keys():
        if num in segments[segment]:
            numbers[num].append(segment)


def part_one():
    ones = 0
    fours = 0
    sevens = 0
    eights = 0
    for signal in signals:
        for output in signal[1]:
            if len(output) == 2:
                ones += 1
            elif len(output) == 3:
                sevens += 1
            elif len(output) == 4:
                fours += 1
            elif len(output) == 7:
                eights += 1
    return ones+fours+sevens+eights


def part_two():
    output_values = 0
    for signal in signals:
        sorted_signal = sorted(signal[0], key=len)
        segs = dict()
        for letter in sorted_signal[1]:
            if letter not in sorted_signal[0]:
                segs['1'] = letter
        remaining = list()
        for letter in 'abcdefg':
            if letter not in sorted_signal[1]:
                remaining.append(letter)
        possibilites = permutations(remaining)
        for possibility in list(possibilites):
            segs['2'] = possibility[0]
            segs['4'] = possibility[1]
            segs['5'] = possibility[2]
            segs['7'] = possibility[3]
            for one in sorted_signal[0]:
                segs['3'] = one
                segs['6'] = sorted_signal[0][1] if one == sorted_signal[0][0] else sorted_signal[0][0]
                good_digits = list()
                for digit in signal[0]:
                    digit_keys = list()
                    for letter in digit:
                        digit_keys.append(list(segs.keys())[
                                          list(segs.values()).index(letter)])
                    sorted_digit_keys = sorted(digit_keys)
                    if sorted_digit_keys in numbers.values():
                        good_digits.append(list(numbers.keys())[list(
                            numbers.values()).index(sorted_digit_keys)])
                if len(good_digits) == 10:
                    output = list()
                    for out in signal[1]:
                        out_digit_keys = list()
                        for letter in out:
                            out_digit_keys.append(
                                list(segs.keys())[list(segs.values()).index(letter)])
                        output.append(str(list(numbers.keys())[
                                      list(numbers.values()).index(sorted(out_digit_keys))]))
                    output_values += int(''.join(output))
                    break
    return output_values


first = time()
print(part_one())
print("part one computed in " + str(time() - first) + " seconds")
second = time()
print(part_two())
print("part two computed in " + str(time() - second) + " seconds")

print("completely computed in " + str(time() - start) + " seconds")
