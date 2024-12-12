#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";
#import "Math";
#import "Sort";
#import "Hash";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";

Direction :: enum {
    NORTH :: 0;
    EAST :: 1;
    SOUTH :: 2;
    WEST :: 3;
}

move_lines :: (lines: [] string, direction: Direction) {
    if direction == {
        case .NORTH;
            for y: 0..lines.count - 1 for x: 0..lines[0].count - 1 {
                if lines[y][x] == #char "O" {
                    for < k: y - 1..0 {
                        if lines[k][x] == #char "." {
                            lines[k][x] = #char "O";
                            lines[k + 1][x] = #char ".";
                        } else {
                            break;
                        }
                    }
                }
            }
        case .SOUTH;
            for < y: lines.count - 2..0 for x: 0..lines[0].count - 1 {
                if lines[y][x] == #char "O" {
                    for k: y + 1..lines.count - 1 {
                        if lines[k][x] == #char "." {
                            lines[k][x] = #char "O";
                            lines[k - 1][x] = #char ".";
                        } else {
                            break;
                        }
                    }
                }
            }
        case .EAST;
            for < x: lines[0].count - 2..0 for y: 0..lines.count - 1 {
                if lines[y][x] == #char "O" {
                    for k: x + 1..lines[0].count - 1 {
                        if lines[y][k] == #char "." {
                            lines[y][k] = #char "O";
                            lines[y][k - 1] = #char ".";
                        } else {
                            break;
                        }
                    }
                }
            }
        case .WEST;
            for x: 1..lines[0].count - 1 for y: 0..lines.count - 1 {
                if lines[y][x] == #char "O" {
                    for < k: x - 1..0 {
                        if lines[y][k] == #char "." {
                            lines[y][k] = #char "O";
                            lines[y][k + 1] = #char ".";
                        } else {
                            break;
                        }
                    }
                }
            }
    }
}

part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");
    move_lines(lines, Direction.NORTH);
    result := 0;
    for y: 0..lines.count-1 for x: 0..lines[0].count-1 {
        if lines[y][x] == #char "O" {
            result += (lines.count - y);
        }
    }
    log("res: %", result);
}

seen_before: [..][] string;
repeated: Table(int, [..] int);

has_seen_before :: (lines: [] string) -> bool, int {
    for seen_before {
        if equal(it, lines) then return true, it_index;
    }
    return false, -1;
}

equal :: (a: [] $T, b: [] T) -> bool {
    if a.count != b.count return false;
    for a {
        if a[it_index] != b[it_index] return false;
    }
    return true;
}

copy :: (a: [] string) -> [] string {
    b := NewArray(a.count, string);
    for a b[it_index] = copy_string(a[it_index]);
    return b;
}

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");
    cycles := 1_000_000_000;

    // after some number of cycles the pattern repeats itself
    // 1. first find the repeating 'start' and the offset (period/cycle) - the number of iterations after which it repeats
    // 2. compute the lowest number of cycles needed to perform
    // 3. run if for the number from 2. instead of 1_000_000_000

    // 1. 
    wait_for_occurrences := 3;
    repeat_start := -1;
    repeat_offset := -1;
    for current_cycles: 0..100_000 - 1 {
        move_lines(lines, Direction.NORTH);
        move_lines(lines, Direction.WEST);
        move_lines(lines, Direction.SOUTH);
        move_lines(lines, Direction.EAST);

        seen, which := has_seen_before(lines);
        if seen {
            repeats_ptr := table_find_pointer(*repeated, which);
            repeats := << repeats_ptr;
            if repeats.count == wait_for_occurrences {
                repeat_start = repeats[1];
                repeat_offset = repeats[2] - repeats[1];
                break;
            } else {
                array_add(repeats_ptr, current_cycles);
            }
        } else {
            lines_copy := copy(lines);
            array_add(*seen_before, lines_copy);
            new_array: [..] int;
            array_add(*new_array, current_cycles);
            table_add(*repeated, current_cycles, new_array);
        }

    }

    // 2.
    after_start_cycles := (cycles - repeat_start) % repeat_offset;
    real_cycles := repeat_start + after_start_cycles;

    // 3.
    for current_cycles: 0..real_cycles - 1 {
        move_lines(lines, Direction.NORTH);
        move_lines(lines, Direction.WEST);
        move_lines(lines, Direction.SOUTH);
        move_lines(lines, Direction.EAST);
    }

    log("\n\n");
    for lines log(it);
    result := 0;
    for y: 0..lines.count-1 for x: 0..lines[0].count-1 {
        if lines[y][x] == #char "O" {
            result += (lines.count - y);
        }
    }
    log("res: %", result);
}


main :: () {
    log("============ Part 1 ============");
    part1();
    log("============ Part 2 ============");
    part2();
}