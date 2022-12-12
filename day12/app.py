import math

MAX_COST = 999


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
    with open(f"day12/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        part1_result = part1(lines[:])
        print(part1_result)
        part2_result = part2_for_google_interview(lines[:])
        print(part2_result)


def part1(lines):
    graph = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            current_pos = Pos(x, y)
            if c == "S":
                start = Pos(x, y)
            elif c == "E":
                end = Pos(x, y)
            graph[current_pos] = neighbors(
                current_pos, elevation(current_pos, lines), lines)

    queue = [start]
    visited = set()
    visited.add(start)
    parents = {}
    while queue:
        current = queue.pop(0)
        if current == end:
            break

        for n in graph[current]:
            if n not in visited:
                parents[n] = current
                queue.append(n)
                visited.add(n)

    current_node = end
    path = []
    paths = {}
    while current_node is not None:
        path.append(current_node)
        current_node = parents.get(current_node)
        paths[current_node] = path[:]

    return len(path) - 1


def part2_for_google_interview(lines):
    costs = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            current_pos = Pos(x, y)
            costs[current_pos] = MAX_COST
            if c == "S":
                start = Pos(x, y)
            elif c == "E":
                end = Pos(x, y)
                costs[current_pos] = 0
    for i in range(1, 100):
        ns = neighbors_of_range(i, end, lines)
        for n in ns:
            nns = neighbors(n, elevation(n, lines), lines)
            neighbor_costs = [costs[nn] for nn in nns]
            if costs[n] >= MAX_COST and neighbor_costs:
                costs[n] = min(neighbor_costs) + 1
        print_costs(lines, costs)
    return "JA PIERDOLE"

def print_costs(lines, costs):
    print()
    for y, line in enumerate(lines):
        l = [f"{y}: "]
        for x, c in enumerate(line):
            l.append('{0: >5}'.format(f"{costs[Pos(x, y)]}"))
        print("".join(l))


def neighbors_of_range(r, center, lines):
    print(f"Range {r}")
    neighbors = []
    for y in range(center.y - r, center.y + r + 1):
        for x in range(center.x - r, center.x + r + 1):
            distance = abs(center.x - x) + abs(center.y - y)
            if math.ceil(distance) < r + 1: 
                neighbors.append(Pos(x, y))
    return [n for n in neighbors if neighbor_in_board(n, lines)]



def neighbors(pos, elev, lines):
    ns = []
    line = lines[0]
    if pos.x > 0:
        ns.append(Pos(pos.x - 1, pos.y))
    if pos.x < len(line) - 1:
        ns.append(Pos(pos.x + 1, pos.y))
    if pos.y > 0:
        ns.append(Pos(pos.x, pos.y - 1))
    if pos.y < len(lines) - 1:
        ns.append(Pos(pos.x, pos.y + 1))
    return [n for n in ns if ord(elev) + 1 >= ord(elevation(n, lines))]


def neighbor_in_board(pos, lines):
    line = lines[0]
    return 0 <= pos.x < len(line) and 0 <= pos.y < len(lines)


def elevation(pos, lines):
    if lines[pos.y][pos.x] == "S":
        return "a"
    if lines[pos.y][pos.x] == "E":
        return "z"
    else:
        return lines[pos.y][pos.x]


def part2_for_lazy_people(lines):
    graph = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            current_pos = Pos(x, y)
            if c == "E":
                start = current_pos
            graph[current_pos] = neighbors_from_top_to_bottom(
                current_pos, elevation(current_pos, lines), lines)

    queue = [start]
    visited = set()
    visited.add(start)
    parents = {}
    while queue:
        current = queue.pop(0)
        if lines[current.y][current.x] == "a":
            break

        for n in graph[current]:
            if n not in visited:
                parents[n] = current
                queue.append(n)
                visited.add(n)

    current_node = current
    path = []
    paths = {}
    while current_node is not None:
        path.append(current_node)
        current_node = parents.get(current_node)
        paths[current_node] = path[:]
    return len(path) - 1


def neighbors_from_top_to_bottom(pos, elev, lines):
    ns = []
    line = lines[0]
    if pos.x > 0:
        ns.append(Pos(pos.x - 1, pos.y))
    if pos.x < len(line) - 1:
        ns.append(Pos(pos.x + 1, pos.y))
    if pos.y > 0:
        ns.append(Pos(pos.x, pos.y - 1))
    if pos.y < len(lines) - 1:
        ns.append(Pos(pos.x, pos.y + 1))
    return [n for n in ns if ord(elev) - 1 <= ord(elevation(n, lines))]

def neighbors_star(pos, lines):
    ns = []
    line = lines[0]
    if pos.x > 0:
        ns.append(Pos(pos.x - 1, pos.y))
    if pos.x < len(line) - 1:
        ns.append(Pos(pos.x + 1, pos.y))
    if pos.y > 0:
        ns.append(Pos(pos.x, pos.y - 1))
    if pos.y < len(lines) - 1:
        ns.append(Pos(pos.x, pos.y + 1))
    return ns


if __name__ == "__main__":
    main()
