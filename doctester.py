import doctest
import os
import datetime

paths = [['examples/file1.py', {16: 'sixteen', 45: 'fourty-five'}, 'test1'],
        ['examples/file2.py', {3: '9', 15: '45'}, 'test2']]
# paths [['path', {input: output}, 'function name', 'student name']]
student_id = '982521'

def add_tests(paths):
    for i in range(len(paths)):
        with open(paths[i][0], "r+") as f:
            a = f.readlines()
            index = 0
            for item in a:
                if item == "    \"\"\"\n":
                    for k in paths[i][1]:
                        docin = "    '{0}'\n".format(paths[i][1][k])
                        docout = "    >>> {0}({1})\n".format(paths[i][2], k)
                        if docin not in a:
                            a.insert(index, docin)
                            a.insert(index, docout)
                    break
                index += 1
            f.seek(0)
            f.truncate()

            for line in a:
                f.write(line)

def test(paths, student_id):
    add_tests(paths)
    for i in range(len(paths)):
        os.system('python3 -m doctest -v {0} >> {1}_{2}.txt'.format(paths[i][0],
            str(student_id), datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))

test(paths, student_id)
