def segment(first_point, second_point):
    """Сумма всех координат точек
    :param first_point: координаты первой точки
    :param second_point: координаты второй точки
    :return: текст исключения наоборот или сумму всех координат
    """

    try:
        summa = first_point[0] + first_point[1] + second_point[0] + second_point[1]
        return summa
    except Exception as e:
        return str(e)[::-1]


print(segment(('a', 3), (4, 5)))
