#!/usr/bin/env python3
"""RPS engine"""

from enum import Enum

# TODO: Make it easier to override game constants

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Game Constants
# └─────────────────────────────────────────────────────────────────────────────
# Shape names
NAME_R = 'R'
NAME_P = 'P'
NAME_S = 'S'

# Shape weights (optional)
WEIGHT_R = 1
WEIGHT_P = 2
WEIGHT_S = 3

# Game outcomes
WIN = 6
LOSE = 0
DRAW = 3

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Game Objects
# └─────────────────────────────────────────────────────────────────────────────
class Shape(Enum):
    R = (WEIGHT_R, {NAME_R: DRAW, NAME_P: LOSE, NAME_S: WIN})
    P = (WEIGHT_P, {NAME_R: WIN,  NAME_P: DRAW, NAME_S: LOSE})
    S = (WEIGHT_S, {NAME_R: LOSE, NAME_P: WIN,  NAME_S: DRAW})

    def __init__(self, weight: int, logic: dict):
        self.weight = weight
        self.logic = logic

    def battle(self, other: 'Shape') -> int:
        """Determine outcome of playing this shape versus another shape."""
        outcome = self.logic[other.name]
        return outcome


if __name__ == '__main__':
    R = Shape.R
    P = Shape.P
    S = Shape.S

    print(R.battle(S))
