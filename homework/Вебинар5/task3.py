def everything_for_your_cat(cats_data):
    """Котики и их владельцы
    :param cats_data: информация о котах и их владельцах
    :return: информация о котах и их владельцах в виде строки
    """
    new_cats = {}
    for i in cats_data:
        key = i[2]+' '+i[3]
        sep = ''
        if key in new_cats.keys():
            sep = '; '
        new_cats[key] = new_cats.get(key,'') + sep + i[0] + ', ' + str(i[1])
    res = ""
    for j in new_cats.keys():
        res += j + ': ' + new_cats[j] + '\n'
    return res

