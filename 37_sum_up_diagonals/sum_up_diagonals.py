def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    x = 0 
    y = len(matrix) - 1
    diag_sum = 0

    for lst in matrix:
        for num in lst:
            if x == y:
                diag_sum = lst[x] + diag_sum
            else:
                diag_sum = diag_sum + lst[x] + lst[y]
            x = x + 1
            y = y -1
    return diag_sum

m1 = [
    [1,   2],
    [30, 40],
]

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]