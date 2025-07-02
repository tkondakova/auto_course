def letter_stat(our_str):
    """Буквенная статистика
    :param our_str: строка
    :return: словарь со статистикой по буквам
    """
    letters_dict = {}
    for i in our_str:
        if i in letters_dict:
            letters_dict[i] += 1
        else:
            letters_dict[i] = 1
    return letters_dict

