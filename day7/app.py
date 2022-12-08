DISK_SIZE = 70000000
UNUSED_SPACE_NEEDED = 30000000
SIZE_LIMIT = 100000


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
    with open(f"day7/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        part1_result = part1(lines[:])
        print(part1_result)
        part2_result = part2(lines[:])
        print(part2_result)


def part1(lines):
    node = parse(lines[1:])
    results = []
    [compute_directories_size_and_add_results(n, results) for n in node.nodes]
    return sum(results)


def compute_directories_size_and_add_results(node, results):
    if node.dir:
        if node.size != 0:
            return node.size
        elif node.nodes:
            sum_of_nodes = [compute_directories_size_and_add_results(
                x, results) for x in node.nodes]
            dir_size = sum(sum_of_nodes)
            node.size = dir_size
            if dir_size <= SIZE_LIMIT:
                results.append(dir_size)
            return dir_size
        else:
            return node.size
    else:
        return node.size


def parse(lines):
    root_node = Node("/", True, 0, [])
    current_node = root_node
    for line in lines:
        if line[:4] == "$ ls":
            continue
        elif line[:4] == "$ cd":
            dir_name = line[5:]
            if dir_name == "..":
                current_node = current_node.parent
            else:
                dir = next(
                    (x for x in current_node.nodes if x.name == dir_name), None)
                current_node = dir
        elif line[:3] == "dir":
            dir_name = line[4:]
            current_node.nodes.append(
                Node(dir_name, True, 0, [], current_node))
        else:
            # file
            file_parts = line.split(" ")
            size = int(file_parts[0])
            current_node.nodes.append(Node(file_parts[1], False, size, None))

    return root_node


def sum_node(node):
    if node.dir:
        if node.size != 0:
            return node.size
        if node.nodes:
            sum_of_nodes = [sum_node(x) for x in node.nodes]
            dir_size = sum(sum_of_nodes)
            node.size = dir_size
            return dir_size
        else:
            return node.size
    else:
        return node.size


def part2(lines):
    node = parse(lines[1:])
    result = sum_node(node)
    space_to_clean = UNUSED_SPACE_NEEDED - (DISK_SIZE - result)
    smallest = []
    res = min(find_smallest(node, space_to_clean, smallest))
    return res


def find_smallest(node, to, smallest):
    if node.dir and node.size > to:
        smallest.append(node.size)
    if node.dir:
        [find_smallest(x, to, smallest) for x in node.nodes]

if __name__ == "__main__":
    main()
