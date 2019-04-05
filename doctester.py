import doctest
import importlib

class tester:
    def __init__(self, everything):
        self.filename, self.extra_tests, self.function_name = everything

    def test(self):
        module = importlib.import_module(self.filename)
        self.function = getattr(module, self.function_name)
        globs = {self.function.__name__: self.function}  # globals
        self.new_tests = tester.format_tests(self)
        doctest.run_docstring_examples(
            self.function.__doc__ + self.new_tests,
            globs,
            name=self.function.__name__,
            verbose=True
        )

    def format_tests(self):
        new_tests = ''
        for keys in self.extra_tests:
            new_tests += '\t>>> {0}({1})\n'.format(self.function_name, keys)
            if type(self.extra_tests[keys]) == str:
                new_tests += "\t'{}'\n".format(self.extra_tests[keys])
            else:
                new_tests += "\t{}\n".format(self.extra_tests[keys])
        return new_tests


class runner:
    def __init__(self, quiz):
        self.quiz = quiz

    def run(self, paths):
        input("Press enter to start/continue")
        filename, extra_tests, function_name = paths
        QuestionF = open('quizzes/'+self.quiz+'/'+filename+'.py', 'r')
        AnswerF = open('answers/'+self.quiz+'/'+filename+'_answer.py', 'w')

        QStr = QuestionF.read()
        QList = QStr.split('___')
        print(str(QList[0])[:-4], end="")
        
        AnswerF.write(QList[0][:-4])

        while True:
            try:
                answer = input('    ')
            
                AnswerF.write('    ' + answer + '\n')
        
            except EOFError:
                break

        QuestionF.close()
        AnswerF.close()

        tests = tester(['answers.'+self.quiz+'.'+filename + '_answer', 
                        extra_tests, function_name])
        tests.test()


quiz = 'quiz1'
paths = [['question1', {-2: -1, 15: 16}, 'addone'],
         ['question2', {3: 2, -15: -16}, 'subtractone']]

run = runner(quiz)
for path in paths:
    run.run(path)
