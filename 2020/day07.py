from time import time
from pprint import pprint

start = time()

luggage_rules = {}

with open("day07input.txt", "r") as file_in:
    for rule in file_in.read().rstrip().split('\n'):
        this_bag = rule.split(' bags contain ')
        luggage_rules[this_bag[0]] = {}
        if 'no other' not in this_bag[1]:
            luggage_rules[this_bag[0]] = {}
            for inside in this_bag[1].split(','):
                inside_list = inside.strip().split(' ')
                luggage_rules[this_bag[0]][' '.join(
                    inside_list[1:3])] = int(inside_list[0])
        else:
            luggage_rules[this_bag[0]] = False

# pprint(luggage_rules)

def get_insides(luggage, insides):
    # print(luggage, insides)
    if luggage_rules[luggage]:
        for in_luggage in luggage_rules[luggage].keys():
            insides + get_insides(in_luggage, insides)
            insides.append(in_luggage)
    else:
        insides = []
    return insides

luggage_tree = dict()
for luggage in luggage_rules.keys():
    insides = list()
    luggage_tree[luggage] = get_insides(luggage, insides)

# pprint(luggage_tree)

def part_one(bag_to_find):
    options = 0
    for luggage in luggage_tree.keys():
        if bag_to_find in luggage_tree[luggage]:
            options += 1
    return options


print(part_one('shiny gold'))

def count_insides(luggage, expr):
    if luggage_rules[luggage]:
        expr.append("(")
        for in_luggage in luggage_rules[luggage].keys():
            expr + count_insides(in_luggage, expr)
            expr.append(str(luggage_rules[luggage][in_luggage]))
            expr.append("+")
        expr.pop()
        expr.append(")")
        expr.append("*")
    else:
        expr = []
    return expr


def part_two():
    expr = count_insides("shiny gold", [])
    new_expr = []
    index = 1 # zbaveni se prvni zavorky
    while index < len(expr):
        if expr[index] == ')' and expr[index + 1] == '*':
            new_expr.append('+1') # kdyz za zavorkou nasobim, tak pred ni pripocitam prdchozi kufr
            new_expr.append(expr[index])
            new_expr.append(expr[index + 1])
            index += 2
        else:
            new_expr.append(expr[index])
            index += 1
    str_new_expr = ''.join(new_expr[:-3]) # osklive zbaveni se +1)* na konci
    return str_new_expr


print(eval(part_two()))


print("computed in " + str(time() - start) + " seconds")
