import os
import copy

class Seat:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def find_adjacents(self):  # returns [(x,y), ...] of adjacents seats
        l = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0 <= self.x + i < len(seats) and 0 <= self.y + j < len(seats[self.x]) and \
                    (0 != i or 0 != j): 
                        l.append([self.x + i, self.y + j])
        return l

    def find_first_visible(self, seats, direction):   # returns (x,y), ... of visible seat in the given direction
        if direction == "TL": # top left
            i = j = -1
        if direction == "TC": # top center
            i = -1
            j = 0
        if direction == "TR": # top right
            i = -1
            j = +1
        if direction == "BL": # boottom left
            i = +1
            j = -1
        if direction == "BC": # bottom center
            i = +1
            j = 0
        if direction == "BR": # bottom right
            i = j = +1
        if direction == "L": # left
            i = 0
            j = -1
        if direction == "R": # right
            i = 0
            j = +1

        if not (0 <= self.x + i < len(seats) and 0 <= self.y + j < len(seats[self.x])):
            return None

        if seats[self.x + i][self.y + j].value == ".":
            return seats[self.x + i][self.y + j].find_first_visible(seats, direction)
        
        return [self.x + i, self.y + j]

    def find_all_visibles(self, seats):
        l = []
        for direction in ["TL", "TC", "TR", "BL", "BC", "BR", "L", "R"]:
            x = self.find_first_visible(seats, direction)
            if x != None:
                l.append(x)
        return l


f = open(os.getcwd() + "/2020/11/input.txt", "r")
Lines = f.readlines()

# create list of seats
seats = []
for i, line in enumerate(Lines):
    row = []
    for j, s in enumerate(line):
        if s != "\n" and s != " ":
            x = Seat(s,i,j)
            row.append(x)
    seats.append(row)


def solve(seats, part):
    if part == 1:
        tolerance = 4
    else:
        tolerance = 5
    
    convergence = False
    while not convergence:
        new_seats = copy.deepcopy(seats)
        convergence = True  # nothing as changed so far

        for row_index in range(0, len(seats)):
            for col_index in range(0, len(seats[row_index])):
                s = new_seats[row_index][col_index]
                if part == 1:
                    adj_indexes = s.find_adjacents()
                else:
                    adj_indexes = s.find_all_visibles(seats)
                
                num = 0

                if s.value == 'L':     # the seat is empty, check if we can change it
                    for i, j in adj_indexes:
                        num += seats[i][j].value == '#'
                    if num == 0:
                        s.value = '#'     # seat becomes occupied
                        convergence = False

                if s.value == '#':    # the seat is occupied, check if we can change it
                    for i, j in adj_indexes:
                        num += seats[i][j].value == '#'
                    if num >= tolerance:
                        s.value = 'L'     # seat becomes occupied
                        convergence = False

        seats = new_seats

    num_of_occupied_seats = 0
    for row in seats:
        for col in row:
            num_of_occupied_seats += col.value == '#'
    return num_of_occupied_seats


print("part 1: " + str(solve(seats, 1)))
print("part 2: " + str(solve(seats, 2)))
