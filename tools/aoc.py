#!/usr/bin/env python3
"""Reusable tools and convenience functions for AoC"""

from ast import literal_eval
from collections import deque
from datetime import date, datetime, time
import os
import re
import subprocess
from time import sleep
from typing import Any, Deque
import webbrowser

from aocd import get_data

# TODO: Remove dependency on https://github.com/wimglenn/advent-of-code-data


def ready_set_go():
    """Prep files/environment to start solving a puzzle."""
    # Wait for puzzle kickoff
    kickoff = datetime.combine(date.today(), time(21, 0, 0, 500))
    while (curr := datetime.now()) < kickoff:
        diff = kickoff - curr
        print(f'{diff.total_seconds():03.0f}', end='\r')
        sleep(1)

    # Download puzzle data
    year, day = curr.date().year, curr.date().day + 1
    with open('secrets.txt', 'r', encoding='utf-8') as f:
        session = f.read().strip()
    data = get_data(year=year, day=day, session=session)

    with open('_puzzle.txt', 'w+', newline='\n', encoding='utf-8') as f:
        f.write(data)
        abspath_data = os.path.abspath(f.name)

    # Auto-open files/problem in IDE/browser
    url = f'https://adventofcode.com/{year}/day/{day}'
    subprocess.run(['subl.exe', abspath_data])
    webbrowser.open(url, new=0, autoraise=False)
    return


def load(filename: str, pre: int = 0) -> tuple[str, str]:
    """Read data from file, peeling the specified number of lines of predata from the beginning."""
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read().strip()
        data = data.split('\n')
        data = '\n'.join(data[pre:]).strip()
        peeled = '\n'.join(data[:pre]).strip()
    return data, peeled


def superparse(data: Any, seps: Deque[str] = deque(), str_to_num: str = 'int', extract_num: bool = False) -> list[Any]:
    """Recursively split string data into plain lists + intelligently cast data types."""
    args = {'seps': seps, 'str_to_num': str_to_num, 'extract_num': extract_num}
    data = data.strip()

    if not seps:
        if str_to_num:
            data = smartnum(data, str_to_num)
        elif extract_num:
            data = extract_nums(data)
        return data

    sep = seps.popleft()
    if sep == 'char':
        data = list(data)
    else:
        data = re.split(sep, data)

    for i, item in enumerate(data):
        item = superparse(item, **args)
        data[i] = item

    seps.appendleft(sep)
    return data


def smartnum(s: str, num_type: str) -> int | float | str:
    """Convert number-like strings to numbers, falling back to string if necessary."""
    r = ''
    try:
        lit = literal_eval(s)
        if isinstance(lit, int):
            if num_type == 'bin':
                r = int(s, 2)
            elif num_type == 'hex':
                r = int(s, 16)
            else:
                r = int(s)
        elif isinstance(lit, float):
            r = float(s)
    except:
        r = s
    return r


def is_binary(s: str) -> bool:
    """Determine whether string represents a binary number."""
    for c in s:
        if c not in '01':
            return False
    return True


def extract_nums(s: str) -> list[int]:
    """Extract ints from string."""
    nums = re.findall(r'\d+', s)
    nums = [int(n) for n in nums]
    return nums


def prettyprint(*results) -> None:
    """Pretty-print results with minimal distractions."""
    output = [str(r) for r in results if r]
    output = '\n'.join(output) + '\n'
    if output: print(output)


def submit(part: str, result: Any) -> None:
    """Submit result for specified part."""
    result = str(result)
    print(f'submitting {part}...\n')
    pass


if __name__ == '__main__':
    ready_set_go()
