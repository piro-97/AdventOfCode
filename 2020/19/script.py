import os
import re


def create_rule(line):
    rule = {
        "end_rule": False,
        "content": []
    }

    S = line.replace("\n", "").split(": ")
    rule_number = int(S[0])

    if re.match(r"\d+", S[1]):                  # rule links to other rules
        Options = S[1].split(" | ")

        for option in Options:                  # OR part
            nums = re.findall(r"\d+", option)
            rr = []

            for num in nums:                    # AND part
                rr.append(int(num))
            rule["content"].append(rr)

    else:                                       # rule maps a letter
        rule["end_rule"] = True
        s = S[1].replace('"', '')
        rule["content"].append(s)

    rules[rule_number] = rule


def match_string(text, text_idx, rule_num):
    curr_rule = rules[rule_num]

    if text_idx >= len(text):
        return False

    if curr_rule["end_rule"]:
        return curr_rule["content"][0] == text[text_idx]

    ors = curr_rule["content"]
    for orx in ors:
        resx = False
        for andx in orx:
            curr_res = match_string(text, text_idx + resx, andx)
            if not curr_res:
                resx = False
                break
            resx += curr_res

        if resx:
            return resx

    return False


f = open(os.getcwd() + '/2020/19/input.txt', 'r')
Lines = f.readlines()

rules = {}
matching = 0

creating_rules = True
for line in Lines:
    if line == "\n":
        creating_rules = False
        continue

    if creating_rules:
        create_rule(line)
    else:
        txt = line.replace("\n", "")
        z = match_string(txt, 0, 0)
        zzz = (len(txt) == z)
        matching += zzz

print("part 1:", matching)