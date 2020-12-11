import os
import re

def check_single_field(field, value):
    pattern = ""

    if field == "byr":
        return 1920 <= int(value) <= 2002
    
    if field == "iyr":
        return 2010 <= int(value) <= 2020
    
    if field == "eyr":
        return 2020 <= int(value) <= 2030
    
    if field == "hgt":
        kind = value[len(value) - 2 :]
        val = value[: len(value) - 2]
        if kind == "cm":
            return 150 <= int(val) <= 193
        if kind == "in":
            return 59 <= int(val) <= 76 
        return False
    
    if field == "hcl":
        pattern = re.compile("^#([0-9]|[a-f]){6}$")
        return pattern.match(value) != None

    if field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    if field == "pid":
        pattern = re.compile("^[0-9]{9}$")
        return pattern.match(value) != None

    if field == "cid":
        return True

    return False
    

def check_validity(passport, complete_val):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # without "cid"

    splitted_passport = passport.split(" ")     # ['ecl:#eef340', 'eyr:2023', ..., '']

    fields_in_pass = []
    value_of_field = []
    for sp in splitted_passport:
        s = sp.split(":")
        if (s[0] != ""):
            fields_in_pass.append(s[0])
            value_of_field.append(s[1]) 


    for f in fields:
        if not any(f in s for s in fields_in_pass):
            return 0
        
    if complete_val:
        i = 0
        while (i < len(fields_in_pass)):
            if not check_single_field(fields_in_pass[i], value_of_field[i]):
                print(fields_in_pass[i])
                print(value_of_field[i])
                return 0
            i += 1
        return 1
    else:
        return 1


# part 1 + 2

f = open(os.getcwd() + "/4/input.txt", "r")
Lines = f.readlines()

count1 = 0
count2 = 0
passport = ""
for line in Lines:
    
    if line != "\n":                # string is not over
        passport += line.replace("\n", " ")
    
    else:                           # string is over ('\n' found!)
        if check_validity(passport, False):
            count1 += 1

        if check_validity(passport, True):
            count2 += 1
        
        passport = ""

print("part 1: " + str(count1))
print("part 2: " + str(count2))