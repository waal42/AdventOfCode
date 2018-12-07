from time import time

start = time()

with open("day05input.txt", "r") as fin:
    strin = fin.read()
    polymer_list = list(strin)
    polymer_length = len(strin)


def reduce_polymer(lst_plmr):
    reduced = True
    while reduced:
        reduced = False
        length = len(lst_plmr)
        for index in range(0, length - 1):
            if lst_plmr[index] == "":
                continue
            if abs(ord(lst_plmr[index]) - ord(lst_plmr[index + 1])) == 32:
                lst_plmr[index] = ""
                lst_plmr[index + 1] = ""
                reduced = True
        lst_plmr = list(filter(None, lst_plmr))
    return len(lst_plmr)


def drop_letter(lst_plmr, letter):
    return list(filter(lambda a: a != letter and a != chr(ord(letter) - 32), lst_plmr))


def part_two():
    shortest = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        plmr_lst = polymer_list
        plmr_lst = drop_letter(plmr_lst, letter)
        this_length = reduce_polymer(plmr_lst)
        if letter == "a":
            shortest = this_length
        shortest = min(shortest, this_length)
    print(shortest)


part_two()

print("computed in " + str(time() - start) + " seconds")
