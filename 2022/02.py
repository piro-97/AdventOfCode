import utils

DAY = 2

OUTCOMES = {
    ("rock", "rock") : 3,
    ("rock", "paper") : 0,
    ("rock", "scissor") : 6,
    ("paper", "rock") : 6,
    ("paper", "paper") : 3,
    ("paper", "scissor") : 0,
    ("scissor", "rock") : 0,
    ("scissor", "paper") : 6,
    ("scissor", "scissor") : 3,
}

POINTS = {
    "rock" : 1,
    "paper" : 2,
    "scissor" : 3,
}

def replace_values(in_vals :str) -> str:
    return in_vals.replace("A", "rock").replace("B", "paper").replace("C", "scissor")


def game1(game_string :str) -> str:
    return replace_values(game_string.replace("X", "A").replace("Y", "B").replace("Z", "C"))


def game2(game_string :str) -> str:
    opponent, result = replace_values(game_string).split()

    switch = {
        "X" : [key[0] for key, value in OUTCOMES.items() if value == 0 and key[1] == opponent] [0],  # lose
        "Y" : opponent,  # draw
        "Z" : [key[0] for key, value in OUTCOMES.items() if value == 6 and key[1] == opponent] [0]   # win
    }

    return opponent + " " + replace_values(switch[result])



def calculate_match_result(player_choice :str, opponent_choice :str) -> int:
    return OUTCOMES[(player_choice, opponent_choice)] + POINTS[player_choice]


games = utils.read_input(DAY)
results1 = []
results2 = []
for game in games:
    opponent1, player1 = game1(game).split(" ")
    opponent2, player2 = game2(game).split(" ")
    results1.append(calculate_match_result(player1, opponent1))
    results2.append(calculate_match_result(player2, opponent2))

utils.print_answer(1, sum(results1))
utils.print_answer(2, sum(results2))


