import math
from collections import defaultdict
from itertools import permutations

sample = True
sample = False

WIDTH = 16 if sample else 150
HEIGHT = 12 if sample else 200
SIZE = 4 if sample else 50
wasthere = set()


def test(b):
    cases = [
        # pos1 rot , pos2 rot
        ((SIZE + 24, 3*SIZE - 1), (0, 1),
         (SIZE - 1, 3*SIZE + 24), (-1, 0)),  # from 4 to 6
        ((SIZE - 1, 3*SIZE + 24), (1, 0),
         (SIZE + 24, 3*SIZE - 1), (0, -1)),  # from 6 to 4

        ((SIZE, SIZE + 26), (-1, 0), (26, 2*SIZE), (0, 1)),  # from 3 to 5
        ((24, 2*SIZE), (0, -1), (SIZE, SIZE + 24), (1, 0)),  # from 5 to 3

        ((SIZE + 24, 0), (0, -1), (0, 3*SIZE + 24), (1, 0)),  # from 1 to 6
        ((0, 3*SIZE + 24), (-1, 0), (SIZE + 24, 0), (0, 1)),  # from 6 to 1

        ((2*SIZE + 24, SIZE - 1), (0, 1),
         (2*SIZE - 1, SIZE + 24), (-1, 0)),  # from 2 to 3
        ((2*SIZE - 1, SIZE + 24), (1, 0),
         (2*SIZE + 24, SIZE - 1), (0, -1)),  # from 3 to 2

        ((3*SIZE - 1, 24), (1, 0), (2*SIZE - 1, 2 * \
         SIZE + SIZE - 1 - 24), (-1, 0)),  # from 2 to 4
        ((2*SIZE - 1, 2*SIZE + SIZE - 1 - 24), (1, 0),
         (3*SIZE - 1, 24), (-1, 0)),  # from 4 to 2

        ((2*SIZE + 24, 0), (0, -1), (24, 4*SIZE - 1), (0, -1)),  # from 2 to 6
        ((24, 4*SIZE - 1), (0, 1), (2*SIZE + 24, 0), (0, 1)),  # from 6 to 2

        ((SIZE, 0), (-1, 0), (0, 2*SIZE + SIZE - 1), (1, 0)),  # from 1 to 5
        ((0, 2*SIZE + SIZE - 1), (-1, 0), (SIZE, 0), (1, 0)),  # from 5 to 1
    ]

    res = list(map(lambda c: next_step(c[0], c[1], b), cases))
    [print(a) for a in zip(res, tuple((c[2], c[3]) for c in cases))]
    results = [next_step(c[0], c[1], b) == (c[2], c[3]) for c in cases]
    assert all(results)


