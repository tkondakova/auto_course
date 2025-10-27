def three_most_expensive_purchases():
    """Три самые дорогие покупки
    :return: сумму трех самых дорогих покупок
    """
    file_path = "test_file/task_2.txt"
    # todo Здесь нужно написать код
    with open(file_path, mode='r', encoding='utf-8') as f:
        price = 0
        prices = []
        for l in f.readlines():
            print(l)
            if l == '\n' and price != 0:
                prices.append(price)
                price = 0
            else:
                price += int(l)

        prices.sort(reverse=True)
        top_tree = prices[:3]
        print(top_tree)

        most_expensive_purchases = sum(top_tree)
        return most_expensive_purchases

print(three_most_expensive_purchases())
