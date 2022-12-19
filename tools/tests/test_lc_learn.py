#!/usr/bin/env python3
"""Test lc_learn.py"""

from tools.lc_learn import *


def test_sanitize_io():
    # Input sanitization
    single = 's = "aab"'
    multi = 's = "input", t = "output", k = 9'
    iterable = 's = [1,2,3]'
    iterable_alt = 's = [1, 2, 3]'
    iterable_multi = 's = [1,2,3], t = (1,2,3), k = 9'

    assert sanitize_io(single) == "'aab'"
    assert sanitize_io(multi) == "('input', 'output', 9)"
    assert sanitize_io(iterable) == "[1, 2, 3]"
    assert sanitize_io(iterable_alt) == "[1, 2, 3]"
    assert sanitize_io(iterable_multi) == "([1, 2, 3], (1, 2, 3), 9)"


def test_build_snippet():
    metadata1 = "{ \r\n  \"name\": \"rearrangeString\",\r\n  \"params\": [\r\n    { \r\n      \"name\": \"s\",\r\n      \"type\": \"string\"\r\n    },\r\n    {\r\n      \"name\": \"k\",\r\n      \"type\": \"integer\"\r\n    }\r\n  ],\r\n  \"return\": {\r\n    \"type\": \"string\"\r\n  }\r\n}"
    expected1 = 'rearrangeString', 'rearrangeString(self, s: str, k: int) -> str'
    assert build_snippet(metadata1) == expected1
