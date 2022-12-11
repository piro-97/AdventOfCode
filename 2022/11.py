import math
import re
from copy import deepcopy

import utils

DAY = 11

class Monkey:

    def __init__(self, lines :list[str]):
        self.id = int(next(re.finditer(r"\d+", lines[0])).group())
        self.items = list(map(lambda m : int(m.group()), re.finditer(r"\d+", lines[1])))
        self.operation = re.search(r"new = (?P<operation>.*)", lines[2]).group("operation")
        self.test = int(re.search(r"divisible by (?P<divisor>\d+)", lines[3]).group("divisor"))
        self.on_true = int(re.search(r"throw to monkey (?P<id>\d+)", lines[4]).group("id"))
        self.on_false = int(re.search(r"throw to monkey (?P<id>\d+)", lines[5]).group("id"))
        self.activity = 0

    def throw_item(self, magic_number :int) -> tuple[int,int]:
        """returns (monkey_destination_id, item_worry_level)"""
        self.activity += 1
        old = self.items.pop(0)
        new = eval(self.operation)    # use "old" and the operation to calculate the "new" worry level

        if not magic_number:
            new = new // 3
        else:
            new = new % magic_number

        destination = self.on_true if new % self.test == 0 else self.on_false
        return (destination, int(new))

    def catch_item(self, item :int) -> None:
        self.items.append(item)

    def __str__(self) -> str:
        return str(self.items)


def monkey_business(rounds :int, monkeys :list[Monkey], magic_number=None) -> int:
    for _ in range(rounds):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                dest, item = monkey.throw_item(magic_number)
                monkeys[dest].catch_item(item)
    
    return math.prod(sorted([m.activity for m in monkeys])[-2:])


lines = utils.read_input(DAY)
monkeys = [Monkey(lines[7*i : 7*(i+1)]) for i in range(len(lines)//7)]
magic_number = math.prod([m.test for m in monkeys]) # product of all divisors (primes)

utils.print_answer(1, monkey_business(20, deepcopy(monkeys)))
utils.print_answer(2, monkey_business(10000, monkeys, magic_number))
