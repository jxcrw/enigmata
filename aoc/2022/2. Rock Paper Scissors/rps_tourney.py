#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/2"""

from collections import deque

from tools.aoc import load, prettyprint, superparse
from tools.dsa.rps import Shape

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, _ = load('_example.txt', pre=0)
P, _ = load('_puzzle.txt', pre=0)

seps = deque([r'\n', r' '])
args = {'seps': seps, 'str_to_num': '', 'extract_num': False}
X = superparse(X, **args)
P = superparse(P, **args)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
Rock = Shape.R
Paper = Shape.P
Scissors = Shape.S


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1
# └─────────────────────────────────────────────────────────────────────────────
def play_by_shape(data):
    """Play by strategy guide, assuming second column is player 2 shape."""
    p2_score = 0
    for bout in data:
        p1_shape, p2_shape = decrypt1(*bout)

        weight = p2_shape.weight
        outcome = p2_shape.battle(p1_shape)

        bout_score = weight + outcome
        p2_score += bout_score

    return p2_score


def decrypt1(p1_shape, p2_shape):
    """Decrypt RPS game round, assuming second column is player 2 shape."""
    shapes = {
        'A': Rock, 'B': Paper, 'C': Scissors,
        'X': Rock, 'Y': Paper, 'Z': Scissors,
    }
    return shapes[p1_shape], shapes[p2_shape]


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 2
# └─────────────────────────────────────────────────────────────────────────────
def play_by_outcome(data):
    """Play by strategy guide, assuming second column is player 2 outcome."""
    p2_score = 0
    for bout in data:
        p1_shape, p1_outcome, p2_outcome = decrypt2(*bout)

        logic = p1_shape.logic
        reverse_logic = {v: k for k, v in logic.items()}

        p2_shape = reverse_logic[p1_outcome]
        p2_shape = Shape[p2_shape]
        weight = p2_shape.weight

        bout_score = weight + p2_outcome
        p2_score += bout_score

    return p2_score


def decrypt2(p1_shape, p2_outcome):
    """Decrypt RPS game round, assuming second column is player 2 outcome."""
    shapes = {'A': Rock, 'B': Paper, 'C': Scissors}
    p1_outcomes = {'X': 6, 'Y': 3, 'Z': 0}
    p2_outcomes = {'X': 0, 'Y': 3, 'Z': 6}

    return shapes[p1_shape], p1_outcomes[p2_outcome], p2_outcomes[p2_outcome]


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = play_by_shape(X)
P1 = play_by_shape(P)
prettyprint(X1, P1)

X2 = play_by_outcome(X)
P2 = play_by_outcome(P)
prettyprint(X2, P2)
