import doctest
import importlib
import ast


class tester:
    def __init__(self, everything):
        self.filename, self.extra_tests, self.function_name = everything

    def test(self):
        module = importlib.import_module(self.filename)
        self.function = getattr(module, self.function_name)
        globs = {self.function.__name__: self.function}  # globals
        self.new_tests = tester.format_tests(self)
        print('\n')
        doctest.run_docstring_examples(
            self.function.__doc__ + self.new_tests,
            globs,
            name=self.function.__name__,
            verbose=True
        )
        print('\n')

    def format_tests(self):
        new_tests = ''
        for keys in self.extra_tests:
            keysk = keys
            if str(keys)[0] == '[':
                keysk = ast.literal_eval(keys)

            keysv = self.extra_tests[keys]
            if str(self.extra_tests[keys])[0] == '[':
                keysv = ast.literal_eval(self.extra_tests[keys])

            if type(keysk) == str:
                new_tests += "\t>>> {0}('{1}')\n".format(self.function_name,
                                                         keysk)
            else:
                new_tests += '\t>>> {0}({1})\n'.format(self.function_name,
                                                       keysk)
            if type(keysv) == str:
                new_tests += "\t'{}'\n".format(keysv)
            else:
                new_tests += "\t{}\n".format(keysv)
        return new_tests


class runner:
    def __init__(self, quiz):
        self.quiz = quiz
        print('\n***** IMPORTANT *****')
        print('Make a newline, then press CTRL+D to submit question\n')

    def run(self, paths):
        input("Press enter to start/continue")
        print('\n')
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
paths = [['question1', {-2: -1, 15: 16, 1.5: 2.5}, 'addone'],
         ['question2', {3: 2, -15: -16, 2.5: 1.5}, 'subtractone'],
         ['question3', {-100: 100, 100: 100, -2.5: 2.5}, 'absolute'],
         ['question4', {10: 30, -10: -30, 1.5: 4.5}, 'timesthree'],
         ['question5', {'fake_name': 'hello fake_name', '7': 'hello 7'},
          'hello']]


# quiz = 'quiz2'
# paths = [['question1', {'[15, 16, 17, 18]': '[16, 18]'}, 'only_evens']]

run = runner(quiz)
for path in paths:
    run.run(path)
