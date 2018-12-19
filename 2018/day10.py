from time import time
import re
from pprint import pprint

start = time()

points = dict()
previous_height = 2000000
borders = {"min_x": 1000000, "max_x": -1000000, "min_y": 1000000, "max_y": -1000000}
coords = list()

with open("day10input.txt") as fin:
    i = 0
    for line in fin:
        tmp = list(filter(None, re.findall(r"[-+]?\d*", line)))
        points[i] = {
            "pos_x": int(tmp[0]),
            "pos_y": int(tmp[1]),
            "vel_x": int(tmp[2]),
            "vel_y": int(tmp[3]),
        }
        borders["min_x"] = min(borders["min_x"], points[i]["pos_x"])
        borders["max_x"] = max(borders["max_x"], points[i]["pos_x"])
        borders["min_y"] = min(borders["min_y"], points[i]["pos_y"])
        borders["max_y"] = max(borders["max_y"], points[i]["pos_y"])

        coords.append((points[i]["pos_x"], points[i]["pos_y"]))
        i += 1
    current_height = borders["min_y"] - borders["max_y"]
    # pprint(points)

seconds = 0
while True:
    if abs(current_height) <= 11:
        print("")
        for y in range(borders["min_y"], borders["max_y"] + 1):
            draw = []
            for x in range(borders["min_x"], borders["max_x"] + 1):
                if (x, y) in coords:
                    draw.append("#")
                else:
                    draw.append(" ")
            print("".join(draw))
        print("")
        print("waited " + str(seconds) + " seconds")
        break
    previous_height = current_height
    borders = {"min_x": 1000000, "max_x": -1000000, "min_y": 1000000, "max_y": -1000000}
    coords = list()
    for i in points.keys():
        points[i]["pos_x"] += points[i]["vel_x"]
        points[i]["pos_y"] += points[i]["vel_y"]
        borders["min_x"] = min(borders["min_x"], points[i]["pos_x"])
        borders["max_x"] = max(borders["max_x"], points[i]["pos_x"])
        borders["min_y"] = min(borders["min_y"], points[i]["pos_y"])
        borders["max_y"] = max(borders["max_y"], points[i]["pos_y"])
        coords.append((points[i]["pos_x"], points[i]["pos_y"]))
    current_height = borders["min_y"] - borders["max_y"]
    seconds += 1


print("computed in " + str(time() - start) + " seconds")
