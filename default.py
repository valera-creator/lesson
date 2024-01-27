import argparse


def main():
    """
    default - значение по умолчанию, если параметр не передали
    Тип данных должен соответствовать типу данных в default
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg1', nargs="*", default=100, type=int)
    args = parser.parse_args()

    print(args)


main()
# python default.py
# python default.py --arg1 1 2 3
