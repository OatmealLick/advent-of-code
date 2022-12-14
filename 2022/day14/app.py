import math


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
    with open(f"2022/day14/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        part1_result = part1(lines[:])
        print(part1_result)
        part2_result = part2(lines[:])
        print(part2_result)


def part1(lines):
    rocks = set()
    for l in lines:
        coords = l.split(" -> ")
        for i, c in enumerate(coords):
            if i + 1 <= len(coords) - 1:
                ax, ay = [int(x) for x in c.split(",")]
                bx, by = [int(x) for x in coords[i+1].split(",")]
                rocks.add(Pos(ax, ay))
                while ax != bx or ay != by:
                    if ax < bx:
                        ax += 1
                    elif ax > bx:
                        ax -= 1
                    if ay < by:
                        ay += 1
                    elif ay > by:
                        ay -= 1
                    rocks.add(Pos(ax, ay))
    counter = 0
    while True:
        if handle_sand(rocks):
            counter += 1
        else:
            return counter

def handle_sand(rocks):
    sand = Pos(500, 0)
    max_steps = 1000
    for _ in range(max_steps):
        next_sand = Pos(sand.x, sand.y + 1)
        if next_sand not in rocks:
            sand = next_sand
        else:
            left_sand = Pos(sand.x - 1, sand.y + 1)
            if left_sand not in rocks:
                sand = left_sand
            else:
                right_sand = Pos(sand.x + 1, sand.y + 1)
                if right_sand not in rocks:
                    sand = right_sand
                else:
                    rocks.add(sand)
                    return True
    return False


def part2(lines):
    rocks = set()
    for l in lines:
        coords = l.split(" -> ")
        for i, c in enumerate(coords):
            if i + 1 <= len(coords) - 1:
                ax, ay = [int(x) for x in c.split(",")]
                bx, by = [int(x) for x in coords[i+1].split(",")]
                rocks.add(Pos(ax, ay))
                while ax != bx or ay != by:
                    if ax < bx:
                        ax += 1
                    elif ax > bx:
                        ax -= 1
                    if ay < by:
                        ay += 1
                    elif ay > by:
                        ay -= 1
                    rocks.add(Pos(ax, ay))
    floor = max(rocks, key=lambda x: x.y).y + 2
    for i in range(300, 700):
        rocks.add(Pos(i, floor))
    counter = 0
    while True:
        if handle_sand2(rocks):
            counter += 1
        else:
            return counter

def handle_sand2(rocks):
    sand = Pos(500, 0)
    max_steps = 10000
    for _ in range(max_steps):
        next_sand = Pos(sand.x, sand.y + 1)
        if next_sand not in rocks:
            sand = next_sand
        else:
            left_sand = Pos(sand.x - 1, sand.y + 1)
            if left_sand not in rocks:
                sand = left_sand
            else:
                right_sand = Pos(sand.x + 1, sand.y + 1)
                if right_sand not in rocks:
                    sand = right_sand
                else:
                    if sand == Pos(500, 0):
                        return False
                    else:
                        rocks.add(sand)
                        return True
    raise Exception("cry")




if __name__ == "__main__":
    main()
