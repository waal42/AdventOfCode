from time import time
start = time()

import re

ref = {
    'children': lambda x: x == 3,
    'cats': lambda x: x > 7,
    'samoyeds': lambda x: x == 2,
    'pomeranians': lambda x: x < 3,
    'akitas': lambda x: x == 0,
    'vizslas': lambda x: x == 0,
    'goldfish': lambda x: x < 5,
    'trees': lambda x: x > 3,
    'cars': lambda x: x == 2,
    'perfumes': lambda x: x == 1
}

with open('day16input.txt', 'r') as fin:
    p = re.compile(r'^Sue ([0-9]+): ([A-Za-z]+): ([0-9]+), ([A-Za-z]+): ([0-9]+), ([A-Za-z]+): ([0-9]+)$')
    for line in fin:
        match = p.findall(line.strip())[0]
        nr = match[0]
        things = dict(zip([name for i, name in enumerate(match[1:]) if i % 2 == 0],
                          [int(count) for i, count in enumerate(match[1:]) if i % 2 == 1]))

        if sum([ref[k](v) and 1 or 0 for k, v in things.items()]) == 3: print(nr, things)


runtime = time() - start
print("computed in " + str(runtime) + " seconds")