import os
import math
import numpy as np

EAST = [1,0]
WEST = [-1,0]
NORTH = [0,1]
SOUTH = [0,-1]
FORWARD = 0

RIGHT = -1
LEFT = +1

class Position:
    def __init__(self, direction_facing):
        self.horizontal = 0
        self.vertical = 0
        self.facing = direction_facing

    def move_forward(self, value):
        h, v = self.facing
        self.horizontal += h * value
        self.vertical += v * value

    def move_in_direction(self, direction, value):
        h, v = direction
        self.horizontal += h * value
        self.vertical += v * value

    def rotate(self, rotation_dir, value):
        if rotation_dir == RIGHT:
            value = - value
        value = math.radians(value)
        # compute counterclockwise rotation matrix
        rotation_matrix = [ [ round(math.cos(value)), -round(math.sin(value)) ],
                            [ round(math.sin(value)),  round(math.cos(value)) ] ]
        vector = self.facing
        self.facing = np.dot(rotation_matrix, vector)

    def move_waypoint(self, direction, value):
        h, v = direction
        self.facing[0] += h * value
        self.facing[1] += v * value


def get_instr(opcode):
    if opcode == "R":
        return RIGHT
    if opcode == "L":
        return LEFT
    if opcode == "N":
        return NORTH
    if opcode == "S":
        return SOUTH
    if opcode == "E":
        return EAST
    if opcode == "W":
        return WEST
    if opcode == "F":
        return FORWARD
    return None


f = open(os.getcwd() + "/2020/12/input.txt", "r")
Lines = f.readlines()


# part 1

position = Position(EAST)
for instruction in Lines:
    op = get_instr(instruction[0])
    val = int(instruction[1:])

    if op in [EAST, WEST, NORTH, SOUTH]:            # move in direction
        position.move_in_direction(op, val)

    if op in [RIGHT, LEFT]:                         # rotate
        position.rotate(op, val)
    
    if op in [FORWARD]:                             # move forward
        position.move_forward(val)
    
manhattan = abs(position.horizontal) + abs(position.vertical)
print("part 1: " + str(manhattan))


# part 2

waypoint = [10, 1]
position = Position(waypoint)
for instruction in Lines:
    op = get_instr(instruction[0])
    val = int(instruction[1:])

    if op in [EAST, WEST, NORTH, SOUTH]:            # move waypoint in direction
        position.move_waypoint(op, val)

    if op in [RIGHT, LEFT]:                         # rotate
        position.rotate(op, val)
    
    if op in [FORWARD]:                             # move forward
        position.move_forward(val)

manhattan = abs(position.horizontal) + abs(position.vertical)
print("part 2: " + str(manhattan))
