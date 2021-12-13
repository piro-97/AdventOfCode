import numpy as np
import utils

DAY = 13

def print_m(matrix :np.ndarray) -> None:
    for y in range(matrix.shape[1]):
        for x in range(matrix.shape[0]):
            if matrix[x,y]:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def init(lines :"list[str]") -> np.ndarray:
    X = list( map( lambda s: int(s.split(",")[0]), lines ) )
    Y = list( map( lambda s: int(s.split(",")[1]), lines ) )
    xx = max(X) + 1
    yy = max(Y) + 1
    xx += 1 - (xx % 2)  # paper can be folded in half only if the dimension is odd
    yy += 1 - (yy % 2)  # paper can be folded in half only if the dimension is odd
    matrix = np.zeros((xx, yy), dtype=bool)
    for p in zip(X, Y):
        matrix[p] = True
    return matrix


def fold(matrix :np.ndarray, axis :str, value :int) -> np.ndarray:
    if axis == "x":
        new_matrix_shape = (matrix.shape[0] - value - 1, matrix.shape[1])
    if axis == "y":
        new_matrix_shape = (matrix.shape[0], matrix.shape[1] - value - 1)
    new_matrix = np.zeros(new_matrix_shape, dtype=bool)
    
    for x in range(new_matrix_shape[0]):
        for y in range(new_matrix_shape[1]):
            if axis == "x":
                new_matrix[x,y] = matrix[x,y] or matrix[2*value-x, y]
            if axis == "y":
                new_matrix[x,y] = matrix[x,y] or matrix[x, 2*value-y]
    return new_matrix


# part 1
lines = utils.read_input(DAY)
break_l = lines.index("")
m = init(lines[:break_l])

axis, value = lines[break_l+1].split("=")[0][-1], int(lines[break_l+1].split("=")[1])
m = fold(m, axis, value)
utils.print_answer(1, np.sum(m))

# part 2
m = init(lines[:break_l])
for l in lines[break_l+1:]:
    axis, value = l.split("=")[0][-1], int(l.split("=")[1])
    m = fold(m, axis, value)
print("PART 2 -> ")
print_m(m)
