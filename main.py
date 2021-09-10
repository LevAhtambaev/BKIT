import sys
import math


def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]  # модуль для работы с командной строкой, считывание параметра по номеру
    except:
        # Вводим с клавиатуры значение
        print(prompt)
        # Переводим строку в действительное число

    while True:
        try:
            coef_str = input()
            coef = float(coef_str)
        except ValueError:
            print('Введите корректный коэффициент - действительное число')
            continue
        if index == 1 and coef == 0.0:
            print("Коэффициент А не может быть нулевым")
        else:
            break

    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root == 0:
            result.append(root)
        if root > 0.0:
            result.append(math.sqrt(root))
            result.append(-math.sqrt(root))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 == 0:
            result.append(root1)
        if root1 > 0.0:
            result.append(math.sqrt(root1))
            result.append(-math.sqrt(root1))
        if root2 == 0:
            result.append(root1)
        if root2 > 0.0:
            result.append(math.sqrt(root2))
            result.append(-math.sqrt(root2))
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))  # формат - для подстановки
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))  # формат - для подстановки
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))  # формат - для подстановки
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))

    input("Press Enter to continue...")


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
