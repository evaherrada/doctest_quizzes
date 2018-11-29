def test4(string):
    """ begin docstring
    >>> test4('5')
    5
    >>> test4('10')
    10
    """
    return int(string)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
