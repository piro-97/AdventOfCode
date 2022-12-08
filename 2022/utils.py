import numpy as np

YEAR = 2022

def read_input(day :int, keep_eol=False) -> "list[str]":
    input_path = f"{YEAR}/input/{str(day).zfill(2)}.txt"
    print(f"reading input from -> {input_path}")

    with open(input_path, "r") as f:
        return list( map(lambda x : x.replace("\n", "") if not keep_eol else x, f.readlines()))


def print_answer(part :int, value) -> None:
    print(f"PART {part} -> {value}")


def to_np_array(list_of_strings :"list[str]", dtype=int) -> np.ndarray:
    shape = ( len(list_of_strings), len(list_of_strings[0]) )
    arr = np.zeros(shape, dtype=dtype)

    for i,l in enumerate(list_of_strings):
        for j,c in enumerate(l):
            arr[i,j] = c

    return arr
