from time import time
from collections import defaultdict, deque

start = time()

players = 424
marbles = 7114400
circle = deque([0])
scores = defaultdict(int)


for marble in range(1, marbles + 1):
    length = len(circle)
    if marble % 23 == 0:
        circle.rotate(7)
        scores[marble % players] += marble + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)

max_score = max(scores.values())

print(max_score)


print("computed in " + str(time() - start) + " seconds")
