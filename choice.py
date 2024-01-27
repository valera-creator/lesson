import argparse


def main():
    """
    choices нужен, чтобы можно было вводить значение только из указанного в choices
    type должен соответствовать типу данных в choices (при choices=['1'] и type=int будет ошибка
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('arg_choice', choices=[1, 2, 3, 4, 5], type=int)
    args = parser.parse_args()

    print(f'вы мне должны {args.arg_choice}k рублей')


main()

# винда
# python choice.py 1
# python choice.py 5

# линукс
# python3 choice.py 1
# python3 choice.py 5