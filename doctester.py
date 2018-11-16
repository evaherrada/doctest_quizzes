from typing import List, Optional
import os

def test(
        paths: List[str]):
    for i in paths:
        os.system('python3 ' + i)

paths = ['/home/dherrada/school_projects/new_python_cert/doctest_quizzes/examples/file1.py']

test(paths)
