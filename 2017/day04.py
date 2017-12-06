from time import time
from itertools import permutations
start = time()

with open('day04input.txt') as fin:
    passwords = [word.split(' ') for word in fin.read().rstrip().split('\n')]


def part_one():
    valid_passwords = 0
    for passphrase in passwords:
        valid = True
        len_passphrase = len(passphrase)
        for i in range(len_passphrase):
            repeat = 0
            for j in range(len_passphrase):
                if passphrase[i] == passphrase[j]:
                    repeat += 1
            if repeat > 1:
                valid = False
        if valid:
            valid_passwords += 1
    print(valid_passwords)


def part_two():
    valid_passwords = 0
    for passphrase in passwords:
        valid = True
        len_passphrase = len(passphrase)
        for i in range(len_passphrase):
            for j in range(len_passphrase):
                if i == j:
                    break
                if passphrase[i] in [''.join(x) for x in list(permutations(passphrase[j]))]:
                    valid = False
        if valid:
            valid_passwords += 1
    print(valid_passwords)


part_two()

runtime = time() - start
print('finished in ' + str(runtime) + ' seconds')