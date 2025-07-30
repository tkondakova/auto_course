class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed

    @property
    def info(self):
        """Информация о транспорте"""
        print(f"Марка: {self.brand}\n"
              f"Цвет: {self.color}\n"
              f"Год выпуска: {self.year}\n"             
              f"Мощность двигателя: {self.engine_power} л.с."
              )
        return

class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.passengers = passengers
        self.__park = park
        self._fare = fare

    @property
    def park(self):
        return self.__park

    @park.setter
    def park(self, new_park):
        if not (1000 <= new_park <= 9999):
            raise AssertionError("Номер парка должен быть в диапазоне от 1000 до 9999")
        self.__park = new_park


class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.__route = route
        self.path = path
        self._fare = fare

    @property
    def route(self):
        return self.__route

    @route.setter
    def route(self, new_route):
        self.__route = new_route

    @property
    def how_long(self):
        return self.max_speed/(4*self.path)
