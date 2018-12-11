from time import time
from pprint import pprint
from itertools import cycle
import re

start = time()

instructions = list()
parts = set()

with open("day07input.txt", "r") as fin:
    for line in fin.read().strip().split("\n"):
        match = re.findall(r"[A-Z]", line)[1:]
        instructions.append(tuple(match))
        for item in match:
            parts.add(item)
    sorted_parts = sorted(parts)


def part_one():
    scheme = dict()
    blocked = list()
    order = list()
    buffer = list()
    for item in sorted_parts:
        scheme[item] = {"needed_for": [], "blocked_by": [], "built": False}
    for instr in instructions:
        scheme[instr[0]]["needed_for"].append(instr[1])
        scheme[instr[1]]["blocked_by"].append(instr[0])
        blocked.append(instr[1])
    pprint(scheme)
    while len(order) != len(sorted_parts):
        buffer = sorted(
            [
                x
                for x in scheme.keys()
                if scheme[x]["blocked_by"] == [] and scheme[x]["built"] == False
            ]
        )
        order.append(buffer[0])
        scheme[buffer[0]]["built"] = True
        print("".join(order))
        for part in scheme[buffer[0]]["needed_for"]:
            scheme[part]["blocked_by"].pop(scheme[part]["blocked_by"].index(buffer[0]))
    print("".join(order))


# part_one()


def part_two():
    scheme = dict()
    blocked = list()
    order = list()
    buffer = list()
    workers = 5
    working = 0
    elapsed_time = -1
    time_to_build = 60
    for item in sorted_parts:
        scheme[item] = {
            "needed_for": [],
            "blocked_by": [],
            "built": False,
            "time_to_build": time_to_build + ord(item) - 64,
        }
    for instr in instructions:
        scheme[instr[0]]["needed_for"].append(instr[1])
        scheme[instr[1]]["blocked_by"].append(instr[0])
        blocked.append(instr[1])
    pprint(scheme)
    while len(order) != len(sorted_parts):
        # while elapsed_time < 20:
        # TODO tady je to blbě udělaný, abecedně se to předřazuje, musím dělníka přímo přiřadit k součástce a ne volně
        if workers - working != 0:
            buffer = sorted(
                [
                    x
                    for x in scheme.keys()
                    if scheme[x]["blocked_by"] == [] and scheme[x]["built"] == False
                ]
            )
            working = min(workers, len(buffer))
        for worker in range(working):
            # print("worker " + str(worker) + " working on part " + str(buffer[worker]))
            scheme[buffer[worker]]["time_to_build"] -= 1
            """print(
                "worker "
                + str(worker)
                + " working on part "
                + str(buffer[worker])
                + ", time left: "
                + str(scheme[buffer[worker]]["time_to_build"])
            )"""
            if scheme[buffer[worker]]["time_to_build"] == 0:
                scheme[buffer[worker]]["built"] = True
                order.append(buffer[worker])
                working -= 1
                for part in scheme[buffer[worker]]["needed_for"]:
                    scheme[part]["blocked_by"].pop(
                        scheme[part]["blocked_by"].index(buffer[worker])
                    )
        elapsed_time += 1
    print(elapsed_time, "".join(order))


part_two()


print("computed in " + str(time() - start) + " seconds")
