import argparse

parser = argparse.ArgumentParser()
parser.add_argument('one_arg')
args = parser.parse_args()

print(f'инфа: {args.one_arg}')  # обращение к параметру one_arg

# python one_arg_1.py 1
