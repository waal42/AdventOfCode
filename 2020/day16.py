from time import time
from collections import deque
from pprint import pprint

total_time = time()
parse_time = time()

with open("day16input.txt", "r") as file_in:
    raw_rules, raw_my_ticket, raw_nearby_tickets = [
        x for x in file_in.read().rstrip().split("\n\n")]
    rules = {}
    all_values = []
    my_ticket = raw_my_ticket.split("\n")[1].split(",")
    rule_names = deque()
    for rule in raw_rules.split("\n"):
        name = rule.split(": ")[0]
        rule_names.append(name)
        intervals = rule.split(": ")[1].split(" or ")
        rule_values = []
        for interval in intervals:
            boundaries = interval.split("-")
            rule_values += [x for x in range(int(boundaries[0]),
                                             int(boundaries[1]) + 1)]
        rules[name] = rule_values
        all_values += rule_values
        all_values = list(set(all_values))
        nearby_tickets = []
    positions = deque(x+1 for x in range(len(rule_names)))
    for raw_ticket in raw_nearby_tickets.split(":\n")[1].split("\n"):
        ticket = [int(x) for x in raw_ticket.split(",")]
        nearby_tickets.append(ticket)

print("parse time: " + str(time() - parse_time) + " seconds")


def invalid_ticket(ticket, values):
    invalidated = 0
    for field in ticket:
        if field not in values:
            invalidated += field
    return invalidated


def find_grouped_valid():
    grouped_fields = {}
    for ticket in nearby_tickets:
        if invalid_ticket(ticket, all_values):
            continue
        for i in range(len(ticket)):
            if i+1 not in grouped_fields:
                grouped_fields[i+1] = [ticket[i]]
            else:
                grouped_fields[i+1].append(ticket[i])
    return grouped_fields


part_one_time = time()


def part_one():
    tser = 0  # ticket scanning error rate
    for ticket in nearby_tickets:
        tser += invalid_ticket(ticket, all_values)
    return tser


print(part_one())

print("part one time: " + str(time() - part_one_time) + " seconds")

part_two_time = time()


def part_two():
    grouped_fields = find_grouped_valid()
    possible = {}
    for group in positions:
        for rule in rule_names:
            if not invalid_ticket(grouped_fields[group], rules[rule]):
                if rule not in possible.keys():
                    possible[rule] = [group]
                else:
                    possible[rule].append(group)
    remove = []
    solution = {}
    product = 1
    for length in range(1, 21):
        for rule in possible.keys():
            if length == len(possible[rule]):
                to_solution = [item for item in possible[rule]
                               if item not in remove][0]
                if rule.split(" ")[0] == "departure":
                    product *= int(my_ticket[to_solution - 1])
                remove.append(to_solution)
                solution[rule] = to_solution
    return product


pprint(part_two())

print("part two time: " + str(time() - part_two_time) + " seconds")


print("total time: " + str(time() - total_time) + " seconds")
