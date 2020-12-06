import os


f = open(os.getcwd() + "/6/input.txt", "r")
Lines = f.readlines()

groups = []
id = 0
answers = []
for line in Lines:
    if line != "\n":
        answers.append(line.replace("\n", ""))
    
    else:
        group = dict()
        group['id'] = id
        group['answers'] = answers
        groups.append(group)

        id += 1
        answers = []



# part 1

sum = 0
for g in groups:
    st = ""
    for s in g['answers']:
        st += s

    sum += len(set(st))

print("part 1: " + str(sum))


# part 2

sum = 0
for g in groups:
    st = None
    for s in g['answers']:
        if st is None:
            st = set(s)
        else:
            st = set.intersection(st, (set(s)))

    sum += len(st)

print("part 2: " + str(sum))
