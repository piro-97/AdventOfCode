from math import ceil, floor
import utils
import re
from itertools import product

DAY = 18


def match_num(string :str, offset :int) -> dict:
    match = re.finditer("\d+", string[offset:])
    match = next(match, None)
    if match:
        return {
            "value" : match.group(),
            "start" : abs(offset + match.start()),
            "end" : abs(offset + match.end()),
        }
    else:
        return {
            "value" : '0',
            "start" : 0,
            "end" : 0,
        }


def explode(snail :str, index_l :int, index_r :int) -> str:
    pattern = re.compile("\d+")
    l_addendum, r_addendum = map(int, pattern.findall(snail[index_l:index_r]))
    
    right = match_num(snail, index_r)
    left = match_num(snail[::-1], -index_l)
    left["value"] = int(left["value"][::-1])
    temp = left["start"]
    left["start"] = left["end"]
    left["end"] = temp

    new_l = str(l_addendum + int(left["value"])) if left["end"] - left["start"] > 0 else ""

    if right["end"] - right["start"] > 0:
        new_r = str(r_addendum + int(right["value"]))
    else:
        new_r = ""
        right["start"] = right["end"] = index_r + 1

    s = snail[:left["start"]] + new_l + snail[left["end"] : index_l] + '0' + snail[index_r+1 : right["start"]] + new_r + snail[right["end"]:]
    return s


def split(snail :str, index_l :int, index_r :int) -> str:
    num = int(re.findall("\d+", snail[index_l : index_r])[0])
    return snail[:index_l] + f"[{floor(num / 2)},{ceil(num / 2)}]" + snail[index_r:]


def find_matching_par(snail :str, idx :int) -> tuple:
    level = 0
    i = idx
    while i < len(snail):
        level += (snail[i] == "[")
        level -= (snail[i] == "]")
        if level == 0:
            return (idx, i)
        i += 1


def scan(snail :str) -> str:
    # explode check
    level = 0
    for i,c in enumerate(snail):
        if level >= 4 and c == "[":
            l,r = find_matching_par(snail, i)
            return scan(explode(snail, l, r))
        level += (c == "[")
        level -= (c == "]")
    
    # split check
    for i,c in enumerate(snail):
        num = re.match("\d+", snail[i:])
        if num and int(num[0]) > 9:
            return scan(split(snail, i, i+len(num[0])))

    return snail


def sum(s1 :str, s2 :str) -> str:
    return f"[{s1},{s2}]"


def magnitude(snail :str) -> int:
    if len(snail) == 1:
        return int(snail[0])

    idx_l, idx_r = find_matching_par(snail, 1)
    return 3 * magnitude(snail[idx_l:idx_r+1]) + 2 * magnitude(snail[idx_r+2:-1])


snails = utils.read_input(DAY)

# part 1
s = snails[0]
for i in range(1,len(snails)):
    s = scan(sum(s, snails[i]))
utils.print_answer(1, magnitude(s))

# part 2
couples = product(snails, snails)
max_magn = 0
for c in couples:
    max_magn = max( max_magn, magnitude(scan(sum(c[0], c[1]))) )

utils.print_answer(2, max_magn)