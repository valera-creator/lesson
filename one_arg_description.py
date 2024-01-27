import argparse

parser = argparse.ArgumentParser()
parser.add_argument('one_arg')
args = parser.parse_args()

print(args)

# python one_arg_1.py 1
