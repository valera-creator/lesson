import argparse


def main():
    """
    action - то, как стоит обработать аргумент
    наиболее часто используемые:

    store - значение по умолчанию, без передачи будет None
    store_true - если не передали ничего, то False (флаг)
    store_false - если не передали ничего, то True (флаг)
    store_const - установить значение константу, если передали аргумент
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('--check', action='store_false')

    args = parser.parse_args()
    print(args)


main()
# python action.py
# python action.py --check 10
