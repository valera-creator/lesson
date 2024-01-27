import argparse


def main():
    """
    именованные параметры передаются через - или --
    -n - сокращенное
    --name - полное
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('one', nargs="*")
    parser.add_argument('-n', '--name', nargs='*')

    args = parser.parse_args()
    print(args)


main()
# python names.py 1 --name x y z
