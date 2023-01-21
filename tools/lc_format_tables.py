#!/usr/bin/env python3
"""Tools for learning and reviewing LC problems"""

import os

from tools import md


def find_solution_readmes() -> list[str]:
    """Find all LeetCode solution readme files."""
    readmes = []
    root_main = r'../leetcode/'
    for root, dirs, files in os.walk(root_main):
        if root == root_main: continue  # Skip main solutions root directory itself

        files = [f'{root}/{f}' for f in files if '.md' in f]
        readmes.extend(files)

    return readmes


def format_readme_tables(files: list[str]) -> None:
    """Format tables in solution readmes."""
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            readme = f.read()

        table = md.find_table(readme)
        table_formatted = md.format_table(table)
        readme = readme.replace(table, table_formatted)

        with open(file, 'w+', newline='\n', encoding='utf-8') as f:
            f.write(readme)


if __name__ == '__main__':
    files = find_solution_readmes()
    format_readme_tables(files)
