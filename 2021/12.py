import utils

DAY = 12

class Node:
    def __init__(self, name :str):
        self.name = name
        self.links = []
        self.small = not name.isupper()
    
    def __str__(self):
        return self.name

# part 1
def explore(end :Node, path :"list[Node]") -> int:
    current_node = path[-1]
    if current_node == end:
        return 1

    possible_routes = 0
    routes = current_node.links
    for route in routes:
        if not (route.small and route in path):   # this small cave has not yet been visited
            possible_routes += explore(end, path + [route])

    return possible_routes

# part 2
def explore2(end :Node, path :"list[Node]") -> int:
    current_node = path[-1]
    if current_node == end:
        return 1

    if current_node.name == "start" and len(path) > 1:  # cannot visit start twice
        return 0

    possible_routes = 0
    routes = current_node.links
    for route in routes:
        if route in path and route.small:
            small_caves_visited = list(filter(lambda x : x.small, path))
            if not any([small_caves_visited.count(x) > 1 for x in small_caves_visited]):    # a small cave has already been visited multiple times
                possible_routes += explore2(end, path + [route])
        else:
            possible_routes += explore2(end, path + [route])

    return possible_routes


lines = utils.read_input(DAY)

nodes = {}
for line in lines:
    s1, s2 = line.split("-")
    n1 = nodes[s1] if s1 in nodes.keys() else Node(s1)
    n2 = nodes[s2] if s2 in nodes.keys() else Node(s2)
    n1.links.append(n2)
    n2.links.append(n1)
    nodes[s1], nodes[s2] = n1, n2

utils.print_answer(1, explore(nodes["end"], [nodes["start"]]))
utils.print_answer(2, explore2(nodes["end"], [nodes["start"]]))
