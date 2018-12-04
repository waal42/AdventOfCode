from time import time
from pprint import pprint
from collections import Counter
import re

start = time()

with open("day04input.txt") as fin:
    calendar = dict()
    for log in fin.read().rstrip().split("\n"):
        line = log.strip("[").split("] ")
        dtm = line[0].split(" ")
        if dtm[0] not in calendar.keys():
            calendar[dtm[0]] = dict()
        calendar[dtm[0]][dtm[1]] = line[1]
    schedule = dict()
    guard = 0
    start_sleep = 0
    end_sleep = 0
    for date in sorted(calendar.keys()):
        for clock in sorted(calendar[date].keys()):
            if "begins shift" in calendar[date][clock]:
                guard = int(
                    list(filter(None, re.findall(r"[0-9]*", calendar[date][clock])))[0]
                )
            if "falls asleep" in calendar[date][clock]:
                start_sleep = int(list(filter(None, re.findall(r"[0-9]*", clock)))[1])
            if "wakes up" in calendar[date][clock]:
                end_sleep = int(list(filter(None, re.findall(r"[0-9]*", clock)))[1])
                if guard not in schedule.keys():
                    schedule[guard] = list()
                for x in range(start_sleep, end_sleep):
                    schedule[guard].append(x)


def part_one():
    max_sleep = (0, 0, 0)
    for guard in schedule.keys():
        slept_for = len(schedule[guard])
        most_common_minute = max(set(schedule[guard]), key=schedule[guard].count)
        if slept_for > max_sleep[1]:
            max_sleep = (guard, slept_for, most_common_minute)
    print(
        "longest sleep had guard "
        + str(max_sleep[0])
        + " with length of "
        + str(max_sleep[1])
        + " minutes, most common minute being "
        + str(max_sleep[2])
    )
    print(max_sleep[0] * max_sleep[2])


def part_two():
    most_guard = 0
    most_common_minute = (0, 0)
    for guard in schedule.keys():
        this_common_minute = Counter(schedule[guard]).most_common(1)
        if this_common_minute[0][1] > most_common_minute[1]:
            most_common_minute = this_common_minute[0]
            most_guard = guard
    print(most_guard, most_common_minute, most_guard * most_common_minute[0])


part_one()
part_two()


print("computed in " + str(time() - start) + " seconds")
