from time import time
from pprint import pprint

start = time()

direct_orbits = dict()

with open("day06testinput.txt", "r") as file_in:
    for line in file_in:
        orbit = line.rstrip('\n').split(')')
        if orbit[0] in direct_orbits.keys():
            direct_orbits[orbit[0]].append(orbit[1])
        else:
            direct_orbits[orbit[0]] = [orbit[1]]
    
pprint(direct_orbits)

# nutne revidovat rekurzi
def find_child_orbiters(orbitee, list_of_orbiters):
    if orbitee in direct_orbits.keys():
        for orbiter in direct_orbits[orbitee]:
            newlist += find_child_orbiters(orbiter, list_of_orbiters)
            list_of_orbiters.append(orbiter)
    return list_of_orbiters



def part_one():
    print(find_child_orbiters('COM', direct_orbits['COM']))

part_one()





print("computed in " + str(time() - start) + " seconds")
