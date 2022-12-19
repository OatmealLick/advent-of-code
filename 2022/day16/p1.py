import math
from collections import defaultdict
from itertools import permutations

# SIZE = 4000000
SIZE = 20
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
    with open(f"2022/day16/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    # 0      1  2 .  3 .  4       5      6    7 8    
    # Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    nodes = defaultdict(list)
    rates = {}
    for l in lines:
        parts = l.split(" ")
        n = parts[1]
        ns = "".join(parts[9:]).split(",")
        r = parts[4].split("=")[1].split(";")[0]
        nodes[n] = ns
        rates[n] = int(r)
    print(nodes, rates)
    non_zero_nodes = [n for n in nodes if rates[n] != 0]
    print(len(non_zero_nodes))
    paths = {}
    pairs = []
    for a in non_zero_nodes + ["AA"]:
        for b in non_zero_nodes + ["AA"]:
            if a != b:
                pairs.append((a, b))

    fill_paths(pairs, nodes, paths)
    print(paths)
    l = (len(permutations(non_zero_nodes)))
    results = []
    for p in permutations(non_zero_nodes):
        # print(f"Perm {p}")
        time = 30
        n = "AA"
        r = 0
        total_pressure = 0
        current_end = 0
        while time > 0 and current_end < len(p):
            # print(f"Time {time}")
            # print(f"Rate {r}")
            # cost_to_travel = path_length(n, p[current_end], nodes, paths)
            cost_to_travel = paths[(n, p[current_end])]
            time -= cost_to_travel
            # print(f"Traveled to {p[current_end]} for {cost_to_travel}")
            time -= 1
            total_pressure += r * (cost_to_travel + 1)
            r += rates[p[current_end]]
            n = p[current_end]
            current_end += 1
        # print(f"Time left {time}")
        if time > 0:
            total_pressure += r * time
        results.append(total_pressure)
    print(results)
    print(max(results))

def fill_paths(path, nodes, paths):
    for s, e in path:
        l = path_length(s, e, nodes, paths)
        paths[(s, e)] = l

def path_length(s, e, nodes, paths):
    if (s, e) in paths:
        return paths[(s, e)]
    q = [(s, 0)]
    visited = set()
    visited.add(s)
    while q:
        n, l = q.pop(0)

        if n == e:
            paths[(s, e)] = l
            return l

        ns = nodes[n]
        for nn in ns:
            if not nn in visited:
                visited.add(nn)
                q.append((nn, l + 1))


if __name__ == "__main__":
    main()
