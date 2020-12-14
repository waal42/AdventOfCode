from time import time

start = time()

with open("day13testinput.txt", "r") as file_in:
    data = [x for x in file_in.read().rstrip().split("\n")]
    earliest = int(data[0])
    operational = []
    rel_departures = {}
    bus_schedule = data[1].split(',')
    for bus in range(len(bus_schedule)):
        if bus_schedule[bus] != 'x':
            operational.append(int(bus_schedule[bus]))
            rel_departures[bus] = int(bus_schedule[bus])
        else:
            rel_departures[bus] = 'x'




# print(earliest, operational)


def part_one():
    timestamp = earliest - 1
    bus_found = False
    while not bus_found:
        timestamp += 1
        for bus in operational:
            if timestamp % bus == 0:
                bus_found = True
                break
    return bus*(timestamp-earliest)             
    
# print(part_one())

print(rel_departures)

'''
0,  1, 2, 3,  4, 5,  6,  7
7, 13, x, x, 59, x, 31, 19

x == ?
7  | x
13 | x+1
59 | x+4
31 | x+6
19 | x+7

'''


def part_two():
    min_timestamp = 1000


print(part_two())


print("computed in " + str(time() - start) + " seconds")
