import doctest
import os
import datetime

paths = [['examples/file1.py', {16: 'sixteen', 45: 'fourty-five'}, 'test1'],
        ['examples/file2.py', {3: '9', 15: '45'}, 'test2'],
        ['examples/file3.py', {(2, 4): [3, 6]}, 'test3'],
        ['examples/file4.py', {'15': 15, '33': 33}, 'test4']]
# Lists in the key slot of the dict MUST be defined as tuples
# paths [['path', {input: output}, 'function name', 'student name']]
student_id = '982521'
# Get type of docout
# use type when writing
def add_tests(paths, student_id):
    for i in range(len(paths)):
        with open(paths[i][0], "r+") as f:
            a = f.readlines()
            index = 0
            for item in a:
                if item == "    \"\"\"\n":
                    for k in paths[i][1]:
                        outtype = type(paths[i][1][k])
                        intype = type(k)
                        if outtype == str:
                            docout = "    '{0}'\n".format(paths[i][1][k])
                        else:     
                            docout = "    {0}\n".format(paths[i][1][k])

                        if intype == str:
                            docin = "    >>> {0}('{1}')\n".format(paths[i][2],
                                    k)
                        elif intype == tuple:
                            docin = "    >>> {0}({1})\n".format(paths[i][2],
                                    list(k))
                        else:
                            docin = "    >>> {0}({1})\n".format(paths[i][2], k)

                        if docin not in a:
                            a.insert(index, docout)
                            a.insert(index, docin)
                    break
                index += 1
            f.seek(0)
            f.truncate()

            for line in a:
                f.write(line)

def test(paths, student_id):
    add_tests(paths, student_id)
    for i in range(len(paths)):
        filename = '{0}_{1}.txt'.format(str(student_id),
                datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        os.system('python3 -m doctest -v {0} >> {1}'.format(paths[i][0],
                    filename))
        # score_evaluator(score_calculator(filename))

def score_compiler(filename):
    f = open(filename, "r+")
    a = [x.rstrip() for x in f]
    a = [x.strip(' ') for x in a]
    trying = []
    expecting = []
    got = []
    for i in range(len(a)):
        if a[i] == 'Trying:':
            trying.append(a[i+1])
            continue
        elif a[i] == 'Expecting:':
            expecting.append(a[i+1])
        if a[i] == 'Got:':
            got.append(a[i+1])
            continue
        elif a[i] == 'Expecting:' and '*' not in a[i+2]:
            got.append(a[i+1])
    master = []
    for i in range(len(trying)):
        b = []
        b.append(trying[i])
        b.append(expecting[i])
        b.append(got[i])
        master.append(b)
    return master

# score_evaluator(master_list):

# score_compiler('982521_2018-11-19_18-31-06.txt')

test(paths, student_id)
