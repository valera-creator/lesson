import argparse


def main():
    """
    metavar позволяет изменить названия аргумента при использовании help
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('sahar', nargs=1, help='sahar принимает 1 аргумент', metavar='metavarское название')
    args = parser.parse_args()


main()

# винда
# python metavar.py -h

# линукс
# python3 metavar.py -h