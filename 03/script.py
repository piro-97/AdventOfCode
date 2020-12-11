import os

f = open(os.getcwd() + "/3/input.txt", "r")
Lines = f.readlines()


def count_trees(lines, right_slope, down_slope):
    trees = 0
    curr_pos_x = 0
    curr_pos_y = 0


    while (curr_pos_y < len(lines)):
        line = lines[curr_pos_y]
        
        if (line[curr_pos_x] == "#") :
            trees += 1
        
        curr_pos_x = (curr_pos_x + right_slope) % len(line)
        curr_pos_y += down_slope
    return trees


# part 1

result_1 = count_trees(Lines, 3, 1)
    
print("part 1: " + str(result_1))


# part 2

Counts = []
Counts.append(count_trees(Lines, 1, 1))
Counts.append(count_trees(Lines, 3, 1))
Counts.append(count_trees(Lines, 5, 1))
Counts.append(count_trees(Lines, 7, 1))
Counts.append(count_trees(Lines, 1, 2))

result_2 = 1
for c in Counts:
    result_2 *= c
    
print("part 2: " + str(result_2))