def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    lst_of_lists = [item for item in lst if isinstance(item, list)]
    return len(lst_of_lists) == len(lst)
