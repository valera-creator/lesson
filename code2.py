import argparse

parser = argparse.ArgumentParser(description="convert integers to decimal system")

parser.add_argument('integers', metavar='integers', nargs='+', type=str, help='integers to be converted')
parser.add_argument('--base', default=2, type=int, help='default numeric system')

args = parser.parse_args()

s = " ".join(map(lambda x: str(int(x, args.base)), args.integers))

print(f'result: {s}')

# винда
# python code2.py 1 2 111 211 --base 3

# линукс
# python3 code2.py 1 2 111 211 --base 3
