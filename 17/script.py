import os
import numpy as np
from copy import deepcopy


def find_my_neighbours(point):
    l = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            for k in [-1,0,1]:
                if len(point) == 4:
                    for w in [-1,0,1]:
                        if i != 0 or j != 0 or k != 0 or w != 0:
                            l.append({
                                'x' : point[0] + i,
                                'y' : point[1] + j,
                                'z' : point[2] + k,
                                'w' : point[3] + w
                                })
                else:
                    if i != 0 or j != 0 or k != 0:
                        l.append({
                            'x' : point[0] + i,
                            'y' : point[1] + j,
                            'z' : point[2] + k,
                            'w' : origin[3]
                            })
    return l


f = open(os.getcwd() + "/17/input.txt", "r")
Lines = f.readlines()

#x_max = 23
#y_max = 23
#z_max = 13
#w_max = 13
x_max = 25
y_max = 25
z_max = 17
w_max = 17



origin = [int(x_max / 2), int(y_max / 2), int(z_max / 2), int(w_max / 2)]
Points_original = np.zeros((x_max, y_max, z_max, w_max))

CYCLES = 6

for x, line in enumerate(Lines):
    line = line.replace("\n", "").replace(" ", "")
    for y, char in enumerate(line):
        if char == "#":
            x_p = origin[0] + x
            y_p = origin[1] + y
            z_p = origin[2]
            w_p = origin[3]
            Points_original[x_p][y_p][z_p][w_p] = True


def solve(Points, dimension):
    i = 0
    new_state = deepcopy(Points)
    while i < CYCLES:
        for x in range(x_max):
            for y in range(y_max):
                for z in range(z_max):
                    if dimension == 3:
                        neig = [x,y,z]

                        count_ne = 0
                        ne = find_my_neighbours(neig)
                        for n in ne:
                            xx = n['x']
                            yy = n['y']
                            zz = n['z']
                            ww = n['w']

                            if 0 <= xx < x_max and 0 <= yy < y_max and 0 <= zz < z_max and 0 <= ww < w_max and \
                            Points[xx][yy][zz][ww] == True:
                                count_ne += 1
                        
                        if Points[x][y][z][ww] == True:
                            if count_ne != 2 and count_ne != 3:
                                new_state[x][y][z][ww] = False
                        else:
                            if count_ne == 3:
                                new_state[x][y][z][ww] = True

                    else:   # 4 dimensions
                        for w in range(w_max):
                            neig = [x,y,z,w]

                            count_ne = 0
                            ne = find_my_neighbours(neig)
                            for n in ne:
                                xx = n['x']
                                yy = n['y']
                                zz = n['z']
                                ww = n['w']

                                if 0 <= xx < x_max and 0 <= yy < y_max and 0 <= zz < z_max and 0 <= ww < w_max and \
                                Points[xx][yy][zz][ww] == True:
                                    count_ne += 1
                            
                            if Points[x][y][z][w] == True:
                                if count_ne != 2 and count_ne != 3:
                                    new_state[x][y][z][w] = False
                            else:
                                if count_ne == 3:
                                    new_state[x][y][z][w] = True
            
        Points = deepcopy(new_state)
        i += 1

    return sum(sum(sum(sum(Points))))

#print("part 1:", solve(Points_original, 3))
print("part 2:", solve(Points_original, 4))