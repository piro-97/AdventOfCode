import os


# part 1

f = open(os.getcwd() + "/2/input.txt", "r")
lines = f.readlines()

count = 0

for line in lines:
    l = line.split(" ")      # i.e. l = ["1-3", "a:", "asdfgh"]
    
    occurr = l[0].split("-")
    min_occurr = int(occurr[0])
    max_occurr = int(occurr[1])

    letter = l[1][0]

    string = l[2]

    letter_occurr_in_string = string.count(letter)

    if(letter_occurr_in_string >= min_occurr 
    and letter_occurr_in_string <= max_occurr):
        count += 1

print("part1: " + str(count))


# part 2

count = 0

for line in lines:
    l = line.split(" ")      # i.e. l = ["1-3", "a:", "asdfgh"]
    
    occurr = l[0].split("-")
    first_occur = int(occurr[0]) - 1
    second_occur = int(occurr[1]) - 1

    letter = l[1][0]

    string = l[2]


    found = 0
    if(string[first_occur] == letter):
        found += 1
    if(string[second_occur] == letter):
        found += 1
    
    if(found == 1):
        count += 1

print("part2: " + str(count))