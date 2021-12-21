import utils

DAY = 21

DICES = [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]   # value, frequency pairs when rolling 3 dices

class Configuration:
    def __init__(self, position_1 :int, position_2 :int):
        self.position_1, self.position_2 = position_1, position_2
        self.score_1, self.score_2 = 0, 0
        self.history_1, self.history_2 = [], []
        self.turn = True

    def winner(self, win_threshold :int) -> int:    # returns the id of the winner, 0 if match is not over
        if self.score_1 >= win_threshold:
            return 1
        if self.score_2 >= win_threshold:
            return 2

        return 0

    def step(self, dice_val :int):
        if self.turn:
            self.position_1 = (self.position_1 + dice_val) % 10
            self.score_1 += self.position_1 if self.position_1 != 0 else 10
            self.history_1.append(dice_val)
        else:
            self.position_2 = (self.position_2 + dice_val) % 10
            self.score_2 += self.position_2 if self.position_2 != 0 else 10
            self.history_2.append(dice_val)
    
        self.turn = not self.turn
    
    def __copy__(self):
        c = Configuration(self.position_1, self.position_2)
        c.history_1, c.history_2 = self.history_1.copy(), self.history_2.copy()
        c.score_1, c.score_2 = self.score_1, self.score_2
        c.turn = self.turn
        return c


def deterministic_game(config :Configuration) -> int:
    dice = 1
    while config.winner(1000) == 0:
        config.step(3 * (dice + 1))
        dice += 3
    loser_score = config.score_2 if config.winner(1000) == 1 else config.score_1
    return (dice - 1) * loser_score


def dirac_game(config :Configuration) -> tuple:
    w = config.winner(21)
    if w:
        return (1,0) if w == 1 else (0,1)

    w_1, w_2 = 0,0
    for d,o in DICES:
        c = config.__copy__()
        c.step(d)
        w = dirac_game(c)
        w_1 += o * w[0]
        w_2 += o * w[1]
    
    return (w_1, w_2)


pos_1, pos_2 = map(lambda s : int(s.split(": ")[1]), utils.read_input(DAY))
config = Configuration(pos_1, pos_2)

# part 1
utils.print_answer(1, deterministic_game(config.__copy__()))

# part 2
utils.print_answer(2, max(dirac_game(config)))