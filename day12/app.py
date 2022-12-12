from collections import defaultdict
import heapq as heap
import math

MAX_COST = 9999

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
    # filename = "input.txt"
    filename = "input-sample.txt"
    with open(f"day12/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        part1_result = part1(lines[:])
        print(part1_result)
        # part2_result = part2(lines[:])
        # print(part2_result)


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

    # path = shortest_path(graph, start, end)
    print(path)
    return len(path) - 1

def part2(lines):
    costs = {}
    graph = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            current_pos = Pos(x, y)
            costs[current_pos] = MAX_COST
            if c == "S":
                start = Pos(x, y)
            elif c == "E":
                end = Pos(x, y)
                costs[current_pos] = 0
            # graph[current_pos] = neighbors(current_pos, elevation(current_pos, lines), lines)
    # neighbors_of_range(0, end)
    # neighbors_of_range(1, end)
    neighbors_of_range(2, end)
    
def neighbors_of_range(r, center):
    neighbors = []
    for y in range(center.y - r, center.y + r + 1):
        for x in range(center.x - r, center.x + r + 1):
            distance = math.sqrt((center.x - x)**2 + (center.y - y)**2)
            print(f"for x {x}, y {y} distance {distance}")

    

def part2_old(lines):
    graph = {}
    starts = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            current_pos = Pos(x, y)
            if c == "S":
                start = current_pos
                starts.append(current_pos)
            elif c == "E":
                end = current_pos

            if c == "a":
                starts.append(current_pos)

            graph[current_pos] = neighbors(
                current_pos, elevation(current_pos, lines), lines)


    paths = {}
    path_lengths = []
    for start in starts:
        path_length = bfs_on_steroids(start, end, graph, paths)
        path_lengths.append(path_length)
        print(f"For start {start} path length {path_length}")
    return min(path_lengths)

def bfs_on_steroids(start, end, graph, paths):
    queue = [start]
    visited = set()
    visited.add(start)
    parents = {}
    while queue:
        current = queue.pop(0)

        print(current) # you need to take the best neighbor not just assume on the first!
        path_from_paths = paths.get(current, 0)
        print(path_from_paths)
        if path_from_paths != 0:
            break

        if current == end:
            break
        for n in graph[current]:
            if n not in visited:
                parents[n] = current
                queue.append(n)
                visited.add(n)

    current_node = current
    path = []
    print(f"parents size {len(parents)}")
    print(paths)
    while current_node != start:
        print("Inside while")
        path.append(current_node)
        current_node = parents.get(current_node)
        if current_node:
            path_from_current_node_to_end = path[:]
            paths[current_node] = len(path_from_current_node_to_end) + path_from_paths
    return paths[start]


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
    return pos.x > 0 and pos.x < len(line) - 1 and pos.y > 0 and pos.y < len(lines) - 1


def elevation(pos, lines):
    if lines[pos.y][pos.x] == "S":
        return "a"
    if lines[pos.y][pos.x] == "E":
        return "z"
    else:
        return lines[pos.y][pos.x]


if __name__ == "__main__":
    main()
