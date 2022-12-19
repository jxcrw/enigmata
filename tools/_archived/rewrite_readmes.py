#!/usr/bin/env python3
"""Rewrite solution record tables to improve granularity of timing info"""

import re

from tools.format_table import format_table
from tools.utilities import build_solution_metadata_dict


def rewrite_readme(filename: str):
    # Parse original readme
    with open(filename, 'r', encoding='utf-8') as f:
        fulltext = f.read().strip()
    intro, table = fulltext.split('\n\n')

    # Rewrite intro
    emoji_search = re.search(r'(🙃|😎|🤯)', fulltext)
    emoji = ' ' + emoji_search[0] if emoji_search else ''

    intro_lines = intro.split('\n')
    intro_lines[0] += emoji
    intro = '\n'.join(intro_lines)

    # Rewrite table
    table = table.replace('Solution Time', 'Total')
    table = table.replace('Language', 'Solution')
    table = table.replace('Initial solution', '∞')
    table = table.replace('No solution', '∞')
    table = table.replace('Near miss', '≈')
    table = table.replace('Unknown', '∞')
    table = re.sub(r'(🙃|😎|🤯)', '', table)

    table = [line.split('|') for line in table.split('\n')]
    table = [[cell.strip() for cell in row] for row in table]
    table[0].insert(2, 'Think')
    table[0].insert(3, 'Code')
    table[1].insert(2, ':---:')
    table[1].insert(3, ':---:')
    table[2].insert(2, '∞')
    table[2].insert(3, '∞')

    for row in table[3:]:
        row.insert(2, '–')
        row.insert(3, '–')

        row[3], row[4] = row[4], row[3]
        if row[3] == '∞' or row[3] == '≈': row[4] = '∞'

    table = ['|'.join(row) for row in table]
    table = '\n'.join(table)
    table = format_table(table)

    # Glue everything back together
    fulltext_new = intro + '\n\n' + table + '\n'

    with open(filename, 'w+', newline='\n', encoding='utf-8') as f:
        f.write(fulltext_new)


if __name__ == '__main__':
    solution_metadata = build_solution_metadata_dict()
    for k, v in solution_metadata.items():
        root = v['root']
        files = v['files']
        readme = f'{root}/README.md'
        print(readme)
        rewrite_readme(readme)