def main():
    filename = "input-sample.txt" if sample else "input.txt"
    with open(f"2022/day22/{filename}", "r") as f:
        lines = [x.replace("\n", "") for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    b = [[-1] * WIDTH for _ in range(HEIGHT)]
    for y, l in enumerate(lines[:-2]):
        for x, c in enumerate(l):
            if c == "#":
                b[y][x] = 1
            elif c == ".":
                b[y][x] = 0
    # your higher indexes are at the bottom, remember
    # -1 for nothing, 0 for road, 1 for wall
    commands = parse_commands(lines[-1])
    s = (b[0].index(0), 0)
    rot = (1, 0)
    p = s
    wasthere.add(p)

    # test(b)
    # exit(0)

    print(commands )
    print(f"Starting pos {p} and rot {rot}")
    for i, c in enumerate(commands):
        # if i > 119:
        # break
        print(f"Before {c}, has pos {p} and rot {rot}")
        if c.isdigit():
            for _ in range(int(c)):
                p, rot = next_step(p, rot, b)
                print(p, rot)
                wasthere.add(p)
        else:
            rot = rotate(rot, c)
        print(f"After {c}, has pos {p} and rot {rot}")

    printb(b, wasthere)
    print(p, rot)
    row, col = p[1] + 1, p[0] + 1
    print(row, col)
    res = 1000 * row + 4 * col + score_for_rot(rot)
    print(len(commands))
    return res


def score_for_rot(rot):
    match rot:
        case (1, 0):
            return 0
        case (0, 1):
            return 1
        case (-1, 0):
            return 2
        case _:
            return 3


def parse_commands(l):
    l = l.replace("R", " R ")
    l = l.replace("L", " L ")
    return l.strip().split(" ")


def rotate(rot, dir):
    if dir == "R":
        rots = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    else:
        rots = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    nc = (rots.index(rot) + 1) % len(rots)
    return rots[nc]


def sector(p):
    x, y = p
    if sample:
        if 2*SIZE <= x < 3*SIZE and y < SIZE:
            return 1
        elif x < SIZE and SIZE <= y < 2*SIZE:
            return 2
        elif SIZE <= x < 2*SIZE and SIZE <= y < 2*SIZE:
            return 3
        elif 2*SIZE <= x < 3*SIZE and SIZE <= y < 2*SIZE:
            return 4
        elif 2*SIZE <= x < 3*SIZE and 2*SIZE <= y < 3*SIZE:
            return 5
        elif 3*SIZE <= x < 4*SIZE and 2*SIZE <= y < 3*SIZE:
            return 6
        else:
            raise Exception("C SAMPLE")
    else:
        if SIZE <= x < 2*SIZE and y < SIZE:
            return 1
        elif 2*SIZE <= x < 3*SIZE and y < SIZE:
            return 2
        elif SIZE <= x < 2*SIZE and SIZE <= y < 2*SIZE:
            return 3
        elif SIZE <= x < 2*SIZE and 2*SIZE <= y < 3*SIZE:
            return 4
        elif x < SIZE and 2*SIZE <= y < 3*SIZE:
            return 5
        elif x < SIZE and 3*SIZE <= y < 4*SIZE:
            return 6
        else:
            raise Exception("C")


def sample_sector_offsets(s):
    match s:
        case 1:
            return (2, 0)
        case 2:
            return (0, 1)
        case 3:
            return (1, 1)
        case 4:
            return (2, 1)
        case 5:
            return (2, 2)
        case 6:
            return (3, 2)

def sector_offsets_sized(s):
    if sample:
        return tuple(a * SIZE for a in sample_sector_offsets(s))
    else:
        return tuple(a * SIZE for a in sector_offsets(s))

def sector_offsets(s):
    match s:
        case 1:
            return (1, 0)
        case 2:
            return (2, 0)
        case 3:
            return (1, 1)
        case 4:
            return (1, 2)
        case 5:
            return (0, 2)
        case 6:
            return (0, 3)
        case _:
            raise Exception("D")


def complementary_sector(s, rot):
    if sample:
        match s, rot:
            case 4, (1, 0):
                return 6, (0, 1)
            case 6, (0, -1):
                return 4, (-1, 0)
            case 5, (-1, 0):
                return 3, (0, 1)
            case 3, (0, 1):
                return 5, (1, 0)
            case 2, (0, -1):
                return 1, (0, 1)
            case 1, (0, -1):
                return 2, (0, 1)
            case 2, (0, 1):
                return 5, (0, -1)
            case 5, (0, 1):
                return 2, (0, -1)
            case 1, (1, 0):
                return 6, (-1, 0)
            case 6, (1, 0):
                return 1, (-1, 0)
            case 6, (0, 1):
                return 2, (0, 1)
            case 2, (0, -1):
                return 6, (0, -1)
            case 1, (-1, 0):
                return 3, (0, 1)
            case 3, (0, -1):
                return 1, (1, 0)
            case _, _:
                raise Exception(f"ASD SAMPLE {s}, {rot}")
    else:
        match s, rot:
            case 4, (0, 1):
                return 6, (-1, 0)
            case 6, (1, 0):
                return 4, (0, -1)
            case 5, (0, -1):
                return 3, (1, 0)
            case 3, (-1, 0):
                return 5, (0, 1)
            case 2, (0, 1):
                return 3, (-1, 0)
            case 3, (1, 0):
                return 2, (0, -1)
            case 2, (1, 0):
                return 4, (-1, 0)
            case 4, (1, 0):
                return 2, (-1, 0)
            case 1, (-1, 0):
                return 5, (1, 0)
            case 5, (-1, 0):
                return 1, (1, 0)
            case 6, (0, 1):
                return 2, (0, 1)
            case 2, (0, -1):
                return 6, (0, -1)
            case 1, (0, -1):
                return 6, (1, 0)
            case 6, (-1, 0):
                return 1, (0, 1)
            case _, _:
                raise Exception("ASD")


def printb(b, wasthere):
    for y, l in enumerate(b):
        line = []
        for x, c in enumerate(l):
            if (x, y) in wasthere:
                line.append("^")
            else:
                match c:
                    case -1:
                        line.append(" ")
                    case 0:
                        line.append(".")
                    case 1:
                        line.append("#")
        print("".join(line))


def minus(a: tuple, b: tuple):
    ax, ay = a
    bx, by = b
    return ax - bx, ay - by


def plus(a: tuple, b: tuple):
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by


def mirror_top_bottom():
    if sample:
        return [(1, 2), (2, 1), (2, 5), (5, 2)]
    else:
        return []


def mirror_left_right():
    if sample:
        return [(1, 6), (6, 1)]
    else:
        return [(2, 4), (4, 2), (1, 5), (5, 1), (6, 2), (2, 6)]

def mirror_and_swap():
    if sample:
        return [(4, 6), (6, 4), (3, 5), (5, 3), (2, 6), (6, 2)]
    else:
        return []


def next_step(p, rot, b):
    nx, ny = p[0] + rot[0], p[1] + rot[1]
    outside = ny >= len(b) or nx >= len(b[ny])
    if not outside:
        ncell = b[ny][nx]
    if outside or ncell == -1:
        s = sector(p)
        sos = sector_offsets_sized(s)
        ns, nrot = complementary_sector(s, rot)
        nsos = sector_offsets_sized(ns)
        nx, ny = minus(p, sos)
        transition = (s, ns)
        if transition in mirror_top_bottom():
            nnx = (SIZE - 1) - nx
            nny = ny
        elif transition in mirror_left_right():
            nnx = nx
            nny = (SIZE - 1) - ny
        elif transition in mirror_and_swap():
            nnx, nny = ny, nx
            nnx = (SIZE - 1) - nnx
            nny = (SIZE - 1) - nny
        else:  # swap pairs
            nnx, nny = ny, nx
        nnnx, nnny = plus(nsos, (nnx, nny))
        if b[nnny][nnnx] == 0:
            return (nnnx, nnny), nrot
        elif b[nnny][nnnx] == 1:
            return p, rot
        else:
            raise Exception("EE")
    elif ncell == 0:
        return (nx, ny), rot
    elif ncell == 1:
        return p, rot  # can improve by returning additional info, wall will block you
    else:
        raise Exception("A")


if __name__ == "__main__":
    main()