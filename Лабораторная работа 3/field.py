def field(items, *args):
    assert len(args) > 0, 'Can`t be zero encounters'
    if len(args) == 1:
        for dictionary in items:
            note = dictionary.get(args[0])
            if note is not None:
                yield note
    else:
        for d in items:
            dictionary = dict()
            for key in args:
                note = d.get(key)
                if note is not None:
                    dictionary[key] = note
            if len(dictionary) != 0:
                yield dictionary


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': 'Кресло', 'price': None, 'color': None},
        {'title': None, 'price': 10000, 'color': 'pink'}
    ]
    data1 = list()
    data2 = list()

    for i in field(goods, 'title'):
        data1.append(i)
    print(str(data1))
    print()

    for i in field(goods, 'title', 'price'):
        data2.append(i)
    print(data2)
