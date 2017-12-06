from time import time
start = time()

import re

ingredients = []


def parse_input(ingredient):
    cap, dur, fla, tex, cal = map(int, re.findall('-?\d+', ingredient))
    ingredients.append([cap, dur, fla, tex, cal])


def score_part_one(a, b, c):
    d = 100-a-b-c
    cap_score = a * ingredients[0][0] + b * ingredients[1][0] + c * ingredients[2][0] + d * ingredients[3][0]
    dur_score = a * ingredients[0][1] + b * ingredients[1][1] + c * ingredients[2][1] + d * ingredients[3][1]
    fla_score = a * ingredients[0][2] + b * ingredients[1][2] + c * ingredients[2][2] + d * ingredients[3][2]
    tex_score = a * ingredients[0][3] + b * ingredients[1][3] + c * ingredients[2][3] + d * ingredients[3][3]
    cal_score = a * ingredients[0][4] + b * ingredients[1][4] + c * ingredients[2][4] + d * ingredients[3][4]
    if (cap_score <= 0 or dur_score <= 0 or fla_score <= 0 or tex_score <= 0):
        return 0
    elif cal_score == 500:
        return cap_score*dur_score*fla_score*tex_score
    else:
        return 0

def part_one():
    with open('day15input.txt') as file:
        lines = file.read().rstrip().split('\n')

    for line in lines:
        parse_input(line)

    print(max(score_part_one(a, b, c) for a in range(101) for b in range(101) for c in range(101) if 0 <= a+b+c <= 100))



part_one()


runtime = time() - start
print("computed in " + str(runtime) + " seconds")