from time import time
from math import floor

start = time()

with open("day02input.txt", "r") as file_in:
    list_of_passwords = [x for x in file_in.read().rstrip().split("\n")]

passwords = list()
for password in list_of_passwords:
    this_password = dict()
    splitted = password.split(" ")
    limits = splitted[0].split("-")
    this_password["min"] = int(limits[0])
    this_password["max"] = int(limits[1])
    this_password["required"] = splitted[1].rstrip(":")
    this_password["password"] = splitted[2]
    passwords.append(this_password)


def part_one():
    valid_passwords = 0
    for password in passwords:
        occurances = password["password"].count(password["required"])
        if password["min"] <= occurances <= password["max"]:
            valid_passwords += 1
            password["valid"] = True
        else:
            password["valid"] = False
    return valid_passwords

# print(part_one())

def part_two():
    valid_passwords = 0
    for password in passwords:
        first = password["min"]
        second = password["max"]
        letter = password["required"]
        pwd = password["password"]
        positions = pwd[first - 1] + pwd[second - 1]
        if positions.count(letter) == 1:
            valid_passwords += 1
            password["valid"] = True
        else:
            password["valid"] = False
    return valid_passwords


print(part_two())

print("computed in " + str(time() - start) + " seconds")
