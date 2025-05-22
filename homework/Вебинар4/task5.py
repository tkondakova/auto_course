def josephus_task(num_people, kill_num):
    """Задача Иосифа Флавия
    :param num_people: количество воинов
    :param kill_num: номер воина
    :return: номер последнего оставшегося воина
    """
    people_list = list(range(num_people + 1)[1:])
    first_kill = kill_num - 1
    while len(people_list) > 1:
        print(people_list)
        if first_kill >= len(people_list):
            first_kill = first_kill % len(people_list)
        people_list.pop(first_kill)
        first_kill = first_kill + kill_num - 1
    # print(people_list)
    return int(people_list[0])

print(josephus_task(3, 7))
