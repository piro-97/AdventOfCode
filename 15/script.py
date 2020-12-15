import os

def solve(goal):
    current_turn = 1
    last_number = -1
    last_appearance = {}
    while current_turn != goal + 1:

        # read input
        if current_turn <= len(input_numbers):
            current_number = int(input_numbers[current_turn-1])

        else:
            try:        # last number has already been said
                current_number = current_turn - 1 - last_appearance[last_number]

            except:     # first time a number is said
                current_number = 0

        # save previous number
        last_appearance[last_number] = current_turn - 1
        last_number = current_number

        current_turn += 1
    
    return current_number


f = open(os.getcwd() + "/15/input.txt", "r")
Lines = f.readlines()
input_numbers = Lines[0].split(",")

print('part 1: ', str(solve(2020)))
print('part 2: ', str(solve(30000000)))