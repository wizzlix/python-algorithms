def reverse_string(s):
    chars = list(s)

    # Это просто простой алгоритм обращения строки.
    for i in range(len(s)//2):

        # Это просто временная переменная для подкачки.
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp

    return ''.join(chars)