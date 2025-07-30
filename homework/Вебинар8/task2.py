class Trigon:
    def __init__(self, *args):
        # todo Здесь нужно написать код
        if len(args) != 3:
            raise IndexError(f'Передано {len(args)} аргументов, а ожидается 3')
        for side in args:
            if not isinstance(side, (int, float)):
                raise TypeError('Стороны должны быть числами')
        for side in args:
            if side <= 0:
                raise ValueError('Стороны должны быть положительными')
        a, b, c = args
        if not (a + b > c and a + c > b and b + c > a):
            raise Exception('Не треугольник')
        self.sides = args
