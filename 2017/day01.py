from time import time
start = time()

import unittest

def next_digit_match(strNumber):
    total = 0
    lenStrNum = len(strNumber)
    for i in range(lenStrNum):
        #print(i, strNumber[i], total)
        if i == lenStrNum - 1:
            if strNumber[i] == strNumber[0]:
                total += int(strNumber[i])
        else:
            if strNumber[i] == strNumber[i+1]:
                total += int(strNumber[i])
    return total


def test_next_digit_match():
    assert next_digit_match('1111') == 4
    assert next_digit_match('1122') == 3
    assert next_digit_match('1234') == 1


def halfway_digit_match(strNum):
    total = 0
    lenStrNum = len(strNum)
    halfLen = int(lenStrNum/2)
    for i in range(lenStrNum):
        halfwayIndex = i + halfLen if i + halfLen <= lenStrNum -1 else i - halfLen
        if strNum[i] == strNum[halfwayIndex]:
            total += int(strNum[i])
    return total


def part_one():
    with open('day01input.txt') as fin:
        inputString = fin.readline().strip()
        print(next_digit_match(inputString))


def part_two():
    with open('day01input.txt') as fin:
        inputString = fin.readline().strip()
        print(halfway_digit_match(inputString))


part_two()

runtime = time() - start
print("computed in " + str(runtime) + " seconds")