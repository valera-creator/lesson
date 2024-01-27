import argparse


def main():
    """
    dest переименовывает название аргумента на более удобное
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('--AllaMikhailovna', dest='Alla', type=int)
    parser.add_argument('--ArtemKorotkov', dest='Artem', type=int)

    args = parser.parse_args()
    print(args)


main()

# винда
# python dest.py --AllaMikhailovna 100 --ArtemKorotkov 100

# линукс
# python3 dest.py --AllaMikhailovna 100 --ArtemKorotkov 100
