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

# python required.py --test 50
