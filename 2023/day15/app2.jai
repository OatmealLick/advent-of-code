#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";
#import "Math";
#import "Sort";
#import "Hash";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");
    rows_to_expand, cols_to_expand := expand(lines);
    galaxies: [..] Pos;
    for j: 0..lines.count - 1 for i: 0..lines[0].count - 1 {
        if lines[j][i] != #char "." {
            array_add(*galaxies, .{i, j});
        }
    }
    lowest_path: u64 = 0;
    pairs := 0;
    
    //gap := 100;
    gap: u64 = 1_000_000;
    for j: 0..galaxies.count - 1 {
        for i: j+1..galaxies.count - 1 {
            pairs += 1;
            a := galaxies[j];
            b := galaxies[i];
            path: u64 = 0;
            for k: min(a.x, b.x) + 1..max(a.x, b.x) {
                if array_find(cols_to_expand, k) {
                    path += gap;
                } else {
                    path += 1;
                }
            }
            for k: min(a.y, b.y) + 1..max(a.y, b.y) {
                if array_find(rows_to_expand, k) {
                    path += gap;
                } else {
                    path += 1;
                }
            }
            lowest_path += path;
        }
    }

    log("result: %", lowest_path);
    log("pairs: %", pairs);
}

Pos :: struct {
    x: int;
    y: int;
}

expand :: (lines: [] string) -> [] int, [] int {
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
    return rows_to_expand, cols_to_expand;
}

main :: () {
    log("============ Part 2 ============");
    part2();
}