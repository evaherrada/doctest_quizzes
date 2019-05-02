# Doctest Quiz

### test
#### Parameters
* quiz
    * This parameter specifies the name of the folder that the quiz items are in.
    * This is a relative path
    * Syntax
        * path.to.folder

* paths
  * Syntax
    * `[['filename', {extra_tests}, 'function_name']]`
        * filename
            * Name of the question file
            * Should be a string
        * extra_tests
            * Key is the doctest in ('>>>' line in a normal doctest)
            * Value is doctest out (line after '>>>' in a normal doctest)
    * doctest in can be a string, integer, float, or list (list must be formatted as a string Eg. '[1, 2]')
    * doctest out can be a string, int, or list
