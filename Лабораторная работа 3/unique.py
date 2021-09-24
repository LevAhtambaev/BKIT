from get_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.used_elements = set()
        self.data = items
        self.index = 0
        self.ignore_case = False
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                if self.ignore_case:
                    current = current.lower()
                self.index = self.index + 1
                if current not in self.used_elements:
                    # Добавление в множество производится
                    # с помощью метода add
                    self.used_elements.add(current)
                    return current

    def __iter__(self):
        return self


data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
# data1 = gen_random(5, 1, 3)

# print(data)
#Unique(data, ignore_case=False)
print('first')
for i in Unique(data):
    print(i)
# вывод 1 2 
print('second')
for i in Unique(data2, ignore_case=False):
    print(i)
# вывод a A b B
print('third')
for i in Unique(data2, ignore_case=True):
    print(i)
# вывод a b 
print('fourth')
print(data1)
for i in Unique(data1):
    print(i)
# data1 = [3, 3, 3, 2, 2]
# вывод 3 2
