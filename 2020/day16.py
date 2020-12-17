from time import time
from collections import deque

start = time()

with open("day16input.txt", "r") as file_in:
    raw_rules, my_ticket, raw_nearby_tickets = [
        x for x in file_in.read().rstrip().split("\n\n")]
    rules = {}
    all_values = []
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

# print(nearby_tickets)
# print(find_grouped_valid())




def part_one():
    tser = 0  # ticket scanning error rate
    for ticket in nearby_tickets:
        tser += invalid_ticket(ticket, all_values)
    return tser


print(part_one())


def part_two():
    grouped_fields = find_grouped_valid()
    validated = []
    while True:
        for group in positions:
            for rule in rule_names:
                if rule in validated:
                    continue
                if not invalid_ticket(grouped_fields[group], rules[rule]):
                    validated.append(rule)
                    #print(group, rule)
                    break
        if len(validated) == len(rule_names):
            print("success")
            break
        else:
            validated = []
            print(rule_names[0])
            rule_names.rotate(1)
            break
    pass

print(part_two())


print("computed in " + str(time() - start) + " seconds")
