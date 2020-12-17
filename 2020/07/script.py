import os
import re


def disassemble_rule(text):
    S = text.split("contain ")
    outer_bag_color = re.search(r'^[a-z]+\s[a-z]+', S[0])[0]

    inner_bags = []
    Inner_bags = S[1].split(", ")
    for inner in Inner_bags:
        inner.replace(".\n", "")

        qty = re.search(r'[0-9]+', inner)
        if qty != None:
            qty = int(qty[0])
            color = re.search(r'[a-z]+\s[a-z]+', inner)[0]
        else:   # no other bags
            qty = 0
            color = None

        possibility = dict()
        possibility['qty'] = qty
        possibility['color'] = color
    
        if qty != 0:
            inner_bags.append(possibility)

    return {
        'outer' : outer_bag_color,
        'inner' : inner_bags
    }


def can_contain_color(color_out, color_in):
    found = False
    for rule in rules:
        if rule['outer'] == color_out:
            for inside in rule['inner']:
                found = found or inside['color'] == color_in or can_contain_color(inside['color'], color_in)
    return found


def count_inner_bags(color_out):
    count = 0
    for rule in rules:
        if rule['outer'] == color_out:
            for inside in rule['inner']:
                count += inside['qty'] + inside['qty'] * count_inner_bags(inside['color'])
    return count



# main

f = open(os.getcwd() + "/2020/7/input.txt", "r")
Lines = f.readlines()

rules = []
for line in Lines:
    rules.append(disassemble_rule(line))


# part 1

count = 0
my_color = "shiny gold"
already_processed_colors = []
for rule in rules:
    if rule['outer'] not in already_processed_colors:
        count += can_contain_color(rule['outer'], my_color)
        already_processed_colors.append(rule['outer'])

print("part 1: " + str(count))


# part 2
print("part 2: " + str(count_inner_bags(my_color)))