goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Кресло', 'price': None, 'color': None},
    {'title': None, 'price': 10000, 'color': 'pink'}
]


def field(items, *args):
    assert len(args) > 0, 'Can`t be zero encounters'
    line = []
    if len(args) == 1:
        for x in range(len(items)):
            try:
                if items[x][args[0]] is not None:
                    element = "'" + items[x][args[0]] + "'"
                    line.append(element)
            except KeyError:
                print('KeyError: Key does not exist')
        row = ", ".join(line)
        print(row)
    if len(args) > 1:
        for x in range(len(items)):
            line.clear()
            for y in range(len(args)):
                try:
                    if items[x][args[y]] is not None:
                        pair = "'" + str(args[y]) + "': " + "'" + str(items[x][args[y]]) + "'"
                        line.append(pair)
                except KeyError:
                    print('KeyError: Key does not exist')
            row = ", ".join(line)
            print("{" + row + "}")


field(goods, 'title')
field(goods, 'color')
field(goods, 'title', 'price', 'color')
