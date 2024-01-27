import sys


def print_help(msg=""):
    """функция печатает правила использования и ошибку, если она есть"""

    print(f"Usage: {sys.argv[0]} [-h] [--base BASE] int [int ...]\n{msg}")
    quit()


def main(args):
    print(args, 'all_args')
    integers = []
    base = 2  # по умолчанию

    while args:
        arg = args.pop(0)
        if arg == '-h':  # вывод подсказки
            print_help()

        elif arg == '--base':  # изменить систему счисления
            try:
                base = int(args.pop(0))
            except ValueError:
                print_help(f"invalid base value: {arg}")

        else:  # добавляем в список числа
            integers.append(arg)

    if not integers:  # список пустой
        print_help('No int args')

    try:
        return list(map(lambda x: int(x, base), integers))  # преобразования
    except ValueError as e:
        print_help(f"invalid value: {e}")


print(main(sys.argv[1:]))

# python repeat.py --base 3 0 1 10 11

# python repeat.py --base 3 140 1 1010

# python repeat.py