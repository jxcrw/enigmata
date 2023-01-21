#!/usr/bin/env python3
"""Tools for learning and reviewing LC problems"""

from copy import deepcopy
from datetime import datetime
from itertools import zip_longest
import os
import re
import time
import timeit
from typing import Any

from airium import Airium
import colorama
from colorama import Fore
from dateutil.utils import today
import keyboard
from rich.console import Console
from rich.table import Table

from tools import md

SOLUTIONS_URL = 'https://github.com/jxcrw/enigmata/blob/main/leetcode/{title}'

colorama.init(autoreset=True)


def build_lc_metadata() -> dict:
    """Build sorted dictionary of LC solution metadata."""
    metadata = {}
    root_main = r'../leetcode/'
    for root, dirs, files in os.walk(root_main):
        if root == root_main: continue  # Skip main solutions root directory itself

        prob_title = os.path.basename(root)
        prob_id = prob_title.split('. ')[0]
        anchor = build_anchor(root)

        prob_data = {'root': root, 'title': prob_title, 'anchor': anchor, 'files': files}
        metadata[int(prob_id)] = prob_data

    metadata = {k: metadata[k] for k in sorted(metadata)}
    return metadata


def build_anchor(root: str) -> str:
    """Build anchor for later inclusion in problem table."""
    readme_file = root + '/README.md'
    with open(readme_file, 'r', encoding='utf-8') as f:
        readme = f.read()

    prob_title = os.path.basename(root)
    prob_id, title_text = prob_title.split('. ')
    emoji_search = re.search(r'(🙃|😎|🤯)', readme)
    emoji_tweak = '-' if emoji_search else ''

    anchor = f"#{prob_id}-{title_text.lower().replace(' ', '-')}-solutions{emoji_tweak}"
    return anchor


def update_main_readme():
    """Update main readme."""
    lc_metadata = build_lc_metadata()
    table = build_problem_table(lc_metadata)
    subreadmes = collect_subreadmes(lc_metadata)
    insert_into_main_readme(table, '<!-- Problem table -->')
    insert_into_main_readme(subreadmes, '<!-- Sub-READMEs -->')


def build_problem_table(lc_metadata: dict):
    """Generate HTML problem table."""
    num_cols = 15

    links = []
    for k, data in lc_metadata.items():
        anchor = data['anchor']
        num_solutions = len(data['files']) - 1
        link = f'''<a href="{anchor}">{k}</a><sub>{num_solutions}</sub>'''
        links.append(link)
    links_chunked = chunkit(links, num_cols, '')

    a = Airium()
    with a.table():
        for chunk in links_chunked:
            with a.tr():
                [a.td(align='center', _t=link) for link in chunk]
    table = str(a)
    return table


def collect_subreadmes(lc_metadata: dict) -> str:
    """Collect problem-specific READMEs."""
    filenames = [lc_metadata[k]['root'] + '/README.md' for k in lc_metadata]
    readmes = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as f:
            readme = f.read()
        readme = readme.replace('###', '####') # Make heading level appropriate for main README
        readmes.append(readme)

    readmes = '\n'.join(readmes)
    return readmes


def insert_into_main_readme(text: str, marker: str):
    """Insert text into main README at position indicated by marker."""
    readme_file = '../README.md'
    with open(readme_file, 'r', encoding='utf-8') as f:
        readme = f.read()

    readme = readme.split(marker)
    readme[1] = f'{marker}\n{text}\n{marker}'

    with open(readme_file, 'w+', newline='\n', encoding='utf-8') as f:
        f.write(''.join(readme))


def update_problem_readme(prob_id: int, attempt: tuple[str, ...], filename: str):
    """Update problem-specific readme with solution attempt."""
    lc_metadata = build_lc_metadata()
    root = lc_metadata[prob_id]['root']

    url = sanitize_url(SOLUTIONS_URL.format(**lc_metadata[prob_id]))
    url = f'{url}/{filename}'
    date = f'{today():%Y/%m/%d}'
    think, code, total = attempt
    cols = [date, think, code, total, f'[Python]({url})']

    readme_file = f'{root}/README.md'
    with open(readme_file, 'r', encoding='utf-8') as f:
         readme = f.read()

    table = md.find_table(readme)
    table_new = md.add_table_row(cols, table)
    table_new = md.format_table(table_new)
    readme = readme.replace(table, table_new)

    with open(readme_file, 'w+', newline='\n', encoding='utf-8') as f:
        f.write(readme)


