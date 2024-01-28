import argparse


def main():
    """
    type - тип данных, который должен быть в параметре (по умолчанию стоит str)
    например: int, str, list и даже FileType)
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--num', type=int)

    args = parser.parse_args()
    print(args)
    print(f'число: {args.num}')


main()

# винда
# python type.py --num 1

# линукс
# python3 type.py --num 1
