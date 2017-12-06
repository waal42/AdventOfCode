from time import time
from pprint import pprint

start = time()

finish_line = 2503

reindeer_stats = {}


def parse_input(reindeer):
    args = reindeer[0:-1].split()
    name = args[0]
    speed = int(args[3])
    time = int(args[6])
    rest = int(args[-2])
    reindeer_stats[name] = {'speed': speed,
                            'time': time,
                            'rest': rest,
                            'running': True,
                            'points': 0,
                            'distance': 0,
                            'time_to_change': time
                            }


def compute_distance(reindeer):
    time = reindeer_stats[reindeer]['time']
    speed = reindeer_stats[reindeer]['speed']
    rest = reindeer_stats[reindeer]['rest']
    time_elapsed = 0
    time_ran = 0
    cycles = 0
    while time_elapsed < finish_line:
        if time_elapsed + time > finish_line:
            time_ran += finish_line - time_elapsed
            time_elapsed = finish_line
        else:
            time_ran += time
            time_elapsed += time
        time_elapsed += rest
    return time_ran * speed


def part_one():
    with open('day14input.txt') as file:
        inputs = file.read().rstrip().split('\n')

    for reindeer in inputs:
        parse_input(reindeer)

    max_distance = 0
    for reindeer in reindeer_stats.keys():
        max_distance = max(max_distance, compute_distance(reindeer))

    print(max_distance)


def part_two():
    with open('day14input.txt') as file:
        inputs = file.read().rstrip().split('\n')

    for reindeer in inputs:
        parse_input(reindeer)

    time_elapsed = 0
    for lap in range(finish_line + 1):
        if lap > 0:
            previous_lap = max_distance
        time_elapsed += 1
        max_distance = 0
        for deer in reindeer_stats.keys():
            if lap > 0:
                if reindeer_stats[deer]['distance'] == previous_lap:
                    reindeer_stats[deer]['points'] += 1
            reindeer_stats[deer]['time_to_change'] -= 1
            if reindeer_stats[deer]['running']:
                reindeer_stats[deer]['distance'] += reindeer_stats[deer]['speed']
            if reindeer_stats[deer]['time_to_change'] == 0:
                reindeer_stats[deer]['time_to_change'] = reindeer_stats[deer]['rest'] if reindeer_stats[deer]['running'] else reindeer_stats[deer]['time']
                reindeer_stats[deer]['running'] = not reindeer_stats[deer]['running']
            max_distance = max(max_distance, reindeer_stats[deer]['distance'])
    pprint(reindeer_stats)


part_two()


runtime = time() - start
print("computed in " + str(runtime) + " seconds")