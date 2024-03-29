import argparse


def main():
    """
    description - необязательный параметр для пояснения скрипта
    параметр help в аргументах нужен для пояснения работы с параметрами
    чтобы узнать о скрипте информацию, можно использовать -h или --help
    """

    parser = argparse.ArgumentParser(description='Описание скрипта: обучение пользоваться description и help')

    parser.add_argument('one', nargs=1, help='one принимает 1 аргумент')
    parser.add_argument('-n', '--name', nargs=2, help='name принимает 2 аргумента')

    args = parser.parse_args()


main()

# винда
# python help.py -h

# линукс
# python3 help.py -h
