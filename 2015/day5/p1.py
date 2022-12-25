from functools import reduce
from collections import defaultdict


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2015/day5/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(line):
    pass

if __name__ == "__main__":
    main()
