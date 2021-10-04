from get_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.data = items
        self.ignore_case = False
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        it = iter(self.data)
        while True:
            try:
                current = next(it)
            except StopIteration:
                raise StopIteration
            else:
                if self.ignore_case is True and isinstance(current, str):
                    current = current.lower()
                if current not in self.used_elements:
                    self.used_elements.add(current)
                    return current

    def __iter__(self):
        return self


if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    data3 = ['a', 'b', 'c', 'd', 'c', "A", "B", "C", 'c', 'b', 1, 2, 2, 3, 3, 1, 2, 3, 4]
    data4 = gen_random(10, 1, 3)

    print('first')
    print(list(Unique(data1)))
    print('second')
    print(list(Unique(data2, ignore_case=False)))
    print('third')
    print(list(Unique(data4)))
    print('fourth')
    print(list(Unique(data3, ignore_case=True)))
