from functools import reduce
from enum import Enum

from collections import defaultdict
from typing import List, Tuple

def main():
    filename = "input.txt"
    #filename = "input-sample.txt"
    with open(f"{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines: List[str]) -> int:
    a, b = reduce(lambda x, agg: (x[0] + agg[0], x[1] + agg[1]), map(convert, lines), (0, 0))
    print(a, b)
    return b - a

def convert(l: str) -> Tuple[int, int]:
    results = []
    i = 0
    while i < len(l):
        c = l[i]
        if c == "\\":
            cn = l[i + 1]
            if cn == "\\" or cn == "\"":
                results.append((2, 4)) # ok
                i += 2
            elif cn == "x":
                results.append((4, 5)) # ok
                i += 4
            else:
                raise Exception(f"received {c} and {cn}")
        elif c == "\"":
            results.append((1, 2)) # ok
            i += 1
        else:
            results.append((1, 1)) # ok
            i += 1
    results.append((0, 2))
    print(results)
    return reduce(lambda x, agg: (x[0] + agg[0], x[1] + agg[1]), results)
    

if __name__ == "__main__":
    main()
