#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";
#import "Math";
#import "Sort";
#import "Hash";

#load "time-cpu.jai";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";

Direction :: enum {
    HORIZONTAL :: 0;
    VERTICAL :: 1;
}

part1 :: () {
    freq := estimate_cpu_frequency(500);

    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n\r\n");
    result := 0;
    
    start := rdtsc();
    for lines {
        res := compute_mirror_result(split(it, "\r\n"));
        result += res;
    }

    // judging whether part2 can be done brute force style
    // judgement: certainly so
    end := rdtsc();
    log("Result %", result);
    log("Time: %", cast(float)(end - start) / cast(float)freq);
}

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n\r\n");
    result := 0;
    
    for lines {
        board := split(it, "\r\n");
        old_res := compute_mirror_result(board);
        res := -1;
        found := false;
        width := board[0].count;
        height := board.count;
        for j: 0..height - 1 for i: 0..width - 1 {
            old_char := board[j][i];
            new_char: u8;
            if old_char == #char "." {
                new_char = #char "#";
            } else  {
                new_char = #char ".";
            }
            board[j][i] = new_char;
            res := compute_mirror_result(board, old_res);
            board[j][i] = old_char;
            if res != -1 && res != old_res {
                result += res;
                found = true;
                break j;
            }
        }
        if !found {
            result += old_res;
        }
    }
    log("Result %", result);
}

compute_mirror_result :: (lines: [] string, old_res: int = -1) -> int {

    line_one := -1;
    line_two := -1;

    other_lines_to_check := 99;
    result := 0;

    // find two lines that are the same
    the_same := true;
    for j: 0..lines.count - 2 {
        the_same = true;
        line_one = j;
        line_two = j + 1;

        for i: 0..lines[0].count - 1 {
            if lines[line_one][i] != lines[line_two][i] {
                the_same = false;
                break;
            }
        }

        if the_same {
            // check surrounding
            from_line := max(0, line_one - other_lines_to_check);
            to_line := min(lines.count - 1, line_two + other_lines_to_check);
            offset := min(line_one - from_line, to_line - line_two);
            if offset == 0 {
                new_res := (line_one + 1) * 100;
                if old_res != -1 { // skipping the old result, looking for a new one
                    if old_res != new_res {
                        return new_res;
                    }
                } else {
                    return new_res;
                }
            }

            is_mirror := true;
            for k: 1..offset for i: 0..lines[0].count - 1 {
                if lines[line_one - k][i] != lines[line_two + k][i] {
                    is_mirror = false;
                    break;
                }
            }
            if is_mirror {
                new_res := (line_one + 1) * 100;
                if old_res != -1 { // skipping the old result, looking for a new one
                    if old_res != new_res {
                        return new_res;
                    }
                } else {
                    return new_res;
                }
            }
        }
    }
    for i: 0..lines[0].count - 2 {
        the_same = true;
        line_one = i;
        line_two = i + 1;

        for j: 0..lines.count - 1 {
            if lines[j][line_one] != lines[j][line_two] {
                the_same = false;
                break;
            }
        }

        if the_same {
            // check surrounding
            from_line := max(0, line_one - other_lines_to_check);
            to_line := min(lines[0].count - 1, line_two + other_lines_to_check);
            offset := min(line_one - from_line, to_line - line_two);
            if offset == 0 {
                new_res := line_one + 1;
                if old_res != -1 { // skipping the old result, looking for a new one
                    if old_res != new_res {
                        return new_res;
                    }
                } else {
                    return new_res;
                }
            }

            is_mirror := true;
            for k: 1..offset for i: 0..lines.count - 1 {
                if lines[i][line_one - k] != lines[i][line_two + k] {
                    is_mirror = false;
                    break;
                }
            }
            if is_mirror {
                new_res := line_one + 1;
                if old_res != -1 { // skipping the old result, looking for a new one
                    if old_res != new_res {
                        return new_res;
                    }
                } else {
                    return new_res;
                }
            }
        }
    }
    return -1;
}

main :: () {
    log("============ Part 1 ============");
    part1();
    log("============ Part 2 ============");
    part2();
}