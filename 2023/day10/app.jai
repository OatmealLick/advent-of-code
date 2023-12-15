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


// maybe I could've used Pos :: struct {x: int; y: int; } ?
start_nexts :: (x: int, y: int) -> int, int, int, int {
    
    start := start_real_character();
    if start == #char "|" {
        return x, y - 1, x, y + 1;
    } else {
        return x + 1, y, x, y + 1;
    }
}

start_real_character :: () -> u8 {
    // hardcoded to avoid tons of if statements :) 
    start: u8;
    if FILENAME == "input.txt" {
        start = #char "|";
    } else {
        start = #char "F";
    } 
    return start;
}


next :: (prev_x: int, prev_y: int, x: int, y: int, lines: [] string) -> int, int {
    c := lines[y][x];

    x1, y1, x2, y2: int;
    if c == #char "|" {
        x1 = x;
        y1 = y + 1;
        x2 = x;
        y2 = y - 1;
    } else if c == #char "-" {
        x1 = x - 1;
        y1 = y;
        x2 = x + 1;
        y2 = y;
    } else if c == #char "F" {
        x1 = x;
        y1 = y + 1;
        x2 = x + 1;
        y2 = y;
    } else if c == #char "L" {
        x1 = x;
        y1 = y - 1;
        x2 = x + 1;
        y2 = y;
    } else if c == #char "J" {
        x1 = x;
        y1 = y - 1;
        x2 = x - 1;
        y2 = y;
    } else if c == #char "7" {
        x1 = x;
        y1 = y + 1;
        x2 = x - 1;
        y2 = y;
    } else {
        log("Got %, this should not happen!", c);
        return -1, -1;
    }
    if prev_x == x1 && prev_y == y1 {
        return x2, y2; 
    } else {
        return x1, y1;
    }
}

part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");

    prev_x, prev_y: int;
    x1, y1, x2, y2: int;
    for j: 0..lines.count - 1 for i: 0..lines[j].count - 1 {
        if lines[j][i] == #char "S" {
            prev_x = i;
            prev_y = j;
            x1, y1, x2, y2 = start_nexts(i, j);
            break;
        }
    }

    x, y := x1, y1;
    steps := 0;
    while true {
        steps += 1;
        next_x, next_y := next(prev_x, prev_y, x, y, lines);
        log("for prev %, % and %, % next is %, %", prev_x, prev_y, x, y, next_x, next_y);
        if lines[next_y][next_x] == #char "S" break;
        prev_x, prev_y = x, y;
        x, y = next_x, next_y;
    }
    steps += 1;
    log("steps %, steps / 2 = %", steps, cast(int) (steps / 2));
}


part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");

    prev_x, prev_y: int;
    x1, y1, x2, y2: int;
    for j: 0..lines.count - 1 for i: 0..lines[j].count - 1 {
        if lines[j][i] == #char "S" {
            prev_x = i;
            prev_y = j;
            x1, y1, x2, y2 = start_nexts(i, j);
            break;
        }
    }

    x, y := x1, y1;
    steps := 0;
    while true {
        steps += 1;
        next_x, next_y := next(prev_x, prev_y, x, y, lines);
        log("for prev %, % and %, % next is %, %", prev_x, prev_y, x, y, next_x, next_y);
        if lines[next_y][next_x] == #char "S" break;
        prev_x, prev_y = x, y;
        x, y = next_x, next_y;
    }
    steps += 1;
    log("steps %, steps / 2 = %", steps, cast(int) (steps / 2));
}

main :: () {
    log("============ Part 1 ============");
    part1();
    log("============ Part 2 ============");
    part2();
}