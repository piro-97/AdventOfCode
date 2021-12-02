import utils

DAY = 2


def perform_command(line: str, position: "list[int]", is_aiming: bool) -> "list[int]":
    l = line.split(" ")
    direction = l[0]
    quantity = int(l[1])

    if direction == "forward":
        position["horizontal"] += quantity
        if is_aiming:
            position["depth"] += position["aim"] * quantity

    idx = "aim" if is_aiming else "depth"
    if direction == "up":
        position[idx] -= quantity
    if direction == "down":
        position[idx] += quantity


lines = utils.read_input(DAY)

# part 1
position = {
    "horizontal": 0,
    "depth": 0,
    "aim": 0,
}

for line in lines:
    perform_command(line, position, False)

utils.print_answer(1, position["horizontal"] * position["depth"])

# part 2
position = {
    "horizontal" : 0,
    "depth" : 0,
    "aim" : 0,
}
for line in lines:
    perform_command(line, position, True)

utils.print_answer(2, position["horizontal"] * position["depth"])
