import os
import datetime

paths = [['examples/file1.py', {16: 'sixteen', 45: 'fourty-five'}, 'test1'],
         ['examples/file2.py', {3: '9', 15: '45'}, 'test2'],
         ['examples/file3.py', {(2, 4): [3, 6]}, 'test3'],
         ['examples/file4.py', {'15': 15, '33': 33}, 'test4']]
# Lists in the key slot of the dict MUST be defined as tuples
# paths [['path', {input: output}, 'function name', 'student name']]
# add defining dict keys as strings
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
        date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = '{0}_{1}.txt'.format(str(student_id), date_time)
        os.system('python3 -m doctest -v {0} >> {1}'.format(paths[i][0],
                                                            filename))
    score_compiler(filename)


def score_compiler(filename):
    f = open(filename, "r+")
    lines = f.readlines()
    a = [x.rstrip() for x in lines]
    b = [x.strip(' ') for x in a]
    trying = []
    expecting = []
    got = []
    for i in range(len(b)):
        if b[i] == 'Trying:':
            trying.append(b[i+1])
            continue
        elif b[i] == 'Expecting:':
            expecting.append(b[i+1])
        if b[i] == 'Got:':
            got.append(b[i+1])
            continue
        elif b[i] == 'Expecting:' and '*' not in b[i+2]:
            got.append(b[i+1])
    master = []
    for i in range(len(trying)):
        c = []
        c.append(trying[i])
        c.append(expecting[i])
        c.append(got[i])
        master.append(c)
    score_evaluator(master, f, lines)


def score_evaluator(master_list, f, lines):
    f.seek(0)
    correct = 0
    wrong = 0
    for i in master_list:
        if i[1] != i[2]:
            character = u'\u274c'
            wrong += 1
        else:
            character = u'\u2713'
            correct += 1
        f.write('{0} Tried: {1} Expected: {2} Got: {3}\n'.format(character,
                i[0], i[1], i[2]))
    f.write('Total Correct: {0}\nTotal Incorrect: {1}\nScore: {2}\n\n'.format(
            correct, wrong, (correct/(correct+wrong)*100)))
    for line in lines:
        f.write(line)
    f.close()


test(paths, student_id)
