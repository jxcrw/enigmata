#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/11"""

from copy import deepcopy
from math import lcm, prod
import re

from tools.aoc import extract_nums, load, prettyprint

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, _ = load('_example.txt', pre=0)
P, _ = load('_puzzle.txt', pre=0)

sep = '\n\n'
X = X.split(sep)
P = P.split(sep)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
class Monkey:
    """A monkey who's just monkeying around."""
    def __init__(self, s: str):
        s = s.split('\n')
        self.name = s[0]
        self.items = extract_nums(s[1])
        self.divisor = extract_nums(s[3])[0]
        self.target_true = extract_nums(s[4])[0]
        self.target_false = extract_nums(s[5])[0]
        self.operation = re.findall(r'Operation: new = (.*?) (.*?) (.*?)$', s[2])[0]
        self.inspections = 0

    def __repr__(self):
        return f'{self.name} {self.items}'

    def inspect(self, item: int) -> int:
        """Inspect an item and calculate its new worry level."""
        operand1 = item
        operator = self.operation[1]
        operand2 = self.operation[2]
        operand2 = int(operand2) if operand2.isnumeric() else item

        item = eval(f'{operand1} {operator} {operand2}') # Yeah yeah, eval is unsafe
        self.inspections += 1
        return item

    def aim(self, item: int) -> int:
        """Determine where to throw an item."""
        target = self.target_true if item % self.divisor == 0 else self.target_false
        return target


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1/2
# └─────────────────────────────────────────────────────────────────────────────
def calc_monkey_biz(monkeys: list[Monkey], rounds: int = 0, worry_damping: int = 0) -> int:
    """Compute level of monkey business after some rounds of keepaway."""
    LCM = lcm(*[m.divisor for m in monkeys])

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.items.reverse()
            while monkey.items:
                item = monkey.items.pop()
                item = monkey.inspect(item)

                if worry_damping:
                    item //= worry_damping
                else:
                    item %= LCM

                target = monkey.aim(item)
                monkeys[target].items.append(item)

    inspections = sorted([m.inspections for m in monkeys])
    monkey_biz = prod(inspections[-2:])
    return monkey_biz


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X = [Monkey(chunk) for chunk in X]
P = [Monkey(chunk) for chunk in P]

X1 = calc_monkey_biz(deepcopy(X), rounds=20, worry_damping=3)
P1 = calc_monkey_biz(deepcopy(P), rounds=20, worry_damping=3)
prettyprint(X1, P1)

X2 = calc_monkey_biz(deepcopy(X), rounds=10000, worry_damping=0)
P2 = calc_monkey_biz(deepcopy(P), rounds=10000, worry_damping=0)
prettyprint(X2, P2)
