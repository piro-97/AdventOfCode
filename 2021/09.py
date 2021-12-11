import numpy as np
import utils

DAY = 9

def neighbours(index :"tuple[int,int]", shape) -> "set[tuple[int,int]]":
    x,y = index
    ne = set()
    if x > 0:
        ne.add( (x-1, y) )
    if x < shape[0] - 1:
        ne.add( (x+1, y) )
    if y > 0:
        ne.add( (x, y-1) )
    if y < shape[1] - 1:
        ne.add( (x, y+1) )
    return ne

def is_lowpoint(matrix :np.ndarray, index :"tuple[int,int]") -> bool:
    ne = neighbours(index, matrix.shape)
    for n in ne:
        if matrix[n] <= matrix[index]:
            return False
        
    return True

def basin_size(matrix :np.ndarray, mask :np.ndarray, index :"tuple[int,int]") -> int:
    if mask[index]: # already visited
        return 0

    mask[index] = True

    if matrix[index] == 9:  # limit of basin
        return 0

    return 1 + np.sum([basin_size(matrix, mask, n) for n in neighbours(index, matrix.shape)])


lines = utils.read_input(DAY)

SHAPE = (len(lines), len(lines[0]))
heightmap = np.zeros(SHAPE, dtype=int)

for i, line in enumerate(lines):
    for j, value in enumerate(line):
        heightmap[i,j] = int(value)

# part 1
risk = 0
for i in range(SHAPE[0]):
    for j in range(SHAPE[1]):
        if is_lowpoint(heightmap, (i,j)):
            risk += heightmap[i,j] + 1

utils.print_answer(1, risk)

# part 2
basins = []
mask = np.zeros_like(heightmap, dtype=bool)
for i in range(SHAPE[0]):
    for j in range(SHAPE[1]):
        basins.append(basin_size(heightmap, mask, (i,j)))

basins.sort()
utils.print_answer(2, basins[-1] * basins[-2] * basins[-3])