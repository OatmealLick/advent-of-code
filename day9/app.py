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
    # filename = "input-sample2.txt"
    with open(f"day9/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        # part1_result = part1(lines[:])
        # print(part1_result)
        part2_result = part2(lines[:])
        print(part2_result)


def part1(lines):
    position_set = set()
    h = Pos(0, 0)
    t = Pos(0, 0)
    position_set.add(t)
    for l in lines:
        print(f"Step {l}")
        parts = l.split(" ")
        if parts[0] == "R":
            dir = Pos(1, 0)
        elif parts[0] == "L":
            dir = Pos(-1, 0)
        elif parts[0] == "U":
            dir = Pos(0, 1)
        else:
            dir = Pos(0, -1)
        steps = int(parts[1])

        for s in range(steps):
            h = Pos(h.x + dir.x, h.y + dir.y)
            print(f"Updating h to {h}")
            if not is_touching(h, t):
                # update t
                print(f"Updating t to {t}")
                t = Pos(h.x - dir.x, h.y - dir.y)
                position_set.add(t)
    print(position_set)
    return len(position_set)

def is_touching(h, t):
    x = abs(t.x - h.x)
    y = abs(t.y - h.y)
    return x <= 1 and y <= 1 

def distance_abs(h, t):
    x = abs(t.x - h.x)
    y = abs(t.y - h.y)
    return x + y 


def part2(lines):
    position_set = set()
    nodes = [Pos(0, 0)] * 10
    position_set.add(Pos(0,0))
    for l_i, l in enumerate(lines):
        print(f"Step {l}")
        parts = l.split(" ")
        if parts[0] == "R":
            dir = Pos(1, 0)
        elif parts[0] == "L":
            dir = Pos(-1, 0)
        elif parts[0] == "U":
            dir = Pos(0, 1)
        else:
            dir = Pos(0, -1)
        steps = int(parts[1])

        for s in range(steps):
            h = nodes[0]
            # h_copy = Pos(h.x, h.y)
            h = Pos(h.x + dir.x, h.y + dir.y)
            # print(f"Updating h to {h}")
            nodes[0] = h
            for n in range(1, len(nodes)):
                h = nodes[n-1]
                t = nodes[n]
                if not is_touching(h, t):
                    if n == 6:
                        print(f"h {h}, t {t}")
                    if distance_abs(h, t) == 4:  # diagonal move
                        t = Pos((h.x + t.x) // 2, (h.y + t.y) // 2)
                    elif distance_abs(h, t) == 3:  # diagonal move
                        if abs(h.x - t.x) == 2:
                            delta = 1 if h.x > t.x else -1
                            t = Pos(h.x - delta, h.y)
                        else:
                            delta = 1 if h.y > t.y else -1
                            t = Pos(h.x, h.y - delta)
                    elif distance_abs(h, t) == 2 and (abs(h.x - t.x) == 2 or abs(h.y - t.y) == 2):  # diagonal move
                        if abs(h.x - t.x) == 2:
                            delta = 1 if h.x > t.x else -1
                            t = Pos(h.x - delta, h.y)
                        else:
                            delta = 1 if h.y > t.y else -1
                            t = Pos(h.x, h.y - delta)
                    else:
                        # t_copy = Pos(t.x, t.y)
                        # t = h_copy
                        t = Pos(h.x - dir.x, h.y - dir.y)
                    # print(f"Updating t{n} to {t}")
                    nodes[n] = t
                    # h_copy = t_copy
                    if n == 9:
                        position_set.add(t)
            # if 0 < l_i < 6:
                # print_board(nodes)
    # print(position_set)
    # print_been_there(position_set)
    return len(position_set)

def print_board(nodes):
    lines = []
    for y in range(20):
        line = ["."] * 50
        if y == 10:
            line[25] = "s"
        for i, n in enumerate(nodes):
            if n.y == y - 10:
                line[25 + n.x] = str(i)

        lines.append(line + [f"{19 - y}"])
    
    lines.reverse()
    print("".join([str(n)[-1] for n in range(-25, 25)]))
    for line in lines:
        print("".join(line))
    print("")


def print_been_there(poss):
    for y in range(20):
        line = ["."] * 50
        for n in poss:
            if n.y == y - 10:
                line[25 + n.x] = "*"
        print("".join(line) + f" {y}")


if __name__ == "__main__":
    main()
