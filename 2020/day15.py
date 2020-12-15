from time import time
from pprint import pprint

start = time()

test_round  = [0, 3, 6] # 2020th is 436
test_round2 = [1, 3, 2] # 2020th is 1
test_round3 = [2, 1, 3] # 2020th is 10
test_round4 = [1, 2, 3] # 2020th is 27
test_round5 = [2, 3, 1] # 2020th is 78
test_round6 = [3, 2, 1] # 2020th is 438
test_round7 = [3, 1, 2] # 2020th is 1836
starting_numbers = [1, 0, 15, 2, 10, 13]

'''
prvně načístat ze seznamu, jak dojde, tak počítat
v dict držet dvojice číslo: list pozic, kdy bylo
if num in dict: new_num = i - posledni v seznamu toho cisla
'''



def part_one(numlist, position):
    index = 0
    past_nunbers = {}
    previous_number = 0
    while index < position:
        if index < len(numlist):
            past_nunbers[numlist[index]] = [index+1]
            previous_number = numlist[index]
        else:
            if len(past_nunbers[previous_number]) == 1:
                new_number = 0
            else:
                new_number = past_nunbers[previous_number][-1] - past_nunbers[previous_number][-2]
            if new_number in past_nunbers:
                past_nunbers[new_number].append(index+1)
            else:
                past_nunbers[new_number] = [index+1]
            previous_number = new_number
        index += 1
    # pprint(past_nunbers)
    return previous_number


print(part_one(starting_numbers, 2020))


print(part_one(starting_numbers, 30000000))


print("computed in " + str(time() - start) + " seconds")
