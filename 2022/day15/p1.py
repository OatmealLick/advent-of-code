import math
from collections import defaultdict

LINE = 2000000
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
        part1_result = part1(lines[:])
        print(part1_result)
        part2_result = part2(lines[:])
        print(part2_result)


def part1(lines):
    os = []
    for l in lines:
        parts = l.split(" ")
        sensor_x = int(parts[2][:-1].split("=")[1])
        sensor_y = int(parts[3][:-1].split("=")[1])
        beacon_x = int(parts[8][:-1].split("=")[1])
        beacon_y = int(parts[9].split("=")[1])
        os.append((Pos(sensor_x, sensor_y), Pos(beacon_x, beacon_y)))

    blocked = defaultdict(list)
    for p in os:
        neighbourhood(p, blocked)

    for p in os:
        b = p[1]
        if b.y in blocked and b in blocked[b.y]:
            blocked[b.y].remove(b)
    return len(set(blocked[LINE]))

def neighbourhood(p, blocked):
    s = p[0]
    b = p[1]
    d = pdistance(p)
    width = -1
    print(f"Neighbourhood of {p}")
    for y in range(s.y - d, s.y + d + 1):
        if y > s.y:
            width -= 1
        else:
            width += 1
        if y != LINE:
            continue
        for x in range(s.x - width, s.x + width + 1):
            blocked[y].append(Pos(x, y))



def pdistance(p):
    return distance(p[0], p[1])


def distance(s, b):
    return abs(s.x - b.x) + abs(s.y - b.y)


def part2(lines):
    pass


if __name__ == "__main__":
    main()
