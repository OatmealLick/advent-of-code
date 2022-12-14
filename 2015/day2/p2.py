from functools import reduce


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2015/day2/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    return sum(map(f, lines))


def f(l):
    [x, y, z] = list(sorted(map(int, l.split("x"))))
    return x+x+y+y+(x*y*z)


if __name__ == "__main__":
    main()
