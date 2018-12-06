from time import time

start = time()

with open("day05testinput.txt", "r") as fin:
    strin = fin.read()
    polymer_list = list(strin)
    polymer_length = len(strin)
    # print(strin)


"""def reduce_polymer(plmr):
    polymer = plmr
    popped = 0
    something_removed = False
    for index in range(len(plmr) - 1):
        if abs(ord(polymer[index]) - ord(polymer[index + 1]) == 32):
            popped += 2
            polymer = polymer[:index] + polymer[index + 2 :]
            index -= 1
            something_removed = True
        if index + popped >= len(plmr) - 2:
            break
    if something_removed:
        reduce_polymer(polymer)
    else:
        print(polymer)


reduce_polymer(strin)"""


def reduce_polymer(lst_plmr):
    for index in range(len(lst_plmr) - 1):
        if lst_plmr[index] == "":
            continue
        if abs(ord(lst_plmr[index]) - ord(lst_plmr[index + 1])) == 32:
            lst_plmr[index] = ""
            lst_plmr[index + 1] = ""
    if "" in lst_plmr:
        lst_plmr = list(filter(None, lst_plmr))
        reduce_polymer(lst_plmr)
    else:
        # print("".join(lst_plmr))
        return len(lst_plmr)


# reduce_polymer(polymer_list)


def drop_letter(lst_plmr, letter):
    return list(filter(lambda a: a != letter and a != chr(ord(letter) - 32), lst_plmr))


# TODO - tohle zatim nefunguje
def part_two():
    shortest = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        plmr_lst = polymer_list
        plmr_lst = drop_letter(plmr_lst, letter)
        this_length = reduce_polymer(plmr_lst)
        if letter == "a":
            shortest = this_length
        if shortest > this_length:
            shortest = this_length
    print(shortest)


part_two()

print("computed in " + str(time() - start) + " seconds")
