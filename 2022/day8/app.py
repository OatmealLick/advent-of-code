class Node:
    def __init__(self, name, dir, size, nodes, parent=None) -> None:
        self.name = name
        self.dir = dir
        self.size = size
        self.nodes = nodes
        self.parent = parent

    def __str__(self) -> str:
        return f"({self.name}, {self.dir}, {self.size}, {self.nodes})"

    def __repr__(self) -> str:
        return str(self)


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"day8/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        part1_result = part1(lines[:])
        print(part1_result)
        part2_result = part2(lines[:])
        print(part2_result)


def part1(lines):
    result = 0
    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if x == 0 or y == 0 or x == max_x or y == max_y:
                result += 1
            else:
                current = int(lines[y][x])
                left = [int(t) < current for t in lines[y][:x]]
                right = [int(t) < current for t in lines[y][x+1:]]
                column = []
                for i in range(max_y + 1):
                    column.append(lines[i][x])
                top = [int(t) < current for t in column[:y]]
                bot = [int(t) < current for t in column[y+1:]]
                res = any([all(left), all(right), all(top), all(bot)])
                if res:
                    result += 1
    return result

def part2(lines):
    result = 0
    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1
    current_max = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            current = int(lines[y][x])
            left_score = score(reversed(lines[y][:x]), current)
            right_score = score(lines[y][x+1:], current)
            # right = [int(t) for t in lines[y][x+1:]]
            column = []
            for i in range(max_y + 1):
                column.append(lines[i][x])
            # top = [int(t) for t in column[:y]]
            # bot = [int(t) for t in column[y+1:]]
            top = column[:y]
            top = reversed(top)
            top_score = score(top, current)
            bot_score = score(column[y+1:], current)
            scenic_score = left_score * right_score * top_score * bot_score
            if scenic_score > current_max:
                print(current)
                print(top)
                print(scenic_score)
                print(y, x)
                print(left_score, right_score, top_score, bot_score)
            current_max = max(current_max, scenic_score)
    return current_max

def score(left, current):
    left_score = 0
    for t in left:
        t_int = int(t)
        if t_int < current:
            left_score += 1
        else:
            left_score += 1
            break
    return left_score



if __name__ == "__main__":
    main()
