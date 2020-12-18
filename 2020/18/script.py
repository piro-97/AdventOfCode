import os
import re
import math

f = open(os.getcwd() + '/2020/18/input.txt', 'r')
Lines = f.readlines()

number_pattern = re.compile(r"\d+")
operator_pattern = re.compile(r"[\+\*]")


def compute_result(numbers, operations):
    if PRECEDENCE:
        i = 0
        while len(operations) > 0:
            if "+" in operations:
                if operations[i] == "+":
                    operations.pop(i)
                    num1 = numbers.pop(i)
                    num2 = numbers.pop(i)
                    numbers.insert(i, num1 + num2)
                    i -= 1
            else:
                return math.prod(numbers)
            i += 1
        result = numbers[0]
    else:
        result = numbers[0]
        for i, op in enumerate(operations):
            if op == "+":
                result += numbers[i+1]
            if op == "*":
                result *= numbers[i+1]

    return result 


def find_matching_par(expr):
    count = 0
    for i,c in enumerate(expr):
        if c == "(":
            count += 1
        if c == ")":
            count -= 1
        if count == 0:
            return i
    return None


def evaluate_expr(expr):
    if "(" not in expr and ")" not in expr:                 # expr can be computed!
        y = re.split(operator_pattern, expr)
        y = list(map(int, y))
        ops = re.findall(operator_pattern, expr)
    else:
        idx = 0
        y = []
        ops = []
        while idx < len(expr):
            if expr[idx] == "(":
                i = find_matching_par(expr[idx :])
                y.append(evaluate_expr(expr[idx + 1 : idx + i]))
                idx += i + 1
            else:
                if not re.match(operator_pattern, expr[idx:]):
                    x = re.match(number_pattern, expr[idx:])
                    y.append(int(x.group()))
                    idx += x.span()[1]
                else:
                    ops.append(expr[idx])
                    idx += 1

    return compute_result(y, ops)


def solve(lines):
    sum = 0
    for line in Lines:
        line = line.replace(" ", "").replace("\n", "")
        sum += evaluate_expr(line)
    
    return sum

PRECEDENCE = False
print("part 1:", solve(Lines))
PRECEDENCE = True
print("part 2:", solve(Lines))
