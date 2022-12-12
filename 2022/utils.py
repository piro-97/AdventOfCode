import heapq
import numpy as np

YEAR = 2022

def read_input(day :int, keep_eol=False) -> "list[str]":
    input_path = f"{YEAR}/input/{str(day).zfill(2)}.txt"
    print(f"reading input from -> {input_path}")

    with open(input_path, "r") as f:
        return list( map(lambda x : x.replace("\n", "") if not keep_eol else x, f.readlines()) )


def print_answer(part :int, value) -> None:
    print(f"PART {part} -> {value}")


def to_np_array(list_of_strings :"list[str]", dtype=int) -> np.ndarray:
    shape = ( len(list_of_strings), len(list_of_strings[0]) )
    arr = np.zeros(shape, dtype=dtype)

    for i,l in enumerate(list_of_strings):
        for j,c in enumerate(l):
            arr[i,j] = c

    return arr


## GRAPHS

def grid_to_graph(grid :np.ndarray, neighbours_function :callable) -> dict:
    """create a graph in form of a dictionary starting from a 2 dimensional np array

    Args:
        grid (np.ndarray): 2 dim np array representing the grid of the problem 
        neighbours_function (callable): function which defines the neighbour (w,t) of each coordinate (x,y) of the grid.
        Such a function f takes as input a tuple of coordinates and the grid [f((x,y), grid)] and must return a tuple (neighbour, cost)

    Returns:
        dict: graph representation of the grid: key = vertices, values = edges
    """
    graph = {}
    size_x, size_y = grid.shape

    for x in range(size_x):
        for y in range(size_y):
            graph[(x, y)] = [n for n in neighbours_function((x,y), grid)]

    return graph


def dijkstra(graph, start, end) -> int:
    """dijkstra algorithm for shortest path problem

    Args:
        graph (dict): dictionary whose keys are the Vertices of the graph and values are the Edges
        start : starting vertex
        end : set of end vertices

    Returns:
        int: shortest path length
    """
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
