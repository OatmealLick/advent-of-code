def main():
    filename = "input.txt"
    with open(f"day10/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        part1_result = part1(lines[:])
        print(part1_result)
        part2_result = part2(lines[:])
        print(part2_result)


def part1(lines):
    cycle = 1
    count_cycles = [20, 60, 100, 140, 180, 220]
    signal = 0
    register = 1
    for line in lines:
        if line[:4] == "noop":
            if cycle in count_cycles:
                signal += cycle * register
                count_cycles = count_cycles[1:]
            cycle += 1
        else:  # addx 4
            parts = line.split(" ")
            value = int(parts[1])
            if cycle in count_cycles:
                signal += cycle * register
                count_cycles = count_cycles[1:]
            if cycle + 1 in count_cycles:
                signal += (cycle + 1) * register
                count_cycles = count_cycles[1:]
            cycle += 2
            register += value
    return signal


def part2(lines):
    cycle = 1
    register = 1
    crt = []
    WIDTH = 40
    HEIGHT = 6
    for line in lines:
        if line[:4] == "noop":
            handle_crt(cycle, register, crt)
            cycle += 1
        else:  # addx 4
            parts = line.split(" ")
            value = int(parts[1])
            handle_crt(cycle, register, crt)
            cycle+=1
            handle_crt(cycle, register, crt)
            cycle+=1
            register += value
    for i in range(HEIGHT):
        print("".join(crt[i*WIDTH:(i+1)*WIDTH]))
    return 0

def sprite_pos(middle):
    return [middle - 1, middle, middle + 1]

def handle_crt(cycle, register, crt):
    if (cycle - 1) % 40 in sprite_pos(register):
        crt.append("#")
    else:
        crt.append(".")


if __name__ == "__main__":
    main()
