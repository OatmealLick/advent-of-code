import math
from collections import defaultdict
from itertools import permutations


def main():
    # filename = "input.txt"
    filename = "input-sample.txt"
    with open(f"2022/day20/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    res = 0
    x = []
    indexes = {}
    for i, l in enumerate(lines):
        indexes[int(l)] = i
        x.append(int(l))
    untouched = x[:]
    print(x)
    offset = 0
    xlen = len(x)
    x = [1, 2, -2, -3, 0, 3, 4]
    print(lupdate(x, -2, -3, xlen))
    # for i, a in enumerate(untouched):
    #     index = (indexes[i] + offset) % xlen
    #     x = update(x, index, a)
    #     offset += a
    #     print(x)
    # print(x)
    return res


def update(x, index, a, xlen):
    if index + a < xlen:
        return x[:index] + x[index+1:index+1+a] + [x[index]] + x[index+1+a:]
    else:
        newindex = (index + a + 1) % xlen
        print(newindex)
        if index < newindex:
            left = x[:index] + x[index + 1:newindex]
            right = x[newindex:]
        else:
            left = x[:newindex]
            right = x[newindex:index] + x[index + 1:]
        print(left, right)
        return left + [x[index]] + right


def lupdate(x, index, a, xlen):
    if index + a >= 0:
        return x[:index+a] + [x[index]] + x[index+a:index] + x[index+1:]
    else:
        newindex = (index + a + 1) % xlen
        print(newindex)
        if index < newindex:
            left = x[:index] + x[index + 1:newindex]
            right = x[newindex:]
        else:
            left = x[:newindex]
            right = x[newindex:index] + x[index + 1:]
        print(left, right)
        return left + [x[index]] + right


if __name__ == "__main__":
    main()
