import numpy as np
import utils

DAY = 5

MAX = 1000

def is_aligned(p1 :tuple, p2 :tuple) -> bool:
    return (p1[0] == p2[0]) or (p1[1] == p2[1])

def insert_point(matrix :np.ndarray, from_ :tuple, to_ :tuple, diagonal = False) -> None:
    from_x = min(from_[0], to_[0])
    to_x = max(from_[0], to_[0])
    from_y = min(from_[1], to_[1])
    to_y = max(from_[1], to_[1])

    if diagonal:
        for i in range(abs(from_[0] - to_[0]) + 1):
            if to_[0] > from_[0]:
                if to_[1] > from_[1]:
                    matrix[from_[0] + i, from_[1] + i] += 1
                else:
                    matrix[from_[0] + i, from_[1] - i] += 1
            else:
                if to_[1] > from_[1]:
                    matrix[from_[0] - i, from_[1] + i] += 1
                else:
                    matrix[from_[0] - i, from_[1] - i] += 1
        return matrix

    for x in range(from_x, to_x + 1):
        for y in range(from_y, to_y + 1):
            matrix[x,y] += 1
    return matrix

lines = utils.read_input(DAY)

# part 1
matrix = np.zeros((MAX, MAX), dtype=int)

for line in lines:
    l = line.split(" -> ")
    p1 = l[0].split(",")
    p2 = l[1].split(",")
    from_ = (int(p1[0]), int(p1[1]))
    to_ = (int(p2[0]), int(p2[1]))
    if is_aligned(from_, to_):
        matrix = insert_point(matrix, from_, to_)

utils.print_answer(1, np.sum(matrix > 1))


# part 2
matrix = np.zeros((MAX, MAX), dtype=int)

for line in lines:
    l = line.split(" -> ")
    p1 = l[0].split(",")
    p2 = l[1].split(",")
    from_ = (int(p1[0]), int(p1[1]))
    to_ = (int(p2[0]), int(p2[1]))
    if is_aligned(from_, to_):
        matrix = insert_point(matrix, from_, to_)
    else:
        matrix = insert_point(matrix, from_, to_, True)

utils.print_answer(2, np.sum(matrix > 1))


