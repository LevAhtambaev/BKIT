import time
from contextlib import contextmanager


class cm_timer1:

    def __init__(self):
        self.startTime = time.time()

    def __enter__(self):
        self.startTime = time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print("time: {}".format(time.time() - self.startTime))


@contextmanager
def cm_timer2():
    startTime = time.time()
    yield
    print("time: {}".format(time.time() - startTime))


if __name__ == '__main__':
    with cm_timer1():
        time.sleep(2)
    with cm_timer2():
        time.sleep(2)
