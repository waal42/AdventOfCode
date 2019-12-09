'''
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?
'''

from time import time

start = time()

puzzle_input = [359282,820401]


def is_part_one_pwd(pwd):
    two_adjacent = False
    never_decrease = list()
    str_pwd = str(pwd)
    for digit in range(len(str_pwd) - 1):
        if str_pwd[digit] == str_pwd[digit + 1]:
            two_adjacent = True
        if str_pwd[digit] <= str_pwd[digit + 1]:
            never_decrease.append(1)
    if two_adjacent and sum(never_decrease) == 5:
        return True


def part_one():
    pwds = list()
    for password in range(puzzle_input[0], puzzle_input[1] + 1):
        if is_part_one_pwd(password):
            pwds.append(password)
    print(len(pwds))


part_one()

'''
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
'''

def is_part_two_pwd(pwd):
    str_pwd = str(pwd)
    freq_pwd = {str_pwd[5] : 1}
    two_adjacent = False
    never_decrease = list()
    for digit in range(len(str_pwd) - 1):
        if str_pwd[digit] in freq_pwd.keys():
            freq_pwd[str_pwd[digit]] += 1
        else:
            freq_pwd[str_pwd[digit]] = 1
        if str_pwd[digit] <= str_pwd[digit + 1]:
            never_decrease.append(1)
    for digit in freq_pwd.keys():
        if freq_pwd[digit] == 2:
            two_adjacent = True
    if two_adjacent and sum(never_decrease) == 5:
        return True
    else:
        return False


def part_two():
    pwds = list()
    for password in range(puzzle_input[0], puzzle_input[1] + 1):
        if is_part_two_pwd(password):
            pwds.append(password)
    print(len(pwds))

part_two()


print("computed in " + str(time() - start) + " seconds")
