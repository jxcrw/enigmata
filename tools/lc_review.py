#!/usr/bin/env python3
"""Review a previously solved LC problem"""

import os
import re
import subprocess
import webbrowser

from dateutil.utils import today

import lc_templates
from tools.lc_tools import build_lc_metadata, time_attempt, update_main_readme, update_problem_readme


def prep_file(prob_id: int) -> str:
    """Create and open new solution file and reference file."""
    # Prepare new solution file
    lc_metadata = build_lc_metadata()
    root = lc_metadata[prob_id]['root']
    files = lc_metadata[prob_id]['files']

    pyfiles = [f for f in files if '.py' in f]
    basename = min(pyfiles)
    filename = basename.replace('.py', f'_{today():%Y-%m-%d}.py')

    # Lookup info of interest from last solution
    last_solution = f'{root}/{pyfiles[-1]}'
    with open(last_solution, 'r', encoding='utf-8') as f:
        code = f.read()
        abspath_last_solution = os.path.abspath(f.name)

    prob_url = re.search(r'"""(.*)"""', code)[1]
    func_sig = re.search(r'def (.*):', code)[1]

    code = lc_templates.review.format(prob_url=prob_url, func_sig=func_sig)
    code_file = f'{root}/{filename}'
    with open(code_file, 'w+', newline='\n', encoding='utf-8') as f:
        f.write(code)
        abspath_new_file = os.path.abspath(f.name)

    readme = f'{root}/README.md'
    abspath_readme = os.path.abspath(readme)

    # Auto-open files/problem in IDE/browser
    cwd = os.getcwd()
    twd = r'C:\~\dev\enigmata'
    os.chdir(twd)
    command = ['neovide.exe', abspath_new_file, abspath_last_solution, abspath_readme, '--multigrid']
    subprocess.run(command)
    # subprocess.run(['idea64.exe', '--line', '0', '--column', '0', abspath_last_solution])
    # subprocess.run(['idea64.exe', '--line', '6', '--column', '12', abspath_new_file])
    webbrowser.open(prob_url, new=0, autoraise=False)

    os.chdir(cwd)

    return filename


if __name__ == '__main__':
    prob_id = int(input("ID: "))
    filename = prep_file(prob_id)

    attempt = time_attempt(focus_mode=True)
    update_problem_readme(prob_id, attempt, filename)
    update_main_readme()
