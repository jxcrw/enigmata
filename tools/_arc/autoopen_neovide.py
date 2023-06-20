#!/usr/bin/env python3
"""Auto-open files in Neovim for review/learning"""

import subprocess
import os

# Auto-open files/problem in Neovide (for reviewing old problems)
cwd = os.getcwd()
twd = r'C:\~\dev\enigmata'
os.chdir(twd)
command = ['neovide.exe', abspath_new_file, abspath_last_solution, abspath_readme, '--multigrid'] # For reviewing old problems
command = ['neovide.exe', abs_path_code, abs_path_readme, '--multigrid'] # For learning new problems
subprocess.run(command)
os.chdir(cwd)
