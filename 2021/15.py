import numpy as np
from itertools import product
from tqdm import tqdm
import utils

DAY = 15


def tiled_matrix(original :np.ndarray, growth_factor=5) -> np.ndarray:
    s0, s1 = original.shape[0], original.shape[1]
    new_shape = (s0 * growth_factor, s1 * growth_factor)
    matrix_2 = np.zeros(new_shape, dtype=int)
    
    for i in range(growth_factor):
        for j in range(growth_factor):
            new_tile = (matrix + i + j) % 9
            new_tile[new_tile == 0] = 9
            matrix_2[i*s0 : (i+1)*s0, j*s1 : (j+1)*s1] = new_tile
    return matrix_2


def neighbours(index :"tuple[int,int]", shape :tuple) -> "set[tuple[int,int]]":
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


def insert_ordered(point :tuple, queue :list, ordering :dict) -> list:
    if not queue:
        return [point]

    for i,p in enumerate(queue):
        if ordering[point] <= ordering[p]:
            queue.insert(i, point)
            return queue

    return queue + [point]


def dijkstra(matrix :np.ndarray, start :tuple, end :tuple) -> int:
    Q = set()
    distances = {}
    priority_queue = []

    for p in list(product(range(matrix.shape[0]), range(matrix.shape[1]))):
        Q.add(p)
        distances[p] = np.inf

    distances[start] = 0
    priority_queue.append(start)

    with tqdm(Q) as pbar:
        while len(Q) > 0:
            u = priority_queue.pop(0)
            Q.remove(u)

            ne = neighbours(u, matrix.shape)
            for n in ne:
                if n in Q:
                    new_dist = distances[u] + matrix[n]
                    if new_dist < distances[n]:
                        distances[n] = new_dist
                        priority_queue = insert_ordered(n, priority_queue, distances)
            pbar.update()

    return distances[end]


lines = utils.read_input(DAY)
SHAPE = (len(lines), len(lines[0]))
matrix = np.zeros(SHAPE, dtype=int)
for i in range(SHAPE[0]):
    for j in range(SHAPE[1]):
        matrix[i,j] = lines[i][j]
        
# part 1
start = (0,0)
end = (matrix.shape[0]-1, matrix.shape[1]-1)
utils.print_answer(1, dijkstra(matrix, start, end))

# part 2
matrix_2 = tiled_matrix(matrix)
end = (matrix_2.shape[0]-1, matrix_2.shape[1]-1)
utils.print_answer(2, dijkstra(matrix_2, start, end))
