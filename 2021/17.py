import utils
from itertools import product
import re

DAY = 17

MAX_X = 100
MAX_Y = 300
MIN_Y = -300


def next_position(position :tuple, velocity :tuple) -> tuple:
    return (position[0] + velocity[0], position[1] + velocity[1])


def update_velocity(velocity :tuple) -> tuple:
    v_x, v_y = 0, 0
    if velocity[0] > 0:
        v_x = velocity[0] - 1
    if velocity[0] < 0:
        v_x = velocity[0] + 1
    v_y = velocity[1] - 1
    return (v_x, v_y)


def is_in_target(position :tuple, target :tuple) -> bool:
    x1, x2 = target["x"]
    y1, y2 = target["y"]
    return (x1 <= position[0] <= x2) and (y1 <= position[1] <= y2)


def may_reach_target(position :tuple, target :tuple, velocity :tuple) -> bool:
    x, y = position
    x1, x2 = target["x"]
    y1, y2 = target["y"]
    v_x, v_y = velocity
    impossible = (x > x2 and v_x >= 0) or (x < x1 and v_x <= 0) or (y < y1 and v_y <= 0)
    return not impossible


line = utils.read_input(DAY)[0].replace(" ", "")
nums = re.findall("[-]?\d+", line)
target_area = { "x" : (int(nums[0]), int(nums[1])), "y" : (int(nums[2]), int(nums[3])) }

v_x = range(1, MAX_X)
v_y = range(MIN_Y, MAX_Y)
velocities = product(v_x,v_y)

max_y = 0
feasible_solutions = 0
for i, v in enumerate(velocities):
    position = (0,0)
    highest_y = 0
    reached_target = False
    while not reached_target and may_reach_target(position, target_area, v):
        position = next_position(position, v)
        v = update_velocity(v)
        highest_y = max(highest_y, position[1])
        if is_in_target(position, target_area):
            max_y = max(max_y, highest_y)
            feasible_solutions += 1
            reached_target = True

# part 1
utils.print_answer(1, max_y)
# part 2
utils.print_answer(2, feasible_solutions)