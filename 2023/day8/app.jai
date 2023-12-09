#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";
#import "Math";
#import "Sort";
#import "Hash";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";

Directions :: struct {
    left: string;
    right: string;
}

Link :: struct {
    from: string;
    instruction: int;
}

End :: struct {
    node: string;
    steps: int;
}

compare_function :: (a: Link, b: Link) -> bool {
    return a.from == b.from && a.instruction == b.instruction;
}

hash_function :: (a: Link) -> u32 {
    return get_hash(a.from) + cast(u32)(31 * a.instruction);
}

part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    directions: Table(string, Directions);
    nodes: [..] string;
    links: Table(Link, int, given_compare_function=compare_function, given_hash_function=hash_function);

    lines := split(file_contents, "\r\n");
    list := trim(lines[0]);
    for i: 2..lines.count - 1 {
        parts := split(trim(lines[i]), " = ");
        left: string = ---;
        left.count = 3;
        left.data = parts[1].data + 1;
        right: string = ---;
        right.count = 3;
        right.data = parts[1].data + 6;
        table_set(*directions, parts[0], .{left, right});
        if ends_with(parts[0], "A") array_add(*nodes, parts[0]);
    }

    ends_per_node: Table(string, [..] End);
    for i: 0..nodes.count - 1 {
        steps := 0;
        instruction := -1;
        node := copy_string(nodes[i]);
        node_ends: [..] End;
        while true {
            steps += 1;
            instruction = (instruction + 1) % list.count;
            current := nodes[i];
            direction, ok := table_find(*directions, current);
            next := ifx list[instruction] == #char "R" then direction.right else direction.left;
            
            if ends_with(next, "Z") {
                for node_ends if it.node == next continue;

                log("For node % found % (%)", node, next, steps);
                array_add(*node_ends, .{copy_string(next), steps});
                if node_ends.count >= 6 {
                    table_set(*ends_per_node, node, node_ends);
                    break;
                }
            }
            
            nodes[i] = next;
        }
        log("In total for node % has %", node, node_ends);
    }

    result := 1;
    for v, k: ends_per_node {
        result = result * v[0].steps;
    }
    log("% ", result);
    // lcd of the firsts: 8811050362409
}


part2 :: () {
}

print_array :: (header: string, a: [] $T) {
    print("%: ", header);
    for a {
        print("% ", it);
    }
    print("\n");
}

main :: () {
    log("============ Part 1 ============");
    part1();
    log("============ Part 2 ============");
    part2();
}