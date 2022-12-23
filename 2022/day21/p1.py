import math
from collections import defaultdict
from itertools import permutations


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day21/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))

def solve(lines):
    counter = 0
    vars = {}
    while lines:
        print(f"setting counter to {(counter + 1) % len(lines)}")
        counter = (counter + 1) % len(lines)
        l = lines[counter]
        ps = l.split(": ")
        if ps[1].isdigit():
            vars[ps[0]] = int(ps[1])
            lines.remove(l)
            print(f"Added {ps[1]}")
            continue
        else:
            pps = ps[1].split(" ")
            if pps[0] in vars and pps[2] in vars:
                p1 = f"vars['{pps[0]}']"
                p2 = f"vars['{pps[2]}']"
                evaling = f"{p1} {pps[1]} {p2}"
                print(evaling)
                vars[ps[0]] = eval(f"{p1} {pps[1]} {p2}")
                lines.remove(l)
                continue
    return vars["root"]


if __name__ == "__main__":
    main()
