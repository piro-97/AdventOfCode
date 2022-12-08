import utils

DAY = 6

line = utils.read_input(DAY)[0]

def find_first_marker(packet :str, marker_size :int) -> int:
    i = marker_size - 1
    while i < len(packet):
        if len(set(packet[i - marker_size + 1 : i + 1])) == marker_size:
            return i + 1
        i += 1

utils.print_answer(1, find_first_marker(line, 4))
utils.print_answer(2, find_first_marker(line, 14))
