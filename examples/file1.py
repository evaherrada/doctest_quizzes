def test1(num):
    """ start of docstring
    >>> test1(5)
    'five'
    >>> test1(33)
    'thirty-three'
    >>> test1(99)
    'ninety-nine'
    >>> test1(0)
    'zero'
    >>> test1(15)
    'fifteen'
    >>> test1(45)
    'fourty-five'
    >>> test1(16)
    'sixteen'
    >>> test1(45)
    'fourty-five'
    >>> test1(16)
    'sixteen'
    >>> test1(45)
    'fourty-five'
    >>> test1(16)
    'sixteen'
    >>> test1(45)
    'fourty-five'
    >>> test1(16)
    'sixteen'
    """
    nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    tens = {1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty',
            6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen'}
    if num == 0:
        return 'zero'
    numlist = []
    numstr = ''
    b = str(num)
    for digit in b:
        numlist.append(int(digit))
    for i in range(len(numlist)):
        if len(numlist) == 1:
            numstr = nums[numlist[i]]
            break
        elif numlist[1] == 0:
            numstr = tens[numlist[0]]
            break
        elif len(numlist) == 2 and numlist[0] == 1 and numlist[1] > 0:
            numstr = teens[num]
            break
        else:
            numstr = tens[numlist[0]] + '-'
            numstr += nums[numlist[1]]

    return numstr

if __name__ == '__main__':
    import doctest
    doctest.testmod()
