import doctest
import importlib

paths = [['examples.file1', {16: 'sixteen', 45: 'fourty-five'}, 'test1'],
         ['examples.file2', {3: '9', 15: '45'}, 'test2']]

def test(path):
    module_name, extra_tests, function_name = path
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)
    globs = {function.__name__: function} # globals
    new_tests = format_tests(extra_tests, function.__name__)
    doctest.run_docstring_examples(function.__doc__ + new_tests, globs,
                                   name=function.__name__, verbose = True)
    
def format_tests(extra_tests, function_name):
    new_tests = ''
    for keys in extra_tests:
        new_tests += '\t>>> {0}({1})\n'.format(function_name, keys)
        if type(extra_tests[keys]) == str:
            new_tests += "\t'{}'\n".format(extra_tests[keys])
        else:
            new_tests += "\t{}\n".format(extra_tests[keys])
    return new_tests

for path in paths:
    test(path)
