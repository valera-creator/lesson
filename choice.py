import argparse


def main():
    """
    choices нужен, чтобы можно было вводить значение только из указанного в choices
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('arg_choice', choices=(range(1, 101)), type=int)
    args = parser.parse_args()

    print(f'вы мне должны {args.arg_choice}k рублей')


main()

# python choice.py 1
# python choice.py 0
