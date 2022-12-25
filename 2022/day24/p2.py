from collections import defaultdict
from functools import reduce
from copy import deepcopy


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day24/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    maxx = len(lines[0]) - 1
    maxy = len(lines) - 1
    bs = defaultdict(list)
    for y, l in enumerate(lines):
        if y == 0:
            s = (l.find("."), 0)
        elif y == len(lines) - 1:
            e = (l.find(".", len(lines) - 1), maxy)
        else:
            for x, c in enumerate(l):
                if c in [">", "<", "^", "v"]:
                    bs[(x, y)].append(dir(c))

    bss = {}
    bss[0] = bs
    there = journey(s, e, bss, maxx, maxy, 0)
    print(f"Journey there {there}")
    back = journey(e, s, bss, maxx, maxy, there)
    print(f"Journey back {back - there}")
    there_again = journey(s, e, bss, maxx, maxy, back)
    print(f"Journey there again {there_again - back}")
    return there_again


def journey(s, e, bss, maxx, maxy, offset):
    q = [(offset, s)]
    visited = set()
    visited.add((offset, s))
    while q:
        step, c = q.pop(0)

        if c == e:
            return step

        # print(step, c)
        if step + 1 not in bss:
            nbs = move_all_blizzards(bss[step], maxx, maxy)
            bss[step + 1] = nbs
        else:
            nbs = bss[step + 1]

        ns = neighbours(c, maxx, maxy, nbs, e)
        for n in ns:
            nc = (step + 1, n)
            if nc not in visited:
                visited.add(nc)
                q.append(nc)
        if ((step + 1, c) not in visited) and (c not in nbs):
            visited.add((step + 1, c))
            q.append((step + 1, c))


def printb(bs, maxx, maxy, c):
    for y in range(maxy + 1):
        l = []
        for x in range(maxx + 1):
            if y == 0 or y == maxy:
                l.append("#")
            else:
                if (x, y) == c:
                    l.append("E")
                elif (x, y) in bs:
                    if len(bs[x, y]) > 1:
                        l.append(str(len(bs[x, y])))
                    else:
                        l.append("v")
                elif x == 0 or x == maxx:
                    l.append("#")
                else:
                    l.append(".")
        print("".join(l))


def move_all_blizzards(bs, maxx, maxy):
    nbs = deepcopy(bs)
    nbs2 = deepcopy(bs)
    for pos, bss in nbs.items():
        for dir in bss:
            move_blizzard(pos, dir, nbs2, maxx, maxy)
    return nbs2


def move_blizzard(c, dir, bs, maxx, maxy):
    cx, cy = c
    if cx == 1 and dir == (-1, 0):
        nc = (maxx - 1, cy)
    elif cx == maxx - 1 and dir == (1, 0):
        nc = (1, cy)
    elif cy == 1 and dir == (0, -1):
        nc = (cx, maxy - 1)
    elif cy == maxy - 1 and dir == (0, 1):
        nc = (cx, 1)
    else:
        nc = plus(c, dir)
    bs[c].remove(dir)
    if not bs[c]:
        bs.pop(c, None)
    bs[nc].append(dir)


def plus(a, b):
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by


def neighbours(c, maxx, maxy, bs, e):
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cs = map(lambda x: plus(c, x), offsets)
    return reduce(lambda acc, x: acc + [x] if ((x == e) or (x not in bs and within_walls(x, maxx, maxy))) else acc, cs, [])


def within_walls(c, maxx, maxy):
    return 0 < c[0] < maxx and 0 < c[1] < maxy


def dir(c):
    match c:
        case "<":
            return (-1, 0)
        case ">":
            return (1, 0)
        case "^":
            return (0, -1)
        case "v":
            return (0, 1)


if __name__ == "__main__":
    main()

# 231 too low