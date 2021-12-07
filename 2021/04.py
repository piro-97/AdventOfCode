import numpy as np
import utils

DAY = 4


def mark(boards :list, masks :list, extracted :int) -> None:
    for i in range(len(boards)):
        masks[i] = np.logical_or(masks[i], (boards[i] == extracted))

def check_win(boards :list, masks :list, win_value :int) -> list:
    winning_boards = []
    for i in range(len(boards)):
        col_sum = np.sum(masks[i], axis=0)
        row_sum = np.sum(masks[i], axis=1)
        if win_value in col_sum or win_value in row_sum:
            winning_boards += [i]
    return winning_boards if len(winning_boards) > 0 else [-1]


lines = utils.read_input(DAY)

extractions = np.array( list( map( lambda x : int(x), lines[0].replace("\n","").split(",") ) ) )

BOARD_SIZE = 5
boards = []
i = 1
while i < len(lines):
    if lines[i] != "\n":
        board_as_string = ""
        for j in range(BOARD_SIZE):
            board_as_string += " ".join(lines[i+j].split()) + " "
        board = np.fromstring(board_as_string, dtype=int, sep=" ").reshape(BOARD_SIZE,BOARD_SIZE)
        boards.append(board)
        i += BOARD_SIZE
    else:
        i += 1
        
masks = [np.zeros((BOARD_SIZE,BOARD_SIZE), dtype=bool)] * len(boards)

# part 1
j = 0
winner = -1
while winner < 0 and j < extractions.size:
    mark(boards, masks, extractions[j])
    winner = check_win(boards, masks, BOARD_SIZE)[0]
    j += 1

magic_value = np.sum( boards[winner] * (1 - masks[winner]) ) * extractions[j-1]
utils.print_answer(1, magic_value)

# part 2
masks = [np.zeros((BOARD_SIZE,BOARD_SIZE), dtype=bool)] * len(boards)
j = 0
while len(boards) > 1 and j < len(extractions):
    mark(boards, masks, extractions[j])
    winners = check_win(boards, masks, BOARD_SIZE)
    for winner in sorted(winners, reverse=True):
        if winner != -1:
            del boards[winner]
            del masks[winner]
    j += 1
# now only the last board is left, but we have to complete it
winner = -1
while winner < 0 and j < extractions.size:
    mark(boards, masks, extractions[j])
    winner = check_win(boards, masks, BOARD_SIZE)[0]
    j += 1

magic_value = np.sum( boards[0] * (1 - masks[0]) ) * extractions[j-1]
utils.print_answer(2, magic_value)
