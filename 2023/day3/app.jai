#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";

Pos :: struct {
    x: int;
    y: int;
    
}

is_equal_pos :: (x: Pos, y: Pos) -> bool {
    return (x.x == y.x) && (x.y == y.y);
}

hash_pos :: (x: Pos) -> u32 {
    return cast(u32) x.x + cast(u32) 31 * cast(u32)x.y;
}

part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\n");

    valid_part_numbers: [..] int;

    for line, line_index: lines {
        char_index := 0;
        while char_index < line.count {
            char := line[char_index];
            
            if char >= #char "0" && char <= #char "9" {
                number_length := 0;
                last_char := char;
                last_char_index := char_index;
                while last_char >= #char "0" && last_char <= #char "9" {
                    number_length += 1;
                    last_char_index += 1;
                    last_char = line[last_char_index];
                }
                number_digits: string = ---;
                number_digits.count = number_length;
                number_digits.data = *line[char_index];

                if has_adjacent_symbol(.{char_index, line_index}, number_length, lines) {
                    part_number := string_to_int(number_digits);
                    array_add(*valid_part_numbers, part_number);
                }
                
                char_index += number_length;
            } else {
                char_index += 1;
            }
        }
    }

    sum := 0;
    for valid_part_numbers {
        sum += it;
    }

    log("Sum %", sum);
    // 396551 too low
    // 526098 too high
}

has_adjacent_symbol :: (start: Pos, length: int, lines: [] string) -> bool, Pos {
    is_first_line := start.y == 0;
    is_last_line := start.y == lines.count - 1;
    // up
    if !is_first_line for i: 0..length - 1 {
        if is_symbol(lines[start.y - 1][start.x + i]) return true, .{start.x + i, start.y - 1};
    }
    
    // down
    if !is_last_line for i: 0..length - 1{
        if is_symbol(lines[start.y + 1][start.x + i]) return true, .{start.x + i, start.y + 1};
    }
    
    safe_start_y_offset := ifx is_first_line then 0 else -1;
    safe_end_y_offset := ifx is_last_line then 0 else 1;
    // left

    if start.x > 0 for i: safe_start_y_offset..safe_end_y_offset {
        if is_symbol(lines[start.y + i][start.x - 1]) return true, .{start.x - 1, start.y + i};
    }
    
    // right
    if start.x + length - 1 < lines[0].count - 1 for i: safe_start_y_offset..safe_end_y_offset {
        if is_symbol(lines[start.y + i][start.x + length]) return true, .{start.x + length, start.y + i};
    }

    return false, .{0, 0};
}

is_symbol :: (char: u8) -> bool {
    // carriage return babyyyy
    return !((char >= #char "0" && char <= #char "9") || char == #char "." || char == #char "\r");
}

Res :: struct {
    count: int = 0;
    result: int = 0;
}

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\n");
    results: Table(Pos, Res, given_compare_function=is_equal_pos, given_hash_function=hash_pos);

    for line, line_index: lines {
        char_index := 0;
        while char_index < line.count {
            char := line[char_index];
            
            if char >= #char "0" && char <= #char "9" {
                number_length := 0;
                last_char := char;
                last_char_index := char_index;
                while last_char >= #char "0" && last_char <= #char "9" {
                    number_length += 1;
                    last_char_index += 1;
                    last_char = line[last_char_index];
                }
                number_digits: string = ---;
                number_digits.count = number_length;
                number_digits.data = *line[char_index];

                symbols := get_adjacent_symbols(.{char_index, line_index}, number_length, lines);
                if symbols.count != 0 {
                    part_number := string_to_int(number_digits);
                    for symbols {
                        res, find_ok := table_find(*results, it);
                        new_res := ifx find_ok then Res.{res.count + 1, res.result * part_number} else Res.{1, part_number};
                        table_set(*results, it, new_res);
                    }
                }
                
                char_index += number_length;
            } else {
                char_index += 1;
            }
        }
    }

    sum := 0;
    // first value, then key, sweet 
    for res, pos: results {
        if res.count == 2 sum += res.result;
    }

    log("Sum %", sum);
}

get_adjacent_symbols :: (start: Pos, length: int, lines: [] string) -> [] Pos {
    is_first_line := start.y == 0;
    is_last_line := start.y == lines.count - 1;
    symbols: [..] Pos;
    // up
    if !is_first_line for i: 0..length - 1 {
        if is_symbol(lines[start.y - 1][start.x + i]) {
            array_add(*symbols, .{start.x + i, start.y - 1});
        }
    }
    
    // down
    if !is_last_line for i: 0..length - 1{
        if is_symbol(lines[start.y + 1][start.x + i]) array_add(*symbols, .{start.x + i, start.y + 1});
    }
    
    safe_start_y_offset := ifx is_first_line then 0 else -1;
    safe_end_y_offset := ifx is_last_line then 0 else 1;
    // left

    if start.x > 0 for i: safe_start_y_offset..safe_end_y_offset {
        if is_symbol(lines[start.y + i][start.x - 1]) array_add(*symbols, .{start.x - 1, start.y + i});
    }
    
    // right
    if start.x + length - 1 < lines[0].count - 1 for i: safe_start_y_offset..safe_end_y_offset {
        if is_symbol(lines[start.y + i][start.x + length]) array_add(*symbols, .{start.x + length, start.y + i});
    }

    return symbols;
}



main :: () {
    log("============ Part 1 ============");
    part1();
    log("============ Part 2 ============");
    part2();
}
