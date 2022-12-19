import math
from collections import defaultdict
from itertools import permutations

def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day18/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    cubes = set()
    result = 0
    for l in lines:
        c = tuple(map(int, l.split(",")))
        ns = neighbours(c, cubes)
        print(f"c {c}, result: {result}, ns {ns}")
        result += 6 + (-2 * len(ns))
        cubes.add(c)
    return result


def neighbours(c, cubes):
    cx, cy, cz = c
    candidates = [
        (cx + 1, cy, cz),
        (cx - 1, cy, cz),
        (cx, cy + 1, cz),
        (cx, cy - 1, cz),
        (cx, cy, cz + 1),
        (cx, cy, cz - 1),
    ]
    return [ca for ca in candidates if ca in cubes]


if __name__ == "__main__":
    main()
