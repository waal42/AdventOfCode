from time import time

start = time()

with open("day13input.txt", "r") as file_in:
    data = [x for x in file_in.read().rstrip().split("\n")]
    earliest = int(data[0])
    operational = []
    rel_departures = []
    bus_schedule = data[1].split(',')
    for bus in range(len(bus_schedule)):
        if bus_schedule[bus] != 'x':
            bus_num = int(bus_schedule[bus])
            rem = (bus_num - bus) % bus_num
            operational.append(int(bus_num))
            rel_departures.append({'rem': rem, 'mod': bus_num})



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
    
print(part_one())

# print(rel_departures)

def max_size(numlist):
    result = 1
    for num in numlist:
        result *= num
    return result


def mods_without_this(this_mod, numlist):
    result = 1
    for mod in numlist:
        if mod != this_mod:
            result *= mod
    return result


def mmi(num, mod): # modular multiplicative inverse
    reduced_num = num % mod
    k = 1
    found = False
    while not found:
        if k*reduced_num % mod == 1:
            found = True
        else:
            k += 1
    return k


def part_two():
    departures = rel_departures
    bus_mods = operational
    total_M = max_size(bus_mods)
    timestamp = 0
    for bus in departures:
        if bus['rem'] != 0:
            # print ("x =", bus['rem'], "mod", bus['mod'])
            s = mods_without_this(bus['mod'], bus_mods)
            t = mmi(s, bus['mod'])
            q = s*t % total_M
            timestamp += bus['rem']*q
    return timestamp % total_M


print(part_two())


print("computed in " + str(time() - start) + " seconds")
