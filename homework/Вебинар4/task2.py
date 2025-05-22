def flatten_and_sort(array):
    """Преобразование двумерного массива в плоский список
    :param array: двумерный массив
    :return: плоский список
    """
    # todo Здесь нужно написать код
    new_array = []
    for a in array:
        for b in a:
            new_array.append(b)
    result_list = sorted(new_array)
    return result_list
