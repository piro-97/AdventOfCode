import utils
import re
import sys

DAY = 7

class Node:

    def __init__(self, name :str, type :str, parent :"Node", size=0) -> "Node":
        self.name = name
        self.type = type
        self.parent = parent
        self.children = set()
        self.size = size
    
    def add_children(self, child :"Node") -> None:
        self.children.add(child)

    def space(self) -> int:
        return self.size + sum(map(lambda x : x.space(), self.children))

    def cumul_size(self, threshold :int) -> int:
        space = self.space()
        if space > threshold or self.type != "dir":
            space = 0
        
        inner_sum = sum(map(lambda c : c.cumul_size(threshold), self.children))
        return space + inner_sum

    def smallest_deletable(self, threshold :int) -> int:
        space = self.space()
        
        if space < threshold or self.type != "dir":
            return sys.maxsize

        minimum = space
        for c in self.children:
            minimum = min(minimum, c.smallest_deletable(threshold))

        return minimum


def parse_single_file(line :str, cwd :Node) -> None:
    file_pattern = re.compile(r"(?P<size>\d*) (?P<name>.*)")
    dir_pattern = re.compile(r"dir (?P<name>.*)")

    file = re.match(file_pattern, line)
    dir = re.match(dir_pattern, line)

    if file:
        node = Node(file.group("name"), "file", parent=cwd, size=int(file.group("size")))
    else:
        node = Node(dir.group("name"), "dir", parent=cwd)

    cwd.add_children(node)


def parser(commands :list[str]) -> Node:
    cd_pattern = re.compile(r"\$ cd (?P<dir_name>.*)")

    root = Node("/", "dir", parent=None)
    
    cwd = root
    i = 1
    while i < len(commands):
        cd = re.match(cd_pattern, commands[i])
        
        if cd:
            if cd.group("dir_name") == "..":
                cwd = cwd.parent if cwd.parent != None else root

            for child in cwd.children:
                if child.name == cd.group("dir_name"):
                    cwd = child
                    break
        
        if commands[i][0] != "$":
            parse_single_file(commands[i], cwd)

        i += 1
    
    return root

lines = utils.read_input(DAY)
root = parser(lines)

utils.print_answer(1, root.cumul_size(100000))

disk_space = 70000000
used_space = root.space()
required_space = 30000000

utils.print_answer(2, root.smallest_deletable(-disk_space + used_space + required_space))






