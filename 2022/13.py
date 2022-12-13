import ast
import functools

import utils

DAY = 13

def pair_precedence(left, right) -> int:
    if type(left) == int and type(right) == list:
        return pair_precedence([left], right)
    
    if type(left) == list and type(right) == int:
        return pair_precedence(left, [right])
    
    if type(left) == type(right) == int:
        return -1 if left < right else 1 if left > right else 0

    i = 0
    compare = 0
    while i < len(left) and compare == 0:
        if i >= len(right):
            compare = 1
        else:
            compare = pair_precedence(left[i], right[i])
        i += 1

    return -1 if len(left) < len(right) and compare == 0 else compare


lines = utils.read_input(DAY)
packets = list(map(ast.literal_eval, lines[::3])) + list(map(ast.literal_eval, lines[1::3]))

# Part 1
size = len(packets)
pairs = zip(packets[:size//2], packets[size//2:])

ordered = []
for i,p in enumerate(pairs):
    if pair_precedence(p[0], p[1]) < 0:
        ordered.append(i+1)

utils.print_answer(1, sum(ordered))

# Part 2
marker1 = [[2]]
marker2 = [[6]]
packets.append(marker1)
packets.append(marker2)
packets.sort(key=functools.cmp_to_key(pair_precedence))

result = (packets.index(marker1)+1) * (packets.index(marker2)+1)
utils.print_answer(2, result)
