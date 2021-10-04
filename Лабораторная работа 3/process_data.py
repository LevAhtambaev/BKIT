import json
import sys
from print_result import print_result
from cm_timer import cm_timer1
from unique import Unique
from field import field
from get_random import gen_random

# Сделаем другие необходимые импорты

path = r'C:\Users\hoppl\PycharmProjects\LAB3\json_file.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding='utf-8') as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, 'job-name'), ignore_case=True)), key=str.lower)


@print_result
def f2(arg):
    return list(filter(lambda string: str.startswith(str.lower(string), 'программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda s: s + " с опытом python", arg))


@print_result
def f4(arg):
    return dict(zip(arg, list('зарплата {} руб.'.format(val) for val in gen_random(len(arg), 1000000, 2000000))))


if __name__ == '__main__':
    with cm_timer1():
        f4(f3(f2(f1(data))))
