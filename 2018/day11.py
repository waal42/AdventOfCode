from time import time

start = time()


def cell_power_level(x, y, ser_no):
    return int(str((y * (x + 10) + ser_no) * (x + 10))[-3]) - 5


serial_number = 7403
largest_total_power = 0
current_position = (0, 0, 0)
grid = dict()

# populating grid
for y in range(1, 301):
    for x in range(1, 301):
        grid[(x, y)] = cell_power_level(x, y, serial_number)

for square in range(1, 301):
    for y in range(1, 301 - square + 1):
        for x in range(1, 301 - square + 1):
            this_total_power = 0
            for sq_y in range(square):
                for sq_x in range(square):
                    this_total_power += grid[(x + sq_x, y + sq_y)]
            if this_total_power > largest_total_power:
                largest_total_power = this_total_power
                current_position = (x, y, square)
    print(largest_total_power, current_position)    

print(largest_total_power, current_position)


print("computed in " + str(time() - start) + " seconds")
