import argparse

parser = argparse.ArgumentParser()
parser.add_argument('one_arg')
args = parser.parse_args()

print(args.one_arg)  # обращение к аргументу one_arg

# винда
# python one_arg_1.py блаблаблабла

# линукс
# python3 one_arg_1.py блаблаблабла