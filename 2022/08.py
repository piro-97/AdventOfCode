import utils
import numpy as np
import math

DAY = 8

def check_visibility(forest :np.ndarray, coord :tuple) -> bool:
    i, j = coord
    temp = np.clip(forest - forest[i,j] + 1, 0, 9)

    top, bottom, left, right = temp[:i, j], temp[i+1:, j], temp[i, :j], temp[i, j+1:]

    return 0 == math.prod(map(np.sum, [left, right, top, bottom]))


def fmax (arr :np.ndarray) -> int:
    if np.sum(arr >= 0) == 0:
        return arr.size

    return np.argmax(arr >= 0) + 1


def scenic_score(forest :np.ndarray, coord :tuple) -> int:
    i, j = coord
    temp = forest - forest[i,j]

    top, bottom, left, right = np.flip(temp[:i, j]), temp[i+1:, j], np.flip(temp[i, :j]), temp[i, j+1:]

    return math.prod(map(fmax, [left, right, top, bottom]))


trees = utils.to_np_array(utils.read_input(DAY))
visibility = np.zeros_like(trees)
scenic_scores = np.zeros_like(trees)

for i in range(trees.shape[0]):
    for j in range(trees.shape[1]):
        is_visible = check_visibility(trees, (i,j))
        visibility[i][j] = visibility[i][j] or is_visible
        scenic_scores[i][j] = scenic_score(trees, (i,j))

utils.print_answer(1, np.sum(visibility))
utils.print_answer(2, np.max(scenic_scores))
