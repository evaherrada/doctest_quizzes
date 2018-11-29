def test3(nums):
    """ start of docstring 
    >>> test3([1, 2, 3])
    [2, 6]
    """
    a = []
    avg = 0
    sumnum = 0
    for i in range(len(nums)):
        avg += nums[i]
        sumnum += nums[i]
    if nums[0] % int(nums[0]):
        a.append(avg/len(nums))
    else:
        a.append(int(avg/len(nums)))
    a.append(sumnum)
    return a

if __name__ == '__main__':
    import doctest
    doctest.testmod()
