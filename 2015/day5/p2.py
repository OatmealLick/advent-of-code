from functools import reduce

from collections import defaultdict


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2015/day5/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    return reduce(lambda agg, x: agg + (1 if is_nice(x) else 0), lines, 0)

def is_nice(s):
    return has_weird_triple(s) and has_double_of_double_letter(s)

def has_weird_triple(s):
    for i in range(len(s) - 2):
        start = s[i]
        end = s[i + 2]
        if start == end:
            return True
    return False

def has_double_of_double_letter(s):
    for i in range(len(s) - 1):
        pi = s[i:i+2]
        for j in range(min(i + 2, len(s) - 1), len(s) - 1):
            pj = s[j:j+2]
            if pi == pj:
                return True
    return False

if __name__ == "__main__":
    main()
