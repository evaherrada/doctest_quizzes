def file1(num):
    """
    >>> file1(5)
    'five'
    >>> file1(33)
    'thirty-three'
    >>> file1(99)
    'ninety-nine'
    >>> file1(0)
    'zero'
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
    while num >= 10:
        num = num // 10
        numlist.append(num)
    if num > 0:
        numlist.append(num)
    for i in range(len(numlist)):
        if not num % 10:
            numstr += tens[numlist[i]]
            break
        elif num > 10 and num < 20:
            numstr += teens[numlist[i]]
            break
        else:
            if i + 1 < len(numlist):
                numstr += tens[numlist[i]] + '-'
            else:
                numstr += nums[numlist[i]]

    return numstr
if __name__ == '__main__':
    import doctest
    doctest.testmod()
