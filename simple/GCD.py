def gcd(a:int,b:int):
    """
    Вычисляет наибольший общий делитель чисел a и b.
    
    :param a: первое число
    :param b: второе число
    :return: Наибольший общий делитель чисел a и b.
    """

    while a != 0 and b != 0:
        if a > b:
            a = a%b
        else:
            b = b%a

    return a+b 