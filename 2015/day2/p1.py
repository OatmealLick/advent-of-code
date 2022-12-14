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
    [x, y, z] = list(map(int, l.split("x")))
    a = x * y
    b = y * z
    c = z * x
    res = 2*(a+b+c) + min(a, b, c)
    return res


if __name__ == "__main__":
    main()
