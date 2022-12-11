import utils
import re
import numpy as np

DAY = 10


def pretty_draw(arr :np.ndarray) -> None:
    c = "\n".join("".join("#" if cell else " " for cell in row) for row in arr)
    print(c)


lines = utils.read_input(DAY)
add_pattern = re.compile(r"addx (?P<value>.*)")

x = 1
v = 0
clock = 0
MAX_CLOCK = 240
signal_strenghts = np.zeros(MAX_CLOCK, dtype=int)
drawing = np.zeros_like(signal_strenghts)

for line in lines:
    signal_strenghts[clock] = x * (clock + 1)
    drawing[clock] = (x-1 <= (clock) % 40 <= x+1)
    clock += 1

    m = re.match(add_pattern, line)
    if m:
        signal_strenghts[clock] = x * (clock + 1)
        drawing[clock] = (x-1 <= (clock) % 40 <= x+1)
        clock += 1
        x += int(m.group("value"))

utils.print_answer(1, sum([signal_strenghts[i] for i in [19, 59, 99, 139, 179, 219]]))

pretty_draw(drawing.reshape(6,40))
