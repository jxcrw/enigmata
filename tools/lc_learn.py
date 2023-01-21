#!/usr/bin/env python3
"""Learn a new LC problem"""

import json
import os
import re
import subprocess

import pyperclip
import requests
from bs4 import BeautifulSoup

import lc_templates
from lc_tools import SOLUTIONS_URL, sanitize_url, time_attempt, update_main_readme, update_problem_readme


DEBUG = True


def get_prob_info_auto() -> dict:
    """Gather relevant problem info automatically."""
    prob_url = input("URL: ")
    basename = input("File basename: ")
    q = get_question_data(prob_url)

    prob_id = q['questionFrontendId']
    title = prob_id + '. ' + q['title']
    func_name, func_sig = build_snippet(q['metaData'])

    prob_info = {'q': q, 'title': title, 'prob_id': int(prob_id), 'prob_url': prob_url,
                 'basename': basename, 'func_sig': func_sig, 'func_name': func_name}
    return prob_info


def get_prob_info_manual() -> dict:
    """Gather relevant problem prob_info manually."""
    title = input("Problem title: ")
    prob_url = input("URL: ")
    basename = input("File basename: ")
    func = input("Function signature: ")
    func_sig, func_name = sanitize_func(func)
    prob_id = int(title.split('.')[0])

    prob_info = {'title': title, 'prob_id': prob_id, 'prob_url': prob_url,
                 'basename': basename, 'func_sig': func_sig, 'func_name': func_name}
    return prob_info


def get_examples_auto(prob_info: dict) -> dict:
    """Get example inputs and outputs automatically."""
    soup = BeautifulSoup(prob_info['q']['content'], 'html.parser')
    text = soup.get_text()

    inputs = re.findall(r'Input: (.*)', text)
    outputs = re.findall(r'Output: (.*)', text)
    inputs = [sanitize_io(i) for i in inputs]
    outputs = [sanitize_io(o) for o in outputs]

    benchmark_input = inputs[-1]
    inputs = '[' + ', '.join(inputs) + ']'
    outputs = '[' + ', '.join(outputs) + ']'

    example_info = {'inputs': inputs, 'outputs': outputs, 'benchmark_input': benchmark_input}
    prob_info.update(example_info)
    return prob_info


def get_examples_manual(prob_info: dict) -> dict:
    """Get example inputs and outputs manually."""
    inputs, outputs = [], []
    while True:
        i = sanitize_io(input("Input: "))
        o = sanitize_io(input("Output: "))
        if i == 'done' or o == 'done': break
        inputs.append(i)
        outputs.append(o)

    benchmark_input = inputs[-1]
    inputs = '[' + ', '.join(inputs) + ']'
    outputs = '[' + ', '.join(outputs) + ']'

    example_info = {'inputs': inputs, 'outputs': outputs, 'benchmark_input': benchmark_input}
    prob_info.update(example_info)
    return prob_info


def prep_files(prob_info: dict):
    """Create and open solution file and readme."""
    # Prep directory
    root = r'../leetcode/{title}'.format(**prob_info)
    basename = prob_info['basename']
    os.makedirs(root, exist_ok=True)

    # Prep solution file
    code = lc_templates.solution.format(**prob_info)
    code_file = f'{root}/{basename}'
    with open(code_file, 'w+', newline='\n', encoding='utf-8') as f:
        f.write(code)
        abs_path_code = os.path.abspath(f.name)

    # Prep readme
    solutions_url = sanitize_url(SOLUTIONS_URL.format(**prob_info))
    readme = lc_templates.readme.format(solutions_url=solutions_url, **prob_info)
    with open(f'{root}/README.md', 'w+', newline='\n', encoding='utf-8') as f:
        f.write(readme)
        abs_path_readme = os.path.abspath(f.name)

    # Auto-open files in IDE
    subprocess.run(['idea64.exe', abs_path_readme])
    subprocess.run(['idea64.exe', '--line', '9', '--column', '12', abs_path_code])
    return None


def prep_anki_card(prob_info: dict) -> str:
    html = lc_templates.anki.format(**prob_info)
    print("\nAnki HTML on clipboard :) .")
    pyperclip.copy(html)
    return html


def get_question_data(prob_url: str) -> dict:
    """Get JSON object with all question data from LC."""
    slug = re.search(r'https://leetcode.com/problems/(.*?)/', prob_url)[1]
    query = {"operationName": "questionData",
             "variables": {"titleSlug": slug},
             "query": lc_templates.graphql_query}
    r = requests.post('https://leetcode.com/graphql', json=query).json()

    if DEBUG:
        with open('question.json', 'w+', newline='\n', encoding='utf-8') as f:
            json.dump(r, f, indent=2, ensure_ascii=False)

    q = r['data']['question']
    return q


def build_snippet(metadata: dict) -> tuple[str, str]:
    """Manually build solution snippet from LC snippet metadata."""
    metadata = json.loads(metadata)
    if DEBUG:
        with open('metadata.json', 'w+', newline='\n', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)

    method = metadata['name']
    params = [[p['name'], pytype(p['type'])] for p in metadata['params']]
    params = ', '.join([': '.join(p) for p in params])
    ret_type = pytype(metadata['return']['type'])

    sig = lc_templates.sig.format(method=method, params=params, ret_type=ret_type)
    return method, sig


def pytype(_type: str) -> str:
    """Convert LC snippet metadata type to Pythonic type."""
    type_map = {
        'string': 'str',
        'integer': 'int',
        'boolean': 'bool',
        'character[]': 'list[str]',
        'integer[]': 'list[int]',
        'list<list<integer>>': 'list[list[int]]',
    }
    python_type = type_map[_type] if _type in type_map else _type
    return python_type


def sanitize_func(sig: str) -> tuple[str, str]:
    """Make LC's Python function signatures 3.10-compliant."""
    sig = sig.replace("List", "list")
    sig = re.sub(r'Optional\[(.*?)\]', r'\1 | None', sig)
    name = re.search(r'^(.*?)\(', sig)[1]
    return sig, name


def sanitize_io(io: str) -> str:
    """Make LC's example IOs PEP8-compliant."""
    # Input-specific sanitization
    if '=' in io:
        single = io.count('=') == 1
        if single:
            io = io.split('=')[1]
        else:
            inputs = io.split(', ')
            inputs = [i.split(' = ') for i in inputs]
            vals = [i[1] for i in inputs]
            io = '(' + ','.join(vals) + ')'

    # Common sanitization
    io = re.sub(r'(\S),(?=\S)', r'\1, ', io)  # Always single space after comma
    io = io.replace('"', '\'')
    io = io.replace('null', 'None')
    io = io.replace('true', 'True')
    io = io.replace('false', 'False')
    io = io.strip()
    return io


def sanitize_snippet(snippet: str) -> str:
    """Sanitize code snippet."""
    snippet = snippet.replace('\r\n', '\n')
    return snippet


if __name__ == '__main__':
    mode = 'auto'
    if mode == 'auto':
        prob_info = get_prob_info_auto()
        get_examples_auto(prob_info)
    elif mode == 'manual':
        prob_info = get_prob_info_manual()
        get_examples_manual(prob_info)

    prep_files(prob_info)
    prep_anki_card(prob_info)

    attempt = time_attempt()
    prob_id = prob_info['prob_id']
    filename = prob_info['basename']
    update_problem_readme(prob_id, attempt, filename)
    update_main_readme()
