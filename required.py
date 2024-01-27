import argparse


def main():
    """
    required нужен для указания обязательности передачи аргумента
    True - обязательно передавать
    False - необязательно передавать
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('--test', required=True, nargs='*')

    args = parser.parse_args()
    print(args)


main()

# винда
# python required.py --test 50

# линукс
# python3 required.py --test 50