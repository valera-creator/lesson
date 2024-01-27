import argparse


def main():
    """
    store_const устанавливает значение в аргумент, которое находится в const
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_const', const='какая-то константа')

    args = parser.parse_args()
    print(args)


main()
# python const.py
# python const.py --check
