import math
from collections import defaultdict
from itertools import permutations

WIDTH = 150
HEIGHT = 200
# WIDTH = 16
# HEIGHT = 12


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day22/{filename}", "r") as f:
        lines = [x[:-1] for x in f.readlines()]
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

    print(f"Starting pos {p} and rot {rot}")
    for c in commands:
        if c.isdigit():
            for _ in range(int(c)):
                p = next_step(p, rot, b)
        else:
            rot = rotate(rot, c)
        print(f"After {c}, has pos {p} and rot {rot}")


    print(rot, p)
    row, col = p[1] + 1, p[0] + 1
    print(row, col)
    res = 1000 * row + 4 * col + score_for_rot(rot)

    # parse the input, into 2d l 200x100: have -1 for nothing, 0 for road, 1 wall, add helper func for type
    # parse the input line into chars or ints
    # find the start point
    # add wrap around function next_step/next_move to hide the logic of wrap around
    # iterate with current position
    # call next steps / moves until the end
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


def next_step(p, rot, b):
    nx, ny = p[0] + rot[0], p[1] + rot[1]
    outside = ny >= len(b) or nx >= len(b[ny])
    if not outside:
        ncell = b[ny][nx]
    if outside or ncell == -1:
        if rot == (1, 0):
            road_index = b[ny].index(0)
            wall_index = b[ny].index(1)
            if wall_index < road_index:
                return p  # can
            else:
                return (road_index, ny)
        elif rot == (-1, 0):
            road_index = b[ny][::-1].index(0)
            wall_index = b[ny][::-1].index(1)
            lll = len(b[ny]) - 1
            road_index = lll - road_index
            wall_index = lll - wall_index
            if wall_index > road_index:
                return p  # can
            else:
                return (road_index, ny)
        elif rot == (0, 1):  # DOWN
            bb = [b[y][nx] for y in range(HEIGHT)]
            road_index = bb.index(0)
            wall_index = bb.index(1)
            if wall_index < road_index:
                return p  # can
            else:
                return (nx, road_index)
        elif rot == (0, -1):  # UP
            bb = [b[y][nx] for y in range(HEIGHT)]
            road_index = bb[::-1].index(0)
            wall_index = bb[::-1].index(1)
            lll = len(bb) - 1
            road_index = lll - road_index
            wall_index = lll - wall_index
            if wall_index > road_index:
                return p  # can
            else:
                return (nx, road_index)
        else:
            raise Exception("B")
    elif ncell == 0:
        return (nx, ny)
    elif ncell == 1:
        return p  # can improve by returning additional info, wall will block you
    else:
        raise Exception("A")


if __name__ == "__main__":
    main()
