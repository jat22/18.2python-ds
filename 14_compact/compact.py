def compact(lst):
    """Return a copy of lst with non-true elements removed.

        '>>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """


    return [val for val in lst if val]




    # i = 0
    # for e in lst:
    #     print(e)
    #     if not e:
    #         lst.pop(i)
    #     i = i + 1
    # return lst
    # this returns: 
    #  [1, 2, [], (), 'All done']
    # why?????
