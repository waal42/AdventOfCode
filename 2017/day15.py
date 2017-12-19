from time import time

start = time()

start_a = 634
start_b = 301
test_start_a = 65
test_start_b = 8921
gen_a_factor = 16807
gen_b_factor = 48271
divisor = 2147483647


def solution():
    count_matches = 0
    a = start_a
    b = start_b
    for i in range(40000000):
        a = (a * gen_a_factor) % divisor
        b = (b * gen_b_factor) % divisor
        bin_a = bin(a)[-16:]
        bin_b = bin(b)[-16:]
        # print(bin_a)
        # print(bin_b)
        if  bin_a == bin_b:
            count_matches += 1
    print(count_matches)


def solution_two():
    count_matches = 0
    a = start_a
    b = start_b
    for i in range(5000000):
        a = (a * gen_a_factor) % divisor
        b = (b * gen_b_factor) % divisor
        while a % 4 != 0:
            a = (a * gen_a_factor) % divisor
        while b % 8 != 0:
            b = (b * gen_b_factor) % divisor
        # print(a, b)
        bin_a = bin(a)[-16:]
        bin_b = bin(b)[-16:]
        # print(bin_a)
        # print(bin_b)
        if  bin_a == bin_b:
            count_matches += 1
    print(count_matches)

solution_two()

print('finished in ' + str(time() - start) + ' seconds')