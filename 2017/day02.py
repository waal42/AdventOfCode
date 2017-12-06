from time import time
import csv

start = time()


def load_input(input_file):
    with open('day02input.csv') as fin:
        my_list = [list(map(int, rec)) for rec in csv.reader(fin)]
        return my_list


def extremes_diff(num_list):
    small = min(x for x in num_list)
    big = max(x for x in num_list)
    return big - small


def even_division(num_list):
    len_num_list = len(num_list)
    for i in range(len_num_list):
        for j in range(len_num_list):
            if i == j:
                break
            else:
                x, y = num_list[i], num_list[j]
                if x > y and x % y == 0:
                    return x // y
                if x < y and y % x == 0:
                    return y // x


def part_one():
    my_input = load_input('day02input.csv')
    checksum = 0
    for row in my_input:
        checksum += extremes_diff(row)
    print(checksum)


def part_two():
    my_input = load_input('day02input.csv')
    checksum = 0
    for row in my_input:
        checksum += even_division(row)
    print(checksum)


part_one()
part_two()

runtime = time() - start
print('finished in ' + str(runtime) + ' seconds')