def treatment_sum(our_tuple):
    """Обработка суммы элементов кортежа
    :param our_tuple: кортеж
    :return: сумму элементов кортежа
    """

    if (len(our_tuple)) == 2:
        try:
            summa = our_tuple[0] + our_tuple[1]
            return summa
        except TypeError:
            return 'Нельзя сложить эти данные'
    if (len(our_tuple)) < 2:
        try:
            summa = our_tuple[0] + our_tuple[1]
        except IndexError:
            return 'Недостаточно данных'
    if (len(our_tuple)) > 2:
        raise Exception('Много данных')
