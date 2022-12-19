def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day18/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    cubes = set()
    print(len(lines))
    maxx = 0
    maxy = 0
    maxz = 0
    for l in lines:
        c = tuple(map(int, l.split(",")))
        ns = neighbours(c, cubes)
        cubes.add(c)
        cx, cy, cz = c
        maxx = max(maxx, cx)
        maxy = max(maxy, cy)
        maxz = max(maxz, cz)

    maxx += 1
    maxy += 1
    maxz += 1
    s = (-1, -1, -1)
    q = [s]
    visited = set([s])
    res = len(neighbours(s, cubes))
    while q:
        c = q.pop(0)
        res += len(neighbours(c, cubes))
        ns = empty_neighbours(c, cubes, maxx, maxy, maxz)
        for n in ns:
            if n not in visited:
                visited.add(n)
                q.append(n)
    return res


def empty_neighbours(c, cubes, mx, my, mz):
    cas = [ca for ca in candidates(c) if
           -1 <= ca[0] <= mx and
           -1 <= ca[1] <= my and
           -1 <= ca[2] <= mz
           ]
    return [ca for ca in cas if ca not in cubes]


def neighbours(c, cubes):
    return [ca for ca in candidates(c) if ca in cubes]


def candidates(c):
    cx, cy, cz = c
    return [
        (cx + 1, cy, cz),
        (cx - 1, cy, cz),
        (cx, cy + 1, cz),
        (cx, cy - 1, cz),
        (cx, cy, cz + 1),
        (cx, cy, cz - 1),
    ]


if __name__ == "__main__":
    main()
