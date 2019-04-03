# Opens file. File get's printed. ___ gets treated as input field.
# Input gets written to file at specific location. code gets tested.

from doctester import tester

paths = [['question1', {-2: -1, 15: 16}, 'addone'],
         ['question2', {3: 2, -15: -16}, 'subtractone']]


def runner(paths):
    filename, extra_tests, function_name = paths
    QuestionF = open('questions/'+filename+'.py', 'r')
    AnswerF = open('answers/'+filename+'_answer.py', 'w')

    QStr = QuestionF.read()
    QList = QStr.split('___')
    print(QList[0], end="")
    answer = input()
    print(QList[1])

    AStr = QList[0] + answer + QList[1]
    AnswerF.write(AStr)

    QuestionF.close()
    AnswerF.close()

    tests = tester(['answers.'+filename+'_answer', extra_tests, function_name])
    tests.test()


for path in paths:
    runner(path)
