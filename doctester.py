# import doctest
# import importlib

paths = [['examples.file1', {16: 'sixteen', 45: 'fourty-five'}, 'test1'],
         ['examples.file2', {3: '9', 15: '45'}, 'test2']]


class tester:
    def __init__(self, everything):
        self.filename, self.extra_tests, self.function_name = everything
        self.importlib = __import__('importlib')
        self.doctest = __import__('doctest')

    def test(self):
        module = self.importlib.import_module(self.filename)
        self.function = getattr(module, self.function_name)
        globs = {self.function.__name__: self.function}  # globals
        self.new_tests = tester.format_tests(self)
        self.doctest.run_docstring_examples(
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


if __name__ == '__main__':
    for path in paths:
        p1 = tester(path)
        p1.test()
