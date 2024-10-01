import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Comprobador de enlaces")
    parser.add_argument("host", help="La direccion a analizar")
    parser.add_argument("input2", help="Argumento 2")
    parser.add_argument("-o1", "--opcional1", help="Argumento opcional 1")
    parser.add_argument("-o2", "--opcional2", help="Argumento opcional 2")
    return parser.parse_args()

args = parse_args()
print(args)
print(args.input1)
print(args.input2)
print(args.opcional1)
print(args.opcional2)

