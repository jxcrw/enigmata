#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/5"""

from collections import deque

from tools.aoc import load, prettyprint, superparse

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, _ = load('_example.txt', pre=4)
P, _ = load('_puzzle.txt', pre=9)

seps = deque(['\n'])
args = {'seps': seps, 'str_to_num': '', 'extract_num': True}
X = superparse(X, **args)
P = superparse(P, **args)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')

# Hand-munged starting data
rawstacks_X = '''
NZ
DCM
P
'''

rawstacks_P = '''
WBGZRDCV
VTSBCFWG
WNSBC
PCVJNMGQ
BHDFLST
NMWTVJ
GTSCLFP
ZDB
WZNM
'''


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1
# └─────────────────────────────────────────────────────────────────────────────
def reorg_9000(rawstacks, procedure):
    """Move crates around between stacks one crate at a time."""
    stacks = parse_stacks(rawstacks)

    for line in procedure:
        amt, src, dest = line
        for i in range(amt):
            crate = stacks[src].pop()
            stacks[dest].append(crate)

    tops = get_top_crates(stacks)
    return tops


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 2
# └─────────────────────────────────────────────────────────────────────────────
def reorg_9001(rawstacks, procedure):
    """Move crates around between stacks multiple crates at a time."""
    stacks = parse_stacks(rawstacks)

    for line in procedure:
        amt, src, dest = line

        crates = stacks[src][-amt:]
        del stacks[src][-amt:]
        stacks[dest].extend(crates)

    tops = get_top_crates(stacks)
    return tops


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Helpers
# └─────────────────────────────────────────────────────────────────────────────
def parse_stacks(rawstacks: str) -> dict:
    """Convert stacks from raw string representation to dictionary."""
    rawstacks = rawstacks.strip().split('\n')

    stacks = {}
    for i, rawstack in enumerate(rawstacks):
        stack = list(rawstack[::-1])
        stacks[i + 1] = stack

    return stacks

def get_top_crates(stacks: dict) -> str:
    """Concatenate top crate from each stack."""
    tops = []
    for _, crates in stacks.items():
        if crates:
            tops.append(crates[-1])

    tops = ''.join(tops)
    return tops


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = reorg_9000(rawstacks_X, X)
P1 = reorg_9000(rawstacks_P, P)
prettyprint(X1, P1)

X2 = reorg_9001(rawstacks_X, X)
P2 = reorg_9001(rawstacks_P, P)
prettyprint(X2, P2)
