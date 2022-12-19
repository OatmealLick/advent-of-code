import math
from collections import defaultdict

SIZE = 4000000
# SIZE = 20
F = 4000000
# LINE = 10


class Pos:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __hash__(self) -> int:
        return self.x + 31 * self.y


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day15/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    os = []
    for l in lines:
        parts = l.split(" ")
        sensor_x = int(parts[2][:-1].split("=")[1])
        sensor_y = int(parts[3][:-1].split("=")[1])
        beacon_x = int(parts[8][:-1].split("=")[1])
        beacon_y = int(parts[9].split("=")[1])
        os.append((Pos(sensor_x, sensor_y), Pos(beacon_x, beacon_y)))

    pos_x_bs = set()
    neg_x_bs = set()
    # os = [(Pos(7, 9), Pos(11, 7))]
    # os = [(Pos(14, 10), Pos(15, 10))]
    for s, b in os:
        print(f"For s {s} b {b}")
        new_pos = set()
        new_neg = set()

        if b.x >= s.x and b.y <= s.y or b.x <= s.x and b.y >= s.y:
            b_prim = prim_xy(b, s)
            print(f"EEE {b.y - b.x}")
            new_pos.update([b.x - b.y, b_prim.x - b_prim.y])
            pos_x_bs.update(new_pos)

            b_prim_y = prim_y(b, s)
            b_prim_x = prim_x(b, s)
            new_neg.update([-b_prim_y.y - b_prim_y.x, -b_prim_x.y - b_prim_x.x])
            neg_x_bs.update(new_neg)
            print(f"IF Adding pos {new_pos}, neg {new_neg}")
        else:
            b_prim = prim_xy(b, s)
            new_neg.update([-b.y - b.x, -b_prim.y - b_prim.x])
            neg_x_bs.update(new_neg)

            b_prim_y = prim_y(b, s)
            b_prim_x = prim_x(b, s)
            new_pos.update([b_prim_y.x - b_prim_y.y, b_prim_x.x - b_prim_x.y])
            pos_x_bs.update(new_pos)
            print(f"ELSE Adding pos {new_pos}, neg {new_neg}")
        print(f"Adding pos {new_pos}, neg {new_neg}")
        print_that(b, s, new_pos, new_neg)
    pos_x_bs = sorted(list(pos_x_bs))
    neg_x_bs = sorted(list(neg_x_bs))
    print(pos_x_bs)
    print(neg_x_bs)
    pos_pairs = [(pos_x_bs[i], pos_x_bs[i+1])
                 for i in range(len(pos_x_bs) - 1) if pos_x_bs[i+1] - pos_x_bs[i] == 2]
    neg_pairs = [(neg_x_bs[i], neg_x_bs[i+1])
                 for i in range(len(neg_x_bs) - 1) if neg_x_bs[i+1] - neg_x_bs[i] == 2]
    print(pos_pairs)
    print(neg_pairs)
    # 14,10 --- y = x - 4 ==> 5, 3 in pos
    # 14,10 --- y = -x - (-24) ==> -23, -25 in neg
    for p in pos_pairs:
        for n in neg_pairs:
            a = sum(p) // 2
            b = sum(n) // 2
            print(f"a {a}, b {b}")
            y = (-a -b) // 2
            print(y)
            x = - b - y
            if -SIZE <= x <= SIZE and -SIZE <= y <= SIZE:
                print(x, y)
                res = F * x + y
                print(res)
    return 0


def print_that(b, s, pos, neg):
    # size = 21
    size_x = 30
    size_y = 20
    print("".join([str(x).ljust(3) for x in range(-1, size_x)]))
    for y in range(0, size_y):
        l = [f"{y}:".ljust(4)]
        for x in range(0, size_x):
            c = Pos(x, y)
            if b == c:
                l.append("B  ")
            elif s == c:
                l.append("S  ")
            else:
                isp = False
                isn = False
                for p in pos:
                    if Pos(x, x - p) == c:
                        isp = True
                for n in neg:
                    if Pos(x, -x - n) == c:
                        isn = True
                if isp:
                    l.append("P  ")
                elif isn:
                    l.append("N  ")
                else:
                    l.append(".  ")
        print("".join(l))


def prim_xy(b, s):
    pos_bs = Pos(b.x - s.x, b.y - s.y)
    return Pos(-pos_bs.x + s.x, -pos_bs.y + s.y)


def prim_y(b, s):
    pos_bs = Pos(b.x - s.x, b.y - s.y)
    return Pos(-pos_bs.x + s.x, pos_bs.y + s.y)


def prim_x(b, s):
    pos_bs = Pos(b.x - s.x, b.y - s.y)
    return Pos(pos_bs.x + s.x, -pos_bs.y + s.y)

def neighbourhood(p, blocked):
    s = p[0]
    b = p[1]
    d = pdistance(p)
    width = -1
    print(f"Neighbourhood of {p}")
    for y in range(s.y - d, s.y + d + 1):
        if not (0 <= y <= SIZE):
            continue
        if y > s.y:
            width -= 1
        else:
            width += 1
        for x in range(s.x - width, s.x + width + 1):
            if not (0 <= x <= SIZE):
                continue
            blocked[y].add(Pos(x, y))


def pdistance(p):
    return distance(p[0], p[1])


def distance(s, b):
    return abs(s.x - b.x) + abs(s.y - b.y)


def part2(lines):
    pass


if __name__ == "__main__":
    main()
