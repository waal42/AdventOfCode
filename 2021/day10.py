from time import time

start = time()

in_time = time()
with open("day10input.txt", "r") as file_in:
    navigation = [line for line in file_in.read().rstrip().split("\n")]
print("input processed in " + str(time() - in_time) + " seconds")

openings = '([{<'
closings = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

unfinished_lines = list()


def part_one():
    corrupted_symbols = list()
    for line in navigation:
        to_close = list()
        to_append = True
        for symbol in line:
            if symbol in openings:
                to_close.append(symbol)
            else:
                if symbol == closings[to_close[-1]]:
                    to_close.pop()
                else:
                    corrupted_symbols.append(symbol)
                    to_append = False
                    break
        if to_append:
            unfinished_lines.append(to_close)
    score = 0
    for symbol in corrupted_symbols:
        if symbol == ")":
            score += 3
        elif symbol == "]":
            score += 57
        elif symbol == "}":
            score += 1197
        elif symbol == ">":
            score += 25137
    return score


def part_two():
    scores = list()
    for line in unfinished_lines:
        score = 0
        for symbol in reversed(line):
            score *= 5
            if symbol == "(":
                score += 1
            elif symbol == "[":
                score += 2
            elif symbol == "{":
                score += 3
            elif symbol == "<":
                score += 4
        scores.append(score)
    return sorted(scores)[int(len(scores)/2)]


first = time()
print(part_one())
print("part one computed in " + str(time() - first) + " seconds")
second = time()
print(part_two())
print("part two computed in " + str(time() - second) + " seconds")

print("completely computed in " + str(time() - start) + " seconds")
