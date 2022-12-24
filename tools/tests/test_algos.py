#!/usr/bin/env python3
"""Test dsa.algos"""

import math

from tools.dsa.algos import *


def test_gcd():
    # Exercises from UND Discrete Math 3rd Edition, Chapter 22.
    assert gcd(233, 89) == 1
    assert gcd(1001, 13) == 13
    assert gcd(2457, 1458) == 27
    assert gcd(567, 349) == 1
    assert gcd(987654321, 123456789) == 9

    # Compare against native math.gcd().
    assert gcd(233, 89) == math.gcd(233, 89)
    assert gcd(1001, 13) == math.gcd(1001, 13)
    assert gcd(2457, 1458) == math.gcd(2457, 1458)
    assert gcd(567, 349) == math.gcd(567, 349)
    assert gcd(987654321, 123456789) == math.gcd(987654321, 123456789)
