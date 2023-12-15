#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";
#import "Math";
#import "Sort";
#import "Hash";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";
//FILENAME :: "sample2.txt";



part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");
    log("Before");
    for lines log(it);
    expanded := expand(lines);
    log("After");
    for expanded log(it);
    galaxies: [..] Pos;
    for j: 0..expanded.count - 1 for i: 0..expanded[0].count - 1 {
        if expanded[j][i] != #char "." {
            array_add(*galaxies, .{i, j});
        }
    }
    lowest_path := 0;
    pairs := 0;
    for j: 0..galaxies.count - 1 {
        for i: j+1..galaxies.count - 1 {
            pairs += 1;
            a:= galaxies[j];
            b:= galaxies[i];
            horizontal := abs(b.x - a.x);
            vertical := abs(b.y - a.y);
            lowest_path += horizontal + vertical;
        }
    }

    log("result: %", lowest_path);
    log("pairs: %", pairs);
}

Pos :: struct {
    x: int;
    y: int;
}

expand :: (lines: [] string) -> [] string {
    rows_to_expand: [..] int;
    cols_to_expand: [..] int;
    for j: 0..lines.count - 1 {
        row_empty := true;
        for i: 0..lines[0].count - 1 {
            if lines[j][i] != #char "." {
                row_empty = false;
                break;
            }
        }
        if row_empty array_add(*rows_to_expand, j);
    }
    for i: 0..lines[0].count - 1 {
        col_empty := true;
        for j: 0..lines.count - 1 {
            if lines[j][i] != #char "." {
                col_empty = false;
                break;
            }
        }
        if col_empty array_add(*cols_to_expand, i);
    }

    expanded: [..] string;

    new_width := lines[0].count + cols_to_expand.count;
    for j: 0..lines.count - 1 {
        if array_find(rows_to_expand, j) {
            new_line: string = ---;
            new_line.count = new_width;
            new_line_data := NewArray(new_width, u8);
            for i: 0..new_width - 1 {
                new_line_data[i] = #char ".";
            }
            new_line.data = new_line_data.data;
            array_add(*expanded, new_line);
            array_add(*expanded, new_line);
        } else {
            new_line: string = ---;
            new_line.count = new_width;
            new_line_data: [..] u8;
            for i: 0..lines[0].count - 1 {
                if array_find(cols_to_expand, i) {
                    array_add(*new_line_data, #char ".");
                }
                char := lines[j][i];
                array_add(*new_line_data, char);
            }
            new_line.data = new_line_data.data;
            array_add(*expanded, new_line);
        }
    }
    return expanded;
}

main :: () {
    log("============ Part 1 ============");
    part1();
}