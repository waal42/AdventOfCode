from time import time
from copy import deepcopy

start = time()

with open("day11input.txt", "r") as file_in:
    seats = [list(x) for x in file_in.read().rstrip().split("\n")]


def print_current_seats(seats):
    for line in seats:
        print(''.join(line))
    pass



def get_adjacent_seats(x, y, height, width, seats):
    count_occupied = 0
    for local_y in range(max(0, y-1), min(height, y+2)):
        for local_x in range(max(0, x-1), min(width, x+2)):
            if seats[local_y][local_x] == '#':
                count_occupied += 1 
    if seats[y][x] == '#':
        count_occupied -= 1
    return count_occupied

def part_one():
    # print_current_seats(seats)
    height = len(seats)
    width = len(seats[0])
    stabilized = False
    previous_occupied = 0
    current_seats = seats
    while not stabilized:
        new_seats = deepcopy(current_seats)
        total_occupied = 0
        for y in range(height):
            for x in range(width):
                occupied = get_adjacent_seats(x, y, height, width, current_seats)
                if current_seats[y][x] == 'L' and occupied == 0:
                    new_seats[y][x] = '#'
                    total_occupied += 1
                elif current_seats[y][x] =='#':
                    if occupied >= 4:
                        new_seats[y][x] = 'L'
                    else:
                        total_occupied += 1
        # print_current_seats(new_seats)
        # print(previous_occupied, total_occupied)
        if total_occupied == previous_occupied:
            stabilized = True
        previous_occupied = total_occupied
        current_seats = new_seats
    return total_occupied              
    
print(part_one())

directions = { # pohyb ve vsech osmi smerech v promennych (y, x)
    'up': (-1, 0),
    'up_right': (-1, 1),
    'right': (0, 1),
    'down_right': (1, 1),
    'down': (1, 0),
    'down_left': (1, -1),
    'left': (0, -1),
    'up_left': (-1, -1)
}

def get_visible_seats(x, y, height, width, seats):
    count_occupied = 0
    for direction in directions:
        local_y = y
        local_x = x
        any_seat = False
        while 0 <= local_x < width and 0 <= local_y < height and not any_seat:
            local_y += directions[direction][0]
            local_x += directions[direction][1]
            if local_x == width or local_y == height or local_x == -1 or local_y == -1:
                break
            if seats[local_y][local_x] != '.':
                any_seat = True
                if seats[local_y][local_x] == '#':
                    count_occupied += 1
    return count_occupied


# print_current_seats(seats)
# print(get_visible_seats(0, 9, len(seats), len(seats[0]), seats))    
        

def part_two():
    height = len(seats)
    width = len(seats[0])
    stabilized = False
    previous_occupied = 0
    current_seats = seats
    while not stabilized:
        new_seats = deepcopy(current_seats)
        total_occupied = 0
        for y in range(height):
            for x in range(width):
                occupied = get_visible_seats(x, y, height, width, current_seats)
                if current_seats[y][x] == 'L' and occupied == 0:
                    new_seats[y][x] = '#'
                    total_occupied += 1
                elif current_seats[y][x] =='#':
                    if occupied >= 5:
                        new_seats[y][x] = 'L'
                    else:
                        total_occupied += 1
        # print_current_seats(new_seats)
        # print(previous_occupied, total_occupied)
        if total_occupied == previous_occupied:
            stabilized = True
        previous_occupied = total_occupied
        current_seats = new_seats
    return total_occupied

print(part_two())


print("computed in " + str(time() - start) + " seconds")
