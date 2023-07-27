from functools import reduce
from enum import Enum

from collections import defaultdict

class Command(Enum):
    TURN_OFF = 0
    TURN_ON = 1
    TOGGLE = 2


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    # turn on 887,9 through 959,629
    commands = map(parse, lines)
    #print(list(commands)[0:20])
    lights = defaultdict(int)
    print("aloha")
    for c in commands:
        command, sx, sy, ex, ey = c
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                match command:
                    case Command.TURN_ON:
                        lights[(x, y)] += 1
                    case Command.TURN_OFF:
                        lights[(x, y)] = max(0, lights[(x, y)] - 1)
                    case _:
                        lights[(x, y)] += 2
    return reduce(lambda agg, x: agg + x[1], lights.items(), 0)


def parse(line):
    parts = line.split(" ")
    if len(parts) == 4:
        parts.insert(0, "")
    match parts[1]:
        case "on":
            command = Command.TURN_ON
        case "off":
            command = Command.TURN_OFF
        case _:
            command = Command.TOGGLE
    s_parts = parts[2].split(",")
    e_parts = parts[4].split(",")
    sx, sy = int(s_parts[0]), int(s_parts[1])
    ex, ey = int(e_parts[0]), int(e_parts[1])
    return command, sx, sy, ex, ey


if __name__ == "__main__":
    main()
