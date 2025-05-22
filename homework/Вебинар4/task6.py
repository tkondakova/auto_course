def create_phone_number(num_tuple):
    """Создание номера телефона
    :param num_tuple: кортеж из цифр
    :return: строку в виде номера телефона
    """
    # todo Здесь нужно написать код
    str_list = [str(i) for i in num_tuple]
    return "({}) {}-{}".format(''.join(str_list[:3]), ''.join(str_list[3:6]), ''.join(str_list[6:]))
