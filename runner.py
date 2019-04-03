# Opens file. File get's printed. ___ gets treated as input field.
# Input gets written to file at specific location. code gets tested.

#from doctester import tester

quiz = 'quiz1'
paths = [['question1', {-2: -1, 15: 16}, 'addone'],
         ['question2', {3: 2, -15: -16}, 'subtractone']]

class runner:
    def __init__(self, quiz):
        self.quiz = quiz
        self.importlib = __import__('importlib')
        self.tester = self.importlib.import_module('doctester')

    def run(self, paths):
        filename, extra_tests, function_name = paths
        QuestionF = open('quizzes/'+self.quiz+'/'+filename+'.py', 'r')
        AnswerF = open('answers/'+self.quiz+'/'+filename+'_answer.py', 'w')

        QStr = QuestionF.read()
        QList = QStr.split('___')
        print(str(QList[0])[:-4], end="")
        answer = input('    ')
        print(QList[1])

        AStr = QList[0] + answer + QList[1]
        AnswerF.write(AStr)

        QuestionF.close()
        AnswerF.close()

        tests = self.tester.tester(['answers.'+self.quiz+'.'+filename+'_answer', extra_tests, function_name])
        tests.test()


run = runner(quiz)
for path in paths:
    run.run(path)
