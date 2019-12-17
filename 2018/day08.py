from time import time
from pprint import pprint

start = time()

with open("day08input.txt") as fin:
    data = [int(x) for x in fin.read().split(" ")]


def parse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = list()
    totals = 0
    for i in range(children):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:],
        )


total, value, remaining = parse(data)

print("part1: ", total)
print("part2: ", value)


print("computed in " + str(time() - start) + " seconds")