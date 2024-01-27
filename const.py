import argparse


def main():
    """
    store_const устанавливает значение в аргумент, которое находится в const, по умолчанию None
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_const', const='какая-то константа')

    args = parser.parse_args()
    print(args)


main()

# винда
# python const.py
# python const.py --check

# линукс
# python3 const.py
# python3 const.py --check