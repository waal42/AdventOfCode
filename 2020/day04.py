from time import time

start = time()

with open("day04input.txt", "r") as file_in:
    passports = [x.replace("\n", " ").split(" ")
                 for x in file_in.read().rstrip().split("\n\n")]

pass_dict = list()

for passport in passports:
    this_passport = dict()
    for field in passport:
        this_passport[field.split(":")[0]] = field.split(":")[1]
    pass_dict.append(this_passport)

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def part_one():
    valid_passports = 0
    for passport in pass_dict:
        count_fields = 0
        for field in required_fields:
            if field in passport.keys():
                count_fields += 1
        if count_fields == len(required_fields):
            valid_passports += 1
    return valid_passports


# print(part_one())


def isBirthYear(byr):
    if len(byr) != 4:
        return False
    for char in byr:
        if char not in '0123456789':
            return False
    if 1920 <= int(byr) <= 2002:
        return True
    else:
        return False


def isIssueYear(iyr):
    if len(iyr) != 4:
        return False
    for char in iyr:
        if char not in '0123456789':
            return False
    if 2010 <= int(iyr) <= 2020:
        return True
    else:
        return False


def isExpirationYear(eyr):
    if len(eyr) != 4:
        return False
    for char in eyr:
        if char not in '0123456789':
            return False
    if 2020 <= int(eyr) <= 2030:
        return True
    else:
        return False


def isHeight(hgt):
    if hgt[-2:] == 'cm':
        if 150 <= int(hgt[:-2]) <= 193:
            return True
        else:
            return False
    elif hgt[-2:] == 'in':
        if 59 <= int(hgt[:-2]) <= 76:
            return True
        else:
            return False
    else:
        return False


def isHairColor(hcl):
    if len(hcl) != 7:
        return False
    if hcl[0] != '#':
        return False
    for char in hcl[1:]:
        if char not in '0123456789abcdefABCDEF':
            return False
    return True


def isEyeColor(ecl):
    if ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    else:
        return False


def isPassportID(pid):
    if len(pid) == 9:
        return True
    else:
        return False


def part_two():
    valid_passports = 0
    for passport in pass_dict:
        if 'byr' in passport.keys() and isBirthYear(passport['byr']):
            if 'iyr' in passport.keys() and isIssueYear(passport['iyr']):
                if 'eyr' in passport.keys() and isExpirationYear(passport['eyr']):
                    if 'hgt' in passport.keys() and isHeight(passport['hgt']):
                        if 'hcl' in passport.keys() and isHairColor(passport['hcl']):
                            if 'ecl' in passport.keys() and isEyeColor(passport['ecl']):
                                if 'pid' in passport.keys() and isPassportID(passport['pid']):
                                    valid_passports += 1
    return valid_passports


print(part_two())


print("computed in " + str(time() - start) + " seconds")
