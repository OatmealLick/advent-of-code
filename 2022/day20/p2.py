import math
from collections import defaultdict
from itertools import permutations
from copy import deepcopy, copy


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day20/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    x = {}
    key = 811589153
    # key = 1
    lines = [int(l) * key for l in lines]
    for i, l in enumerate(lines):
        x[i] = (i, int(l))
    print("Initial")
    printd(x)
    for j in range(10):
    # for j in range(1):
        for i, l in enumerate(lines):
            x = move(x, i, int(l))
            # print(f"After move x {i} {int(l)}")
        printd(x)
        print(j)

    offset = [k for k, v in x.items() if v[1] == 0][0]
    print(offset)
    a = x[(offset + 1000) % len(x)][1]
    b = x[(offset + 2000) % len(x)][1]
    c = x[(offset + 3000) % len(x)][1]
    print(a, b, c)
    return a + b + c


def printd(x):
    ks = sorted(x.keys())
    l = ["{"]
    for k in ks:
        l.append(f"{k}:{x[k]}, ")
    l.append("}")
    print("".join(l))
    print([x[k][1] for k in ks])
    print()


def getvalues(x):
    ks = sorted(x.keys())
    return [x[k] for k in ks]


def move(x, i, a):
    ind = [k for k, v in x.items() if v == (i, a)][0]
    while a != 0:
        if a > len(x) - 1:
            a = a % (len(x) - 1)
        elif a < -(len(x) - 1):
            a = a % (len(x) - 1)
        if a > 0:
            x, ind = move_right(x, ind)
            a -= 1
        else:
            x, ind = move_left(x, ind)
            a += 1
    return x


def move_right(x, ind):
    if (ind + 1) < (len(x) - 1):
        x[ind], x[ind + 1] = x[ind + 1], x[ind]
        return x, ind + 1
    elif ind == len(x) - 1:
        i, a = x.pop(ind)
        firsti, firsta = x.pop(0)
        tomove = {(k + 1): v for k, v in x.items()}
        tomove.update({0: (firsti, firsta), 1: (i, a)})
        return tomove, 1
    else:
        i, a = x.pop(ind)
        tomove = {((k + 1) if (k < ind) else k): v for k, v in x.items()}
        tomove.update({0: (i, a)})
        return tomove, 0


def move_left(x, ind):
    if (ind - 1) > 0:
        x[ind], x[ind - 1] = x[ind - 1], x[ind]
        return x, ind - 1
    elif ind == 0:
        xlen = len(x)
        i, a = x.pop(ind)
        lasti, lasta = x.pop(xlen - 1)
        tomove = {(k - 1): v for k, v in x.items()}
        tomove.update({(xlen - 2): (lasti, lasta), (xlen - 1): (i, a)})
        return tomove, xlen - 1
    else:
        i, a = x.pop(ind)
        tomove = {((k - 1) if (k > ind) else k): v for k, v in x.items()}
        tomove.update({len(x): (i, a)})
        return tomove, len(x)


# def update(x, index, a, xlen):
#     if index + a < xlen:
#         return x[:index] + x[index+1:index+1+a] + [x[index]] + x[index+1+a:]
#     else:
#         newindex = (index + a + 1) % xlen
#         print(newindex)
#         if index < newindex:
#             left = x[:index] + x[index + 1:newindex]
#             right = x[newindex:]
#         else:
#             left = x[:newindex]
#             right = x[newindex:index] + x[index + 1:]
#         print(left, right)
#         return left + [x[index]] + right

if __name__ == "__main__":
    main()
