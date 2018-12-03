from time import time
from pprint import pprint
import re

start = time()

instructions = dict()

with open("day03input.txt") as fin:
    overlap = 0
    mat = dict()
    non_overlaps = dict()
    for instr in fin.read().rstrip().split("\n"):
        tmp = list(filter(None, re.findall(r"[0-9]*", instr)))
        key = int(tmp[0])
        instructions[key] = {
            "from_x": int(tmp[1]),
            "to_x": int(tmp[1]) + int(tmp[3]),
            "from_y": int(tmp[2]),
            "to_y": int(tmp[2]) + int(tmp[4]),
            "size": int(tmp[3]) * int(tmp[4]),
        }
        non_overlaps[key] = 0
        for x in range(instructions[key]["from_x"], instructions[key]["to_x"]):
            for y in range(instructions[key]["from_y"], instructions[key]["to_y"]):
                if (x, y) in mat.keys():
                    if len(mat[(x, y)]) == 1:
                        overlap += 1
                        non_overlaps[mat[(x, y)][0]] -= 1
                    mat[(x, y)].append(key)
                else:
                    mat[(x, y)] = [key]
                    non_overlaps[key] += 1
    print("size of overlapping inches: " + str(overlap))
    for key in non_overlaps.keys():
        if non_overlaps[key] == instructions[key]["size"]:
            print("id of completely non-overlapping rectangle: " + str(key))
            break

print("computed in " + str(time() - start) + " seconds")
