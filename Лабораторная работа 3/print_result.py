def print_result(func_to_decorate):
    def decorated_func():
        print(func_to_decorate.__name__)
        if isinstance(func_to_decorate(), list):
            for i in func_to_decorate():
                print(i)
        elif isinstance(func_to_decorate(), dict):
            for i in func_to_decorate():
                print(i, " = ", func_to_decorate()[i])
        else:
            print(func_to_decorate())
        return func_to_decorate()

    return decorated_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
