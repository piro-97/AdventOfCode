import utils
from collections import defaultdict

DAY = 14

SOLVED = {}
RULES = {}

# def print_solved():
#     for k in SOLVED.keys():
#         print(f"{k} -> {dict(SOLVED[k])}")


def merge_dict(d1 :dict, d2 :dict) -> dict:
    d_1 = defaultdict(int, d1)
    d_2 = defaultdict(int, d2)
    for k in d_1.keys():
        d_2[k] += d_1[k]
    return dict(d_2)


def deep_explore(letter_pair :str, current_depth :int, target_depth :int) -> dict:
    if current_depth == target_depth:   # generation depth limit reached
        return {}

    if (letter_pair, target_depth - current_depth) in SOLVED.keys():    # I already generated the solution for this pair 
        return SOLVED[ (letter_pair, target_depth - current_depth) ]

    generated_letter = RULES[letter_pair]
    count = {generated_letter : 1}
    count_below_l = deep_explore(letter_pair[0] + generated_letter, current_depth + 1, target_depth)
    count_below_r = deep_explore(generated_letter + letter_pair[1], current_depth + 1, target_depth)
    sol = merge_dict(count_below_l, count_below_r)
    sol = merge_dict(sol, count)

    SOLVED[ (letter_pair, target_depth - current_depth) ] = sol.copy()
    return sol


def run(string :str, iterations :int) -> dict:
    d = {}
    for i in range(len(string) - 1):
        d = merge_dict(d, deep_explore(polymer[i:i+2], 0, iterations))
    for c in string:
        d[c] += 1
    return d


lines = utils.read_input(DAY)
polymer = lines[0]
for line in lines[2:]:
    l = line.replace(" ", "").split("->")
    RULES[l[0]] = l[1]

# part 1
d = run(polymer, 10)
utils.print_answer(1, max(d.values()) - min(d.values()))

# part 2
d = run(polymer, 40)
utils.print_answer(2, max(d.values()) - min(d.values()))
