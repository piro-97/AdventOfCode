import utils

DAY = 3


def calculate_score(string :str) -> int:
    values = []
    for s in string:
        if s.islower():
            values.append(ord(s) - ord("a") + 1)
        else:
            values.append(ord(s) - ord("A") + 27)
    
    return sum(values)


rucksacks = utils.read_input(DAY)

# part 1
scores = []
for rucksack in rucksacks:
    assert len(rucksack) % 2 == 0
    size = len(rucksack) // 2

    compartments = map (set, [rucksack[:size], rucksack[size:]])
    common_items = set.intersection(*compartments)
    scores.append(calculate_score(common_items))

utils.print_answer(1, sum(scores))


# part 2
assert len(rucksacks) % 3 == 0
scores = []
i = 0
while i < len(rucksacks):
    elves = map(set, rucksacks[i:i+3])
    common_items = set.intersection(*elves)
    scores.append(calculate_score(common_items))

    i += 3

utils.print_answer(2, sum(scores))
