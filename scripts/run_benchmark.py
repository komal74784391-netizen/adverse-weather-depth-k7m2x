import argparse

from src.benchmark.datasets import list_split
from src.benchmark.metrics import abs_rel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-root', required=True)
    parser.add_argument('--split', default='rain')
    args = parser.parse_args()
    samples = list_split(args.data_root, args.split)
    print(len(samples), 'samples in', args.split)


if __name__ == '__main__':
    main()
