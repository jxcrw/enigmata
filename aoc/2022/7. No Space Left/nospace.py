#!/usr/bin/env python3
"""https://adventofcode.com/2022/day/7"""

import os
import re

from tools.aoc import load, prettyprint

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Inputs
# └─────────────────────────────────────────────────────────────────────────────
X, _ = load('_example.txt', pre=0)
P, _ = load('_puzzle.txt', pre=0)

print(f'n_X: {len(X)}   n_P: {len(P)}\n')


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
def create_shellscript(sesh: str, basename: str) -> str:
    """Convert a terminal session to an executable shell script.
    Return the absolute path of the created shell script."""
    command_init = f'rm -rf {basename}\nmkdir {basename}\ncd {basename}\n'
    sesh = command_init + sesh

    sesh = re.sub(r'\$ cd /', r'', sesh)                                # $ cd / → <nothing>
    sesh = re.sub(r'^\$ ', r'', sesh, flags=re.M)                       # $ command → command
    sesh = re.sub(r'^dir ', 'mkdir ', sesh, flags=re.M)                 # dir dirname → mkdir dirname
    sesh = re.sub(r'^(\d+) (.*?)$', r'touch "\1_\2"', sesh, flags=re.M) # 123 file.txt → touch "123_file.txt"

    with open(f'{basename}.sh', 'w+', newline='\n', encoding='utf-8') as f:
        f.write(sesh)
        abspath_script = os.path.abspath(f.name)

    return abspath_script

# Create shellscripts
cwd = os.getcwd()
basename_X = 'temp_X'
basename_P = 'temp_P'
script_X = create_shellscript(X, basename_X)
script_P = create_shellscript(P, basename_P)
# subprocess.run(['bash.exe', script_X, cwd])
# subprocess.run(['bash.exe', script_P, cwd])


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 1
# └─────────────────────────────────────────────────────────────────────────────
def sum_tinydirs(entrypoint: str) -> int:
    """Compute total size of "tiny" dirs that are ≤ 100_000 units in size."""
    total = 0
    for root, dirs, files in os.walk(entrypoint):
        dirsize = get_dirsize(root)
        if dirsize <= 100000:
            total += dirsize
    return total


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Part 2
# └─────────────────────────────────────────────────────────────────────────────
DISKSPACE = 70000000
NEEDED = 30000000

def min_deletesize(entrypoint: str) -> float:
    """Find the size of the smallest dir that, when deleted,
    will free up enough disk space for a system update."""
    deletesize = float('inf')
    unused = DISKSPACE - get_dirsize(entrypoint)

    for root, dirs, files in os.walk(entrypoint):
        dirsize = get_dirsize(root)
        if dirsize + unused >= NEEDED:
            deletesize = min(deletesize, dirsize)

    return deletesize


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Helpers
# └─────────────────────────────────────────────────────────────────────────────
def get_dirsize(directory: str) -> int:
    """Compute the total size of all files in a directory."""
    dirsize = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            fileinfo = file.split('_')
            filesize = int(fileinfo[0])
            dirsize += filesize
    return dirsize


# ┌─────────────────────────────────────────────────────────────────────────────
# │ Outputs
# └─────────────────────────────────────────────────────────────────────────────
X1 = sum_tinydirs(basename_X)
P1 = sum_tinydirs(basename_P)
prettyprint(X1, P1)

X2 = min_deletesize(basename_X)
P2 = min_deletesize(basename_P)
prettyprint(X2, P2)
