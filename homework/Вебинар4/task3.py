def sum_digits(num):
    """Нахождение суммы цифр числа
    :param num: число
    :return: сумма цифр числа
    """
    # todo Здесь нужно написать код
    list_str = list(str(num))
    list_int = []
    for i in list_str:
        list_int.append(int(i))
    for i in list_int:
        our_sum = sum(list_int)
    return our_sum
