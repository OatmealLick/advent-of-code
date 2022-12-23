# r1 = "pppw"
# r2 = "sjmn"
r1 = "wvbw"
r2 = "czwc"


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day21/{filename}", "r") as f:
        lines = sorted([x.strip()
                       for x in f.readlines()], key=lambda x: len(x))
        res = solve(lines[:])


def solve(lines):
    vars = {}
    evals = {}

    # write all the evals into dict, numbers into separate dict
    # start from and compute inverse ops: eg. a = humn - b -> humn = a + b
    # add inverse op onto stack
    # follow the thread, next would be a
    # once you reach the top, start taking out from stack and applying
    # you should reach humn = a + b, with known value of a

    # phase 1
    # parse all of the non humn things into num dict, and others into eval dict

    # phase 2
    # follow the trace of humn, one param should be num already
    # add to the list of tuples inverted
    # a = humn - b,
    # d = a * c,
    # f = d / e,
    # h = g / f,
    #
    # {humn: "a - b", a: "d // c", d: "f * e", f: "g / h"}
    # do this until your result is actually computable
    # then you can work your way up

    start_lines = lines[:]
    while start_lines:
        print(start_lines)
        for l in start_lines:
            ps = l.split(": ")
            if ps[1].isdigit():
                if ps[0] != "humn":  # ignore humn
                    vars[ps[0]] = int(ps[1])
                lines.remove(l)
            else:
                if ps[0] == "root":
                    lines.remove(l)
                    continue
                pps = ps[1].split(" ")
                if pps[0] in vars and pps[2] in vars:
                    p1 = f"vars['{pps[0]}']"
                    p2 = f"vars['{pps[2]}']"
                    evaling = f"{p1} {pps[1]} {p2}"
                    # print(evaling)
                    vars[ps[0]] = eval(f"{p1} {pps[1]} {p2}")
                    lines.remove(l)
        if start_lines == lines:
            break
        start_lines = lines[:]

    # build evals
    for l in start_lines:
        p0, p1 = l.split(": ")
        pp0, s, pp1 = p1.split(" ")
        if pp0 in vars:
            pp0v = vars[pp0]
            if s == "+":
                evals[pp1] = (p0, f"(evals['{p0}'][1] - {pp0v})")
                print(1)
            elif s == "-":
                evals[pp1] = (p0, f"({pp0v} - evals['{p0}'][1])")
                print(2)
            elif s == "*":
                evals[pp1] = (p0, f"(evals['{p0}'][1] // {pp0v})")
                print(3)
            elif s == "/":
                evals[pp1] = (p0, f"({pp0v} // evals['{p0}'][1])")
                print(4)
        elif pp1 in vars:
            pp1v = vars[pp1]
            if s == "+":
                evals[pp0] = (p0, f"(evals['{p0}'][1] - {pp1v})")
                print(5)
            elif s == "-":
                evals[pp0] = (p0, f"({pp1v} + evals['{p0}'][1])")
                print(6)
            elif s == "*":
                evals[pp0] = (p0, f"(evals['{p0}'][1] // {pp1v})")
                print(7)
            elif s == "/":
                evals[pp0] = (p0, f"(evals['{p0}'][1] * {pp1v})")
                print(8)
        else:
            raise Exception(f"{pp0, pp1, vars}")
            # todo

    evals[r1] = (r1, vars[r2])
    print(vars)
    print(evals)

    r = resolve("humn", evals)
    print(r)
    print(evals)

    return 0


def resolve(c, evals):
    print(c)
    if c != r1:
        a = resolve(evals[c][0], evals)
        evals[evals[c][0]] = (".", a)
        r = eval(evals[c][1])
        return r
    else:
        return evals[r1][1]


if __name__ == "__main__":
    main()
