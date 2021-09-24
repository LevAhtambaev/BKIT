import random


def gen_random(num_count, begin, end):
    data = []
    for i in range(num_count):
        data.append(random.randint(begin, end))
    return data

data = gen_random(7, 1, 3)
#print(data)
