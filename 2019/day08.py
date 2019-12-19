from time import time
from math import floor

start = time()

with open("day08input.txt", "r") as file_in:
    pixels = list(file_in.read().rstrip('\n'))
    

width = 25
heigth = 6
layer_size = width * heigth

def part_one():
    solution = {'zeroes' : width, 'position' : (0,0), 'layer' : []}
    for layer in range(int(len(pixels)/(layer_size))):
        pixel_layer = pixels[layer * layer_size : layer * layer_size + layer_size]
        if pixel_layer.count('0') < solution['zeroes']:
            solution['zeroes']  = pixel_layer.count('0')
            solution['position'] = (layer)
            solution['layer'] = pixel_layer
    print(solution['layer'].count('1')*solution['layer'].count('2'))
    

part_one()


def part_two():
    picture = [['.' for x in range(width)] for y in range(heigth)]
    for layer in range(int(len(pixels)/(layer_size))):
        pixel_layer = pixels[layer * layer_size : layer * layer_size + layer_size]
        for row in range(heigth):
            this_row = pixel_layer[row * width : row * width + width]
            for column in range(width):
                if picture[row][column] == '.':
                    if this_row[column] == '0':
                        picture[row][column] = 'X'
                    elif this_row[column] == '1':
                        picture[row][column] = ' '
    for row in picture:
        print(''.join(row))
part_two()

print("computed in " + str(time() - start) + " seconds")
