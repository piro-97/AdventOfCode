YEAR = 2021

def read_input(day :int) -> "list[str]":
    if len(str(day)) == 1:
        day = f"0{day}"
    with open(f"{YEAR}/input/{day}.txt", "r") as f:
        return list( map(lambda x : x.replace("\n", ""), f.readlines()))


def print_answer(part :int, value) -> None:
    print(f"PART {part} -> {value}")