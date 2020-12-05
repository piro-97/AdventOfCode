import os


# part 1

f = open(os.getcwd() + "/5/input.txt", "r")
Lines = f.readlines()

ids = []
for line in Lines:

    row_str = line[:7].replace("F", "0").replace("B", "1")
    col_str = line[7:].replace("L", "0").replace("R", "1")

    row = int(row_str, 2)
    col = int(col_str, 2)

    ids.append(row * 8 + col)

max_id = max(ids)
print("part1: " + str(max_id))


# part 2

FIRST_ROW_SEAT = 7
LAST_ROW_SEAT = 127 * 8

all_ids = list(range(max_id))
missing_ids = list(set(all_ids) - set(ids))

for plausible_id in missing_ids:

    if  plausible_id > FIRST_ROW_SEAT and \
        plausible_id < LAST_ROW_SEAT and \
        plausible_id - 1 not in missing_ids and \
        plausible_id + 1 not in missing_ids:

        my_seat_id = plausible_id

print("part2: " + str(my_seat_id))
