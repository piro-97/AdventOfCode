import os
import re

class Rule:
    def __init__(self, line):
        parts = line.replace(" ", "").split(":")
        self.name = parts[0]
        valid = re.findall(r'\d+', parts[1])
        self.interval1 = [int(valid[0]), int(valid[1])]
        self.interval2 = [int(valid[2]), int(valid[3])]
        
    def match_against_rule(self, value):
        return  self.interval1[0] <= value <= self.interval1[1] or \
                self.interval2[0] <= value <= self.interval2[1]

class Ticket:
    def __init__(self, line):
        self.values = list(int(x) for x in re.findall(r'\d+', line))


def find_valid_position(my_list, value, assignments):
 indexes = [item for item in range(0,len(my_list)) if item not in [*assignments]]
 
 possibilities = []
 for index in indexes:
    if value not in my_list[index]:
        possibilities.append(index)
 
 return possibilities


def find_valid_matching(my_list, all_values):
    solved = False
    positions_ok = []
    assignments = {}
    
    while not solved:
        for i in range(0,len(all_values)):
            if all_values[i] not in list(assignments.values()):
                curr_val = all_values[i]
                poss = find_valid_position(my_list, curr_val, assignments)

                if len(poss) == 1:
                    assignments[poss[0]] = curr_val
                    positions_ok.append(poss[0])
                
                if len(poss) == 0:
                    print('ERROR')
        
         
        if len(positions_ok) == len(all_values):
         solved = True
                 
    return assignments



f = open(os.getcwd() + "/16/input.txt", "r")
Lines = f.readlines()

rules = []
section = 0
my_ticket = None
nearby_tickets = []
for line in Lines:
    line = line.replace("\n", "")

    if line == "your ticket:":
        section = 1

    elif line == "nearby tickets:":
        section = 2
    
    elif len(line) != 0:

        if section == 0:
            rules.append(Rule(line))
        
        if section == 1:
            my_ticket = Ticket(line)

        if section == 2:
            nearby_tickets.append(Ticket(line))


# part 1

invalid_fields = []
for ticket in nearby_tickets:
    for val in ticket.values:
        if not any(rule.match_against_rule(val) for rule in rules):
            invalid_fields.append(val)

print("part 1:", sum(invalid_fields))


# part 2

valid_tickets = list(nearby_tickets)
for ticket in nearby_tickets:
    for val in ticket.values:
        if not any(rule.match_against_rule(val) for rule in rules):
            valid_tickets.remove(ticket)

rule_field_association = []
for rule in rules:
    for ticket in valid_tickets:
        for idx, val in enumerate(ticket.values):
            
            if len(rule_field_association) <= idx:
                rule_field_association.append([])
            
            if not rule.match_against_rule(val) and rule.name not in rule_field_association[idx]:
                rule_field_association[idx].append(rule.name)

vals = list(rule.name for rule in rules)
matching = find_valid_matching(rule_field_association, vals)

product = 1
for key, value in matching.items():
    if re.match("^departure", value) != None:
        product *= my_ticket.values[key]

print("part 2:", product)