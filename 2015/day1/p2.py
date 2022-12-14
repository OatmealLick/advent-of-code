from functools import reduce


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2015/day1/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    line = lines[0]
    res = map(lambda x: (x[0] + 1, 1) if x[1] == '(' else (x[0] + 1, -1), enumerate(line))
    res = reduce(lambda a, x: a + [(x[0], (a[-1][1] if a else 0) + x[1])], res, [])
    res = filter(lambda x: x[1] == -1, res)
    res = list(res)
    return res[0]


if __name__ == "__main__":
    main()
