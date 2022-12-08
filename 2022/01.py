import utils

DAY = 1

calories = utils.read_input(DAY)
elves = []
temp = 0

for cal in calories:
    if cal == '':
        elves.append(temp)
        temp = 0
    else:
        temp += int(cal)

elves.sort()

utils.print_answer(1, elves[-1])
utils.print_answer(2, elves[-1] + elves[-2] + elves[-3])
