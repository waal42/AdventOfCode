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
    workers = dict()
    workers_num = 5
    elapsed_time = 0
    time_to_build = 60
    for worker in range(workers_num):
        workers[worker] = {"working": False, "working_on": ""}
    for item in sorted_parts:
        scheme[item] = {
            "needed_for": [],
            "blocked_by": [],
            "built": False,
            "in_progress": False,
            "time_to_build": time_to_build + ord(item) - 64,
        }
    for instr in instructions:
        scheme[instr[0]]["needed_for"].append(instr[1])
        scheme[instr[1]]["blocked_by"].append(instr[0])
        blocked.append(instr[1])
    # pprint(scheme)
    while len(order) != len(sorted_parts):
        free_workers = [x for x in workers.keys() if workers[x]["working"] == False]
        if len(free_workers) != 0:
            buffer = sorted(
                [
                    x
                    for x in scheme.keys()
                    if (
                        scheme[x]["blocked_by"] == []
                        and scheme[x]["built"] == False
                        and scheme[x]["in_progress"] == False
                    )
                ]
            )
            # print("free workers: " + str(free_workers) + ", buffer: " + str(buffer))
            to_assign = min(len(free_workers), len(buffer))
            for worker in range(to_assign):
                workers[free_workers[worker]]["working"] = True
                workers[free_workers[worker]]["working_on"] = buffer[worker]
                scheme[buffer[worker]]["in_progress"] = True
        working_workers = [x for x in workers.keys() if workers[x]["working"] == True]
        # print(elapsed_time, working_workers, free_workers)
        for worker in working_workers:
            """print(
                "worker "
                + str(worker)
                + " working on part "
                + str(workers[worker]["working_on"])
                + " with time to built being "
                + str(scheme[workers[worker]["working_on"]]["time_to_build"])
                + " seconds"
            )"""
            scheme[workers[worker]["working_on"]]["time_to_build"] -= 1
            if scheme[workers[worker]["working_on"]]["time_to_build"] == 0:
                scheme[workers[worker]["working_on"]]["built"] = True
                scheme[workers[worker]["working_on"]]["in_progress"] = False
                order.append(workers[worker]["working_on"])
                for part in scheme[workers[worker]["working_on"]]["needed_for"]:
                    scheme[part]["blocked_by"].pop(
                        scheme[part]["blocked_by"].index(workers[worker]["working_on"])
                    )
                workers[worker]["working"] = False
                workers[worker]["working_on"] = ""
        elapsed_time += 1
    print(elapsed_time, "".join(order))


part_two()


print("computed in " + str(time() - start) + " seconds")
