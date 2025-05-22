def multiplication_chain(num):
    """Цепочка умножений
    :param num: положительное число
    :return: количество перемножений
    """
    # todo Здесь нужно написать код
    list_str = list(str(num))
    dlinna = len(list_str)
    count_multy = 0
    while dlinna > 1:
        list_int = []
        our_mul = 1
        for i in list_str:
            list_int.append(int(i))
        for i in list_int:
            our_mul = our_mul * i
        list_str = list(str(our_mul))
        dlinna = len(list(str(our_mul)))
        count_multy = count_multy + 1
    else:
        print(count_multy)
    return count_multy
