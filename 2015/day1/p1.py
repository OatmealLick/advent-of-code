from functools import reduce


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2015/day1/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    line = lines[0]
    res = reduce(lambda a, x: agg(x, a), line, 0)
    return res


def agg(x, a):
    match x:
        case '(':
            return a + 1
        case _:
            return a - 1


if __name__ == "__main__":
    main()
