from time import time
from pprint import pprint

start = time()

direct_orbits = dict()

with open("day06input.txt", "r") as file_in:
    for line in file_in:
        orbit = line.rstrip('\n').split(')')
        if orbit[0] in direct_orbits.keys():
            direct_orbits[orbit[0]].append(orbit[1])
        else:
            direct_orbits[orbit[0]] = [orbit[1]]


def find_child_orbiters(orbitee):
    orbiters_list = list()
    if orbitee in direct_orbits.keys():
        for orbiter in direct_orbits[orbitee]:
            orbiters_list += [orbiter]
            orbiters_list += find_child_orbiters(orbiter)
        return orbiters_list
    else:
        return []


def part_one():
    count_orbits = 0
    for planet in direct_orbits.keys():
        child_orbits = find_child_orbiters(planet)
        count_orbits += len(child_orbits)
        # print(planet, child_orbits)
    print(count_orbits)


part_one()


def find_node(orbitee, node, found = False):
    if orbitee == node:
        found = True
        return [], found
    path_to_node = list()
    if orbitee in direct_orbits.keys():
        for orbiter in direct_orbits[orbitee]:
            path, found = find_node(orbiter, node, found)
            if found:
                path_to_node = [orbiter] + path + path_to_node
                break
        if orbitee == 'COM':
            return path_to_node
        return path_to_node, found
    else:
        return [], found


def part_two():
    path_to_you = find_node('COM', 'YOU')
    path_to_santa = find_node('COM', 'SAN')
    for index in range(len(path_to_santa)):
        if path_to_santa[index] != path_to_you[index]:
            break
    print(len(path_to_you) + len(path_to_santa) - 2 * (index + 1))


part_two()


print("computed in " + str(time() - start) + " seconds")
