from time import perf_counter
from ast import literal_eval  # tohle je hodně cool
from itertools import chain
from math import floor, ceil

start = perf_counter()

in_time = perf_counter()
with open("day18input.txt", "r") as file_in:
    numbers = [literal_eval(number)
               for number in file_in.read().rstrip().split("\n")]

print("input processed in " + str(perf_counter() - in_time) + " seconds")


def snailfish_addition(previous_sum, new_snail_num):
    return [previous_sum, new_snail_num]


def depth(snailfish_num):
    if isinstance(snailfish_num, list):
        return 1 + max(depth(item) for item in snailfish_num)
    else:
        return 0


def ten_or_greater(snailfish_num):
    num_str = str(snailfish_num).replace(
        "[", "").replace("]", "").replace(" ", "")
    num_list = [int(x) for x in num_str.split(",")]
    for num in num_list:
        if num >= 10:
            return num
    return 0


def explosion(snailfish_num):
    this_depth = 0
    str_snailfish_num = str(snailfish_num).replace(" ", "")
    after_explosion_left = list()
    after_explosion_right = list()
    for i in range(len(str_snailfish_num)):
        if str_snailfish_num[i] == "[":
            this_depth += 1
        if this_depth == 5:
            m = i+1
            while str_snailfish_num[m] != "]":
                m += 1
            lvl_five = literal_eval(str_snailfish_num[i:m+1])
            for j in range(i-1, 0, -1):
                if str_snailfish_num[j].isnumeric():
                    n = j
                    while str_snailfish_num[n-1].isnumeric():
                        n -= 1
                    after_explosion_left.append(str_snailfish_num[:n])
                    after_explosion_left.append(
                        str(lvl_five[0] + int(str_snailfish_num[n:j+1])))
                    after_explosion_left.append(str_snailfish_num[j+1:i])
                    break
            for k in range(m+1, len(str_snailfish_num)):
                if str_snailfish_num[k].isnumeric():
                    o = k
                    while str_snailfish_num[o+1].isnumeric():
                        o += 1
                    after_explosion_right.append(str_snailfish_num[m+1:k])
                    after_explosion_right.append(
                        str(lvl_five[1] + int(str_snailfish_num[k:o+1])))
                    after_explosion_right.append(
                        str_snailfish_num[o+1:len(str_snailfish_num)])
                    break
            break
        if str_snailfish_num[i] == "]":
            this_depth -= 1
    exploded_num = list()
    if after_explosion_left:
        exploded_num.append("".join(after_explosion_left))
    else:
        exploded_num.append(str_snailfish_num[:i])
    exploded_num.append("0")
    if after_explosion_right:
        exploded_num.append("".join(after_explosion_right))
    else:
        exploded_num.append(str_snailfish_num[m+1:])
    return literal_eval("".join(exploded_num))


def split(snailfish_num, num_to_split):
    to_replace = [floor(num_to_split/2), ceil(num_to_split/2)]
    return literal_eval(str(snailfish_num).replace(str(num_to_split), str(to_replace), 1))


def reduce(snailfish_num):
    reduced = False
    while not reduced:
        over_nine = ten_or_greater(snailfish_num)
        if depth(snailfish_num) == 5:
            snailfish_num = explosion(snailfish_num)
        elif over_nine:
            snailfish_num = split(snailfish_num, over_nine)
        else:
            reduced = True
    return snailfish_num


def count_magnitude(snailfish_num):
    return eval(str(snailfish_num).replace("[", "(3*").replace(",", "+2*").replace("]", ")"))


def part_one():
    sum = numbers[0]
    for i in range(1, len(numbers)):
        sum = reduce(snailfish_addition(sum, numbers[i]))
    return count_magnitude(sum)


def part_two():
    max_magnitude = 0
    for i in range(len(numbers) - 1):
        for j in range(i, len(numbers)):
            sum1 = reduce(snailfish_addition(numbers[i], numbers[j]))
            sum2 = reduce(snailfish_addition(numbers[j], numbers[i]))
            max_magnitude = max(max_magnitude, count_magnitude(
                sum1), count_magnitude(sum2))
    return max_magnitude


first = perf_counter()
print(part_one())
print("part one computed in " + str(perf_counter() - first) + " seconds")
second = perf_counter()
print(part_two())
print("part two computed in " + str(perf_counter() - second) + " seconds")

print("completely computed in " + str(perf_counter() - start) + " seconds")
