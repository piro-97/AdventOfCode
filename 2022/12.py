import heapq

import numpy as np
import utils

DAY = 12

COST = 1


def apply_lambda_to_np_array(arr :np.ndarray, f :callable) -> np.ndarray:
    """apply function f to each element x of arr, returning a np array of f(x)

    Args:
        arr (np.ndarray): np array of x elements to apply f to
        f (callable): function f(.) which returns a transformation f(x) of x (type must be compatible with arr.dtype)

    Returns:
        np.ndarray: array of elements f(x) 
    """
    return np.array(list(map(f, arr.flat))).reshape(arr.shape)


def find_coord(grid :np.ndarray, value :np.ndarray.dtype) -> set[tuple[int,int]]:
    x, y = np.where(grid == value)
    return {(xx, yy) for xx, yy in zip(x,y)}


def neighbours4(idx :tuple[int,int], grid :np.ndarray) -> set[tuple[int,int]]:
    x0, y0 = idx
    size_x, size_y = grid.shape
    all_n = {(x0, y0 + 1), (x0, y0 - 1), (x0 + 1, y0), (x0 - 1, y0)}
    return {(z,w) for z,w in all_n if 0 <= z < size_x and 0 <= w < size_y}


def neighbours_climb(idx :tuple[int,int], grid :np.ndarray):
    for n in neighbours4(idx, grid):
        if grid[idx] >= grid[n] - 1:
            yield (n, COST)


def neighbours_descend(idx :tuple[int,int], grid :np.ndarray):
    for n in neighbours4(idx, grid):
        if grid[idx] <= grid[n] + 1:
            yield (n, COST)


def grid_to_graph(grid :np.ndarray, neighbours_function :callable) -> dict:    # TODO try to generalize this function removing the height condition
    graph = {}
    size_x, size_y = grid.shape

    for x in range(size_x):
        for y in range(size_y):
            graph[(x, y)] = [n for n in neighbours_function((x,y), grid)]

    return graph


def dijkstra(graph, start :tuple[int,int], end :set[tuple[int,int]]) -> int:
    heap = [(0, start)]  # cost from start node,end node
    visited = set()
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u in end:
            return cost
        for v, c in graph[u]:
            if v in visited:
                continue
            next_item = cost + c
            heapq.heappush(heap, (next_item, v))
    return -1


lines = utils.read_input(DAY)
grid_alpha = utils.to_np_array(lines, dtype=str)
f = lambda x : ord("a") if x == "S" else ord("z") if x == "E" else ord(x)
grid_decimal = apply_lambda_to_np_array(grid_alpha, f)

start = find_coord(grid_alpha, "S").pop()
end1 = find_coord(grid_alpha, "E")
end2 = find_coord(grid_decimal, ord("a"))

graph1 = grid_to_graph(grid_decimal, neighbours_climb)
graph2 = grid_to_graph(grid_decimal, neighbours_descend)

utils.print_answer(1, dijkstra(graph1, start, end1))
utils.print_answer(2, dijkstra(graph2, end1.pop(), end2))
