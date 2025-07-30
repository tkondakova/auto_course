import math


class Segment:

    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def length(self):
        """Вычисление длины отрезка"""
        return round(math.sqrt((self.first_point[0] - self.second_point[0])**2 + \
                         (self.first_point[1] - self.second_point[1]) ** 2), 2)

    def x_axis_intersection(self):
        """Пересечение оси абсцисс"""
        if self.first_point[1] * self.second_point[1] <= 0:
            return True
        else:
            return False


    def y_axis_intersection(self):
        """Пересечение оси ординат"""
        if self.first_point[0] * self.second_point[0] <= 0:
            return True
        else:
            return False