def time_attempt(focus_mode: bool=False) -> tuple[str, ...]:
    """Time solution attempt."""
    input("Setup complete. Press any key to start... ")
    start = time.time()
    input(f"\nStarted at {pretty_instant(start)}. Press any key to start coding... ")
    start_code = time.time()
    if focus_mode: keyboard.press_and_release('F10')

    flag = input(f"\nStarted coding at {pretty_instant(start_code)}. "
                 f"Enter solution flag ('done', 'none', or 'close'): ").strip()
    end = time.time()
    time_think = pretty_timediff(start_code - start)
    time_code = pretty_timediff(end - start_code)
    time_total = pretty_timediff(end - start)

    if flag == 'close': time_total = '≈'
    elif flag == 'none': time_total = '∞'

    attempt = (time_think, time_code, time_total)
    print(f'\nThink: {time_think}\nCode: {time_code}\nTotal: {time_total}\n\nKeep it up :) .')
    return attempt


def pretty_timediff(delta: float) -> str:
    """Pretty-format a time difference."""
    m, s = divmod(round(delta), 60)
    pretty = f'{m:d}:{s:02d}'
    return pretty


def pretty_instant(instant: float) -> str:
    """Pretty-format a time instant."""
    pretty = f'{datetime.fromtimestamp(instant):%H:%M:%S}'
    return pretty


def sanitize_url(url: str) -> str:
    """Sanitize URL."""
    url = url.replace(' ', '%20')
    return url


def chunkit(iterable, n, fillvalue=None):
    """Split iterable up into chunks of length n, with optional padding."""
    chunks = zip_longest(*[iter(iterable)] * n, fillvalue=fillvalue)
    return chunks


def init_solutions(gdict: dict)  -> list[object]:
    """Find and initialize solution classes in a file."""
    with open(gdict['__file__'], 'r', encoding='utf-8') as f:
        code = f.read()

    classnames = re.findall(r'^class (Solution.*?):$', code, re.MULTILINE)
    solutions = [gdict[name]() for name in classnames]
    return solutions


def pretty_eval(solutions: list[Any], method: str, inputs: list, outputs: list) -> None:
    """Evaluate each solution against each example case and pretty-print results."""
    table = Table.grid(padding=(0, 3))
    results_all, failures = [], []

    for s in solutions:
        name = s.__class__.__name__.replace('Solution', '')
        meth = getattr(s, method)
        inputs_fresh = [deepcopy(i) for i in inputs]

        results, solution_correct = [], True
        for i, o in zip(inputs_fresh, outputs):
            result = meth(*i) if isinstance(i, tuple) else meth(i)
            correct = compare(result, o)
            color = Fore.GREEN if correct else Fore.RED
            if result is not None: results.append(color + f'{result}')

            if not correct and result is not None:
                inst_name = s.__class__.__name__.replace('Solution', 's_').lower()
                failures.append(f'{inst_name}.{method}{i}')
                solution_correct = False

        color = Fore.GREEN if solution_correct else Fore.RED
        if results:
            table.add_row(color + f'{name}', *results)
            results_all.extend(results)

    if results_all:
        print(Fore.LIGHTBLACK_EX + '\n--- Examples ---')
        console = Console()
        console.print(table)
    if failures:
        print(Fore.LIGHTBLACK_EX + '\n--- Failed Calls ---')
        print('\n'.join(failures))


def compare(value: Any, ref: Any) -> bool:
    """Return true if equal, false otherwise. Definition of equality depends on type of value."""
    if isinstance(value, list):
        value.sort()
        ref.sort()
    are_equal = value == ref
    return are_equal


def benchmark(solutions: list[Any], method: str, args: Any, number: int) -> None:
    """Print time required to run each solution under specified conditions."""
    table, results = Table.grid(padding=(0, 3)), []
    for s in solutions:
        name = s.__class__.__name__.replace('Solution', '')
        meth = getattr(s, method)

        result = meth(*deepcopy(args)) if isinstance(args, tuple) else meth(deepcopy(args))
        if result is not None:
            args_fresh = deepcopy(args)
            my_lambda = lambda: meth(*args_fresh) if isinstance(args, tuple) else meth(args_fresh)

            time = timeit.timeit(my_lambda, number=number)
            table.add_row(name, f'{time:.4f}')
            results.append(result)

    if results:
        print(Fore.LIGHTBLACK_EX + '\n--- Benchmarks ---')
        console = Console()
        console.print(table)


if __name__ == '__main__':
    build_lc_metadata()
    update_main_readme()
