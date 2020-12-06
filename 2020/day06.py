from time import time

start = time()

with open("day06input.txt", "r") as file_in:
    grouped_answers = [x.replace("\n", " ").split(" ")
                 for x in file_in.read().rstrip().split("\n\n")]


def part_one():
    sum_of_answers = 0
    for group in grouped_answers:
        sum_of_answers += len(set(''.join(group)))
    return sum_of_answers

print(part_one())


def part_two():
    sum_of_answers = 0
    for group in grouped_answers:
        answers = 'abcdefghijklmnopqrstuvwxyz'
        for answer in group:
            answers = set(answers).intersection(answer)
        sum_of_answers += len(answers)
    return sum_of_answers

print(part_two())


print("computed in " + str(time() - start) + " seconds")