import argparse


def main():
    """
    type - тип данных, который должен быть в параметре (по умолчанию стоит str)
    например: int, str, list и даже FileType)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=argparse.FileType('r'))
    args = parser.parse_args()

    print(f'данные файла:\n{args.file.read()}')


main()

# винда
# python type2_with_file.py --file txt.txt

# линукс
# python3 type2_with_file.py --file txt.txt
