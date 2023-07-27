from enum import Enum

from collections import defaultdict
from typing import List

class Op(Enum):
    ASSIGNMENT = 0
    TURN_ON = 1
    TOGGLE = 2


def main():
    filename = "input.txt"
    filename_upper = filename.upper()
    print(filename_upper)
    with open(f"{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines: List[str]) -> int:
    vars = defaultdict(int)
    while lines:
        to_remove = []
        for i, l in enumerate(lines):
            parts = l.split(" ")
            lp = len(parts)
            if lp == 3:
                start = parts[0]
                end = parts[-1]
                truestart = vars_or_digit(start, vars)
                if truestart is None:
                    continue
                vars[end] = truestart
                to_remove.append(i)
            elif lp == 4 and parts[0] == "NOT":
                start = parts[1]
                end = parts[-1]
                if start in vars:
                    vars[end] = ~vars[start]
                    if vars[end] == 0:
                        print(f"start {vars[start]} end {end}")
                    to_remove.append(i)
                else:
                    continue
            elif lp == 5 and parts[1] == "AND":
                l = parts[0]
                r = parts[2]
                end = parts[-1]
                truel = vars_or_digit(l, vars)
                truer = vars_or_digit(r, vars)
                if truel is None or truer is None:
                    continue
                vars[end] = truel & truer
                if vars[end] == 0:
                    print(f"l {truel} r {truer} end {end}")
                to_remove.append(i)
            elif lp == 5 and parts[1] == "OR":
                l = parts[0]
                r = parts[2]
                end = parts[-1]
                truel = vars_or_digit(l, vars)
                truer = vars_or_digit(r, vars)
                if truel is None or truer is None:
                    continue
                vars[end] = truel | truer
                to_remove.append(i)
            elif lp == 5 and parts[1] == "LSHIFT":
                l = parts[0]
                r = parts[2]
                end = parts[-1]
                if l in vars:
                    vars[end] = vars[l] << int(r)
                    to_remove.append(i)
                else:
                    continue
            elif lp == 5 and parts[1] == "RSHIFT":
                l = parts[0]
                r = parts[2]
                end = parts[-1]
                if l in vars:
                    vars[end] = vars[l] >> int(r)
                    to_remove.append(i)
                else:
                    continue
        print(to_remove)
        len_lines = len(lines)
        for i in range(len_lines - 1, -1, -1):
            if i in to_remove:
                lines.pop(i)
        to_remove = []
    #     counter += 1
    #     if counter >= 7:
    #         break
    print(vars)
    return vars['a']


def vars_or_digit(x, vars):
    if x.isdigit():
        return int(x)
    elif x in vars:
        return vars[x]
    else:
        return None


if __name__ == "__main__":
    main()
