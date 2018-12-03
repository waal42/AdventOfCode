from time import time
from pprint import pprint

start = time()

with open("day02input.txt") as file_in:
    identifications = file_in.read().rstrip().split("\n")


def part_one():
    exactly_two = 0
    exactly_three = 0
    for id in identifications:
        id_stats = dict()
        for letter in id:
            if letter in id_stats.keys():
                id_stats[letter] += 1
            else:
                id_stats[letter] = 1
        if 2 in id_stats.values():
            exactly_two += 1
        if 3 in id_stats.values():
            exactly_three += 1
    # print("twos: " + str(exactly_two))
    # print("threes: " + str(exactly_three))
    print("checksum: " + str(exactly_two * exactly_three))


def part_two():
    id_range = len(identifications)
    word_range = len(identifications[0])
    for first_id in range(id_range):
        for second_id in range(first_id + 1, id_range):
            # print(first_id, second_id)
            diff = 0
            diff_letter = 0
            for letter in range(word_range):
                if (
                    identifications[first_id][letter]
                    != identifications[second_id][letter]
                ):
                    diff += 1
                    diff_letter = letter
                if diff > 1:
                    break
            if diff == 1:
                # print(first_id, second_id)
                # print(identifications[first_id], identifications[second_id])
                # print(diff_letter)
                print(
                    "".join(
                        list(identifications[first_id])[0:diff_letter]
                        + list(identifications[first_id])[diff_letter + 1 :]
                    )
                )
                break


part_one()
part_two()

print("computed in " + str(time() - start) + " seconds")
