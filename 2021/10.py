import utils

DAY = 10


VALID = { ("(", ")"), ("[", "]"), ("{", "}"), ("<", ">") }

def corruption_score(line :str) -> int:
    score = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    }
    buffer = []
    for c in line:
        if c in "([{<":
            buffer.append(c)
        if c in ")]}>":
            last = buffer.pop()
            if (last, c) not in VALID:
                return score[c]
    return 0

def complete_line(line :str) -> int:
    completion_score = 0
    buffer = []
    for c in line:
        if c in ["(", "[", "{", "<"]:
            buffer.append(c)
        if c in [")", "]", "}", ">"]:
            last = buffer.pop()
            if (last, c) not in VALID:
                print("corrupted line")
    buffer.reverse()
    for c in buffer:
        completion_score *= 5
        completion_score += ["(", "[", "{", "<"].index(c) + 1
    
    return completion_score

lines = utils.read_input(10)

# part 1
total = 0
for line in lines:
    total += corruption_score(line)

utils.print_answer(1, total)

# part 2
autocompletion_scores = []
for line in lines:
    if 0 == corruption_score(line):
        autocompletion_scores.append(complete_line(line))
autocompletion_scores.sort()

utils.print_answer(2, autocompletion_scores[len(autocompletion_scores) // 2])