def memorize(func):
    # # todo Здесь нужно написать код

    cache = {}
    def wrapper(*args):
        if not args in cache:
            cache[args] = func(*args)

        return (cache[args], cache)

    return wrapper


# todo Здесь ничего изменять не нужно!
@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия
    :param weight: масса
    :param speed: скорость
    :return: кинетическую энергию
    """
    return (weight * speed ** 2)/2

#print(get_kinetic_energy(5, 3))
