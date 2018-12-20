from time import time

start = time()


def runGenerations(rules, plants, iterations):
    for generation in range(iterations):
        lowestPlant = min(plants)
        highestPlant = max(plants)
        lastPossible = highestPlant - lowestPlant + 7
        pots = "".join(
            [
                "#" if i in plants else "."
                for i in range(lowestPlant - 4, highestPlant + 5)
            ]
        )
        plants = []
        for i in range(2, lastPossible):
            if rules[pots[i - 2 : i + 3]]:
                plants.append(i - 4 + lowestPlant)
    return sum(plants)


with open("day12input.txt") as inFile:
    lines = inFile.read().splitlines()
    plants = [i for i, c in enumerate(lines[0][15:]) if c == "#"]
    rules = dict((line[:5], line[9] == "#") for line in lines[2:])

print("Part 1:", runGenerations(rules, plants, 20))
score199 = runGenerations(rules, plants, 199)
score200 = runGenerations(rules, plants, 200)
constantIncrease = score200 - score199
print(
    "Part 2:",
    runGenerations(rules, plants, 200) + ((50000000000 - 200) * constantIncrease),
)


print("computed in " + str(time() - start) + " seconds")
