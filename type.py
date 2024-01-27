import argparse


def main():
    """
    type - тип данных, который должен быть в параметре (по умолчанию стоит str)
    например: int, str, list и даже FileType)
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--num', type=int)
    parser.add_argument('--file', type=argparse.FileType('r'))

    args = parser.parse_args()
    print(args)
    print(f'число: {args.num}')

    print(f'данные файла:\n{args.file.read()}')


main()
# python type.py --num 1 --file txt.txt
