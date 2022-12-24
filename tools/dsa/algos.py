#!/usr/bin/env python3
"""Common algorithms"""

def gcd(a: int, b: int) -> int:
    """Find the greatest common divisor of a and b. But use math.gcd() in production :) ."""
    if b == 0: return a
    a, b = b, a % b
    return gcd(a, b)


if __name__ == '__main__':
    pass

