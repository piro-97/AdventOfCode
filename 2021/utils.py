import numpy as np

YEAR = 2021

def read_input(day :int) -> "list[str]":
    if len(str(day)) == 1:
        day = f"0{day}"
    with open(f"{YEAR}/input/{day}.txt", "r") as f:
        return list( map(lambda x : x.replace("\n", ""), f.readlines()))


def print_answer(part :int, value) -> None:
    print(f"PART {part} -> {value}")
    

def to_np_array(list_of_strings :"list[str]") -> np.ndarray:
    shape = ( len(list_of_strings), len(list_of_strings[0]) )
    arr = np.zeros(shape, dtype=int)
    for i,l in enumerate(list_of_strings):
        for j,c in enumerate(l):
            arr[i,j] = c
    return arr