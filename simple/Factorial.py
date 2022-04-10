def factorial(n:int):
    """
    Вычисляет факториал числа.
    
    :param n: Число у которого ищим факториал
    :return: Факториал n
    """
    if n < 2: return 1
    return n * factorial(n-1)