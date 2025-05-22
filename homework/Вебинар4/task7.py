def move_zeros(lst):
    """Перемещение нулей
    :param lst: список из цифр
    :return: список из цифр с нулями в конце
    """
    # todo Здесь нужно написать код
    if 0 in lst:
        for i in lst:
            zero = lst.count(0)
        while 0 in lst:
            lst.remove(0)
        lst2 = [0] * zero
        lst.extend(lst2)
    else:
        lst = lst
    return lst
