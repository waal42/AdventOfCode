from time import time
from collections import deque
from math import sin, cos, radians, pi


start = time()

with open("day12input.txt", "r") as file_in:
    actions = [(x[0], int(x[1:])) for x in file_in.read().rstrip().split("\n")]

move_in_direction = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

def perform_action(x, y, action, orientation):
    if action[0] in 'NESW':
        x += action[1]*move_in_direction[action[0]][0]
        y += action[1]*move_in_direction[action[0]][1]
    elif action[0] == 'F':
        x += action[1]*move_in_direction[orientation[0]][0]
        y += action[1]*move_in_direction[orientation[0]][1]
    elif action[0] == 'L':
        angle = action[1]
        while angle != 0:
            orientation.rotate(-1)
            angle -= 90
    elif action[0] == 'R':
        angle = action[1]
        while angle != 0:
            orientation.rotate(1)
            angle -= 90
    return x, y, orientation



def part_one():
    x, y = 0, 0
    orientation = deque(['E', 'N', 'W', 'S'])
    for action in actions:
        x, y, orientation = perform_action(x, y, action, orientation)
    return abs(x) + abs(y)

print(part_one())


def perform_action_for_real_this_time(x_ship, y_ship, x_waypoint, y_waypoint, action):
    x_waypoint_new = x_waypoint
    y_waypoint_new = y_waypoint
    if action[0] == 'F':
        x_ship += action[1]*x_waypoint
        y_ship += action[1]*y_waypoint
    elif action[0] in 'NESW':
        x_waypoint_new += action[1]*move_in_direction[action[0]][0]
        y_waypoint_new += action[1]*move_in_direction[action[0]][1]
    else:
        angle = radians(action[1])
        if action[0] == 'R':
            angle = -angle
        x_waypoint_new = round(cos(angle) * x_waypoint - sin(angle)*y_waypoint)
        y_waypoint_new = round(sin(angle) * x_waypoint + cos(angle)*y_waypoint)
    return x_ship, y_ship, x_waypoint_new, y_waypoint_new



def part_two():
    x_ship = 0
    y_ship = 0
    x_waypoint = 10
    y_waypoint = 1
    for action in actions:
        x_ship, y_ship, x_waypoint, y_waypoint = perform_action_for_real_this_time(x_ship, y_ship, x_waypoint, y_waypoint, action)
    return abs(x_ship) + abs(y_ship)


print(part_two())


print("computed in " + str(time() - start) + " seconds")
