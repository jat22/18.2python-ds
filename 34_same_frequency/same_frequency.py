def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num2 = str(num2)

    num1_map = {}
    for x in num1:
        num1_map[x] = num1.count(x)

    num2_map = {}
    for x in num2:
        num2_map[x] = num2.count(x)

    return num1_map == num2_map