from collections import defaultdict


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day23/{filename}", "r") as f:
        lines = [x for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    # parse input into map of elves
    #   elf: (pos, next dir)
    # add helper function for checking whether can move in dir
    # simulate round phase 1:
    # if no other elves in eight, dont do anything
    # otherwise propose dir, create {proposed pos: [elf]} default dict
    # resolve moves
    # update next dir => first dir considered => +1?
    elves = {}
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "#":
                elves[(x, y)] = 0  # fuck this game!
    proposed_pos = defaultdict(list)
    rounds = 10
    printb(elves)
    print(elves)
    di = 0
    for r in range(rounds):
        for p, _ in elves.items():
            if no_elf_around(p, elves):
                continue
            for i in range(4):
                np = plus(p, direction(di + i))
                if see_elf(p, direction(di + i), elves):
                    proposed_pos[np].append(p)
                    break
        print(proposed_pos)
        for np, ps in proposed_pos.items():
            match len(ps):
                case 1:
                    p = ps[0]
                    elves[np] = elves.pop(p)
        di += 1
        proposed_pos.clear()
        print(f"End of round {r + 1}")
        printb(elves)
        print(elves)

    minx = min(map(lambda x: x[0], elves.keys()))
    maxx = max(map(lambda x: x[0], elves.keys()))
    miny = min(map(lambda x: x[1], elves.keys()))
    maxy = max(map(lambda x: x[1], elves.keys()))
    width = maxx - minx + 1
    height = maxy - miny + 1
    return (width * height) - len(elves)


def printb(elves):
    f = -2
    t = 15
    for y in range(f, t):
        l = [f"{str(y).ljust(2)}: "]
        for x in range(f, t):
            if (x, y) in elves:
                l.append("#")
            else:
                l.append(".")
        print("".join(l))


def direction(d):
    return [(0, -1), (0, 1), (-1, 0), (1, 0)][d % 4]


def see_elf(p, d, elves):
    px, py = p
    dx, dy = d
    npx, npy = px + dx, py + dy
    ps = [(npx - 1, npy), (npx, npy), (npx + 1, npy)
          ] if dy != 0 else [(npx, npy - 1), (npx, npy), (npx, npy + 1)]
    return all([not p in elves for p in ps])


def plus(a, b):
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by


def no_elf_around(p, elves):
    offsets = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1)
    ]
    return all(not plus(p, o) in elves for o in offsets)


if __name__ == "__main__":
    main()
