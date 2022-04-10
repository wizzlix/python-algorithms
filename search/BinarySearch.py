def binary_search(a, what):
    
    # Это просто переменные, которые нужны для бинарного поиска.
    left = 0
    right = len(a) - 1
    index = None

    try:
        # Алгоритм бинарного поиска.
        while (left <= right) and (index is None):
            
            mid = (right + left) // 2

            if a[mid] == what:
                index = mid

            else: 
                if what < a[mid]:
                    right = mid - 1
                else: 
                    left =  mid + 1

        # Это просто проверка, найдено значение или нет.
        if index is not None:
            return index
        else: 
            return "Not found :c"

    # Он ловит исключение и печатает его.
    except Exception as ex:
        print(ex)