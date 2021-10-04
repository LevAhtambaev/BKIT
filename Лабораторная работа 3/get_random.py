import random


def gen_random(num_count, begin, end):
    for i in range(num_count):
        i = random.randint(begin, end)
        yield i


data = gen_random(7, 1, 3)

if __name__ == '__main__':
    print(list(data))

