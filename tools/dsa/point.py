#!/usr/bin/env python3
"""Point stuff"""

from math import sqrt


class Point:
    """A point in 2D space."""

    PLANCK = sqrt(2)

    def __init__(self, x: int = 0, y: int = 0, name: str = ''):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        return f'<{self.x}, {self.y}, {self.name}>'

    def pos(self) -> tuple[int, int]:
        """Get position of point."""
        return self.x, self.y

    def move(self, direction: str, amount: int = 0) -> None:
        """Move point in direction by given amount."""
        match direction:
            case 'L': self.x -= amount
            case 'R': self.x += amount
            case 'U': self.y += amount
            case 'D': self.y -= amount
            case _:
                raise Exception('Unsupported direction.')

    def follow(self, leader: 'Point') -> None:
        """Maintain contact with another point."""
        dist = self.distance(leader)
        if dist > self.PLANCK:
            hop_x = round((leader.x - self.x) / self.PLANCK) # Magic, any divisor ≥ ≈1.4 and < 2 works ¯\_(ツ)_/¯
            hop_y = round((leader.y - self.y) / self.PLANCK)
            self.x += hop_x
            self.y += hop_y

    def distance(self, point: 'Point') -> float:
        """Compute the distance from this point to another point."""
        x1, x2 = self.x, point.x
        y1, y2 = self.y, point.y
        dist = sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        return dist
