def test2(num):
    """ start of docstring
    >>> test2(10)
    '30'
    >>> test2(2)
    '6'
    >>> test2(15)
    '45'
    >>> test2(3)
    '9'
    >>> test2(15)
    '45'
    >>> test2(3)
    '9'
    >>> test2(15)
    '45'
    >>> test2(3)
    '9'
    >>> test2(15)
    '45'
    >>> test2(3)
    '9'
    """
    return str(num * 3)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
