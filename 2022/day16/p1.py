import math
from collections import defaultdict
from itertools import permutations

TIME = 30

def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day16/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
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
    non_zero_nodes = {n: ns for n, ns in nodes.items() if rates[n] != 0}
    non_zero_nodes_list = list(non_zero_nodes.keys())
    print(len(non_zero_nodes_list))
    paths = {}

    print(non_zero_nodes_list)
    pairs = []
    for a in non_zero_nodes_list + ["AA"]:
        for b in non_zero_nodes_list + ["AA"]:
            if a != b:
                pairs.append((a, b))

    fill_paths(pairs, nodes, paths)

    results = []
    # for p in permutations(non_zero_nodes):
    #     # print(f"Perm {p}")
    #     time = 30
    #     n = "AA"
    #     r = 0
    #     total_pressure = 0
    #     current_end = 0
    #     while time > 0 and current_end < len(p):
    #         # print(f"Time {time}")
    #         # print(f"Rate {r}")
    #         # cost_to_travel = path_length(n, p[current_end], nodes, paths)
    #         cost_to_travel = paths[(n, p[current_end])]
    #         time -= cost_to_travel
    #         # print(f"Traveled to {p[current_end]} for {cost_to_travel}")
    #         time -= 1
    #         total_pressure += r * (cost_to_travel + 1)
    #         r += rates[p[current_end]]
    #         n = p[current_end]
    #         current_end += 1
    #     # print(f"Time left {time}")
    #     if time > 0:
    #         total_pressure += r * time
    #     results.append(total_pressure)
    # print(results)
    # print(max(results))

def go(time_left, current_node, nodes_seen, nodes_left, paths, res):
    if not nodes_left:
        res.append(nodes_seen)
        return res
    
    for n in nodes_left:
        left = nodes_left[:]
        left.remove(n)
        step_length = paths[(current_node, n)]
        if time_left > step_length + 1:
            go(time_left - (step_length + 1), n, [*nodes_seen, n], left, paths, res)
        else:
            res.append(nodes_seen) # leaves duplicates




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
