def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    b = {}
    new_str = ''
    for i in our_str:
        b[i] = b.get(i, 0) + 1
        new_str += i + '_' + str(b[i])
    return new_str

