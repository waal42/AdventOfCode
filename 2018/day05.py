from time import time

start = time()

with open("day05testinput.txt", "r") as fin:
    strin = fin.read()
    polymer_list = list(strin)
    polymer_length = len(strin)
    print(strin)


def reduce_polymer(plmr):
    polymer = plmr
    popped = 0
    something_removed = False
    for index in range(len(plmr) - 1):
        if(abs(ord(polymer[index]) - ord(polymer[index+1]) == 32)):
            popped += 2
            polymer = polymer[:index] + polymer[index+2:]
            index -=1 
            something_removed = True
        if index + popped >= len(plmr) -2:
            break 
    if something_removed:
        print("i removed and i go back")
        reduce_polymer(polymer)
    else:
        print(polymer)



reduce_polymer(strin)

print("computed in " + str(time() - start) + " seconds")
