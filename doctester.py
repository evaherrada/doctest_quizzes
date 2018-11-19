import doctest
import os

paths = [['examples/file1.py', {16: 'sixteen', 45: 'fourty-five'}, 'test1'],
        ['examples/file2.py', {3: '9', 15: '45'}, 'test2']]

def add_tests(paths):
    for i in range(len(paths)):
        with open(paths[i][0], "r+") as f:
            a = f.readlines()
            index = 0
            for item in a:
                if item == "    \"\"\"\n":
                    for k in paths[i][1]:
                        a.insert(index, "    '{0}'\n".format(paths[i][1][k]))
                        a.insert(index, "    >>> {0}({1})\n".format(paths[i][2], k))
                    break
                index += 1
            f.seek(0)
            f.truncate()

            for line in a:
                f.write(line)

def test(paths):
    add_tests(paths)
    for i in range(len(paths)):
        os.system('python3 -m doctest -v {0}'.format(paths[i][0]))

test(paths)
