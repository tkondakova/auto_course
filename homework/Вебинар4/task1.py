def which_triangle(a, b, c):
    """Определение типа треугольника
    :param a: длина стороны
    :param b: длина стороны
    :param c: длина стороны
    :return: тип треугольника
    """
    # todo Здесь нужно написать код
    if a == b and b == c:
        type_triangle = "Равносторонний"
    elif a == b or b == c or a == c:
        type_triangle = "Равнобедренный"
    elif a != b and b != c and a != c and a + b > c and b + c > a and a + c > b:
        type_triangle = "Обычный"
    else:
        type_triangle = "Не треугольник"
    return type_triangle

