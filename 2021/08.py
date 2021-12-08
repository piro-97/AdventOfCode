import numpy as np
import utils

DAY = 8


lines = utils.read_input(DAY)

entries = []
for line in lines:
    l = line.split("|")
    entries.append( {"input" : l[0].split(), "output" : l[1].split()} )


# part 1
magic_lenghts = (2,4,3,7)
count = 0
for entry in entries:
    out_nums = list( map(lambda x : len(x) , entry["output"]) )
    for x in out_nums:
        if x in magic_lenghts:
            count += 1
            
utils.print_answer(1, count)


# part 2

def decode(input :"list[str]") -> "dict":
    solved = {}
    codes_left = list()
    for code in input:
        if len(code) == 2:                    # 1
            solved[1] = set(code)
        elif len(code) == 4:                  # 4
            solved[4] = set(code)
        elif len(code) == 3:                  # 7
            solved[7] = set(code)
        elif len(code) == 7:                  # 8
            solved[8] = set(code)
        else:
            codes_left.append(set(code))

    for code in codes_left:
        if len(code) == 6:
            if solved[4].issubset(code):       # 9
                solved[9] = code
            elif solved[1].issubset(code):     # 6
                solved[0] = code
            else:                              # 0
                solved[6] = code
        if len(code) == 5:
            if solved[7].issubset(code):       # 3
                solved[3] = code 
            elif (solved[4] - solved[1]).issubset(code):    # 5
                solved[5] = code
            else:                                           # 2
                solved[2] = code
    return solved

def encode(codes :"list[str]", cipher :dict) -> int:
    total = 0
    for i, code in enumerate(codes):
        for key, value in cipher.items():
            if value == set(code):
                total += key * (10 ** (3 - i))
    return total

value = 0
for entry in entries:
    vocab = decode(entry["input"])
    value += encode(entry["output"], vocab)
    
utils.print_answer(2, value)