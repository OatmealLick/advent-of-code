#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";
#import "Math";
#import "Sort";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";

MappingRange :: struct {
    dest: int;
    src: int;
    len: int;
}

part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");
    _, _, times_string := split_from_left(trim(lines[0]), "Time:");
    _, _, distances_string := split_from_left(trim(lines[1]), "Distance:");
    times := split_by_spaces_to_int(times_string);
    distances := split_by_spaces_to_int(distances_string);
    result := 1;
    for i: 0..times.count - 1 {
        time := times[i];
        distance := distances[i];

        highest_time := -1;
        for < test_time: time - 1..1 {
            if (time - test_time) * test_time > distance {
                highest_time = test_time;
                break;
            }
        } 
        lowest_time := -1;
        for test_time: 1..time - 1 {
            if (time - test_time) * test_time > distance {
                lowest_time = test_time;
                break;
            }
        } 

        log("for time %, distance % got high %, low %", time, distance, highest_time, lowest_time);
        result *= (highest_time - lowest_time + 1);
    }
    log("res %", result);
}

// I spent 10x more time to have proper parsing function in this language
// and as a prize I get -- different parsing in part2?!
part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");
    _, _, times_string := split_from_left(trim(lines[0]), "Time:");
    _, _, distances_string := split_from_left(trim(lines[1]), "Distance:");
    time := split_ignore_spaces_to_int(times_string);
    distance := split_ignore_spaces_to_int(distances_string);
    result := 1;

    highest_time := -1;
    for < test_time: time - 1..1 {
        if (time - test_time) * test_time > distance {
            highest_time = test_time;
            break;
        }
    } 
    lowest_time := -1;
    for test_time: 1..time - 1 {
        if (time - test_time) * test_time > distance {
            lowest_time = test_time;
            break;
        }
    } 

    log("for time %, distance % got high %, low %", time, distance, highest_time, lowest_time);
    result *= (highest_time - lowest_time + 1);
    log("res %", result);
}

main :: () {
    log("============ Part 1 ============");
    part1();
    log("============ Part 2 ============");
    part2();
}


print_array :: (header: string, a: [] $T) {
    print("%: ", header);
    for a {
        print("% ", it);
    }
    print("\n");
}
split_by_spaces_to_int :: (s: string) -> [] int {
    trimmed := trim(s);
    parts: [..] int;
    i := 0;
    log(trimmed);
    for j: 0..trimmed.count - 1 {
        c := trimmed[j];
        if c != #char " " {
            i += 1;
        } else if i != 0 && c == #char " " {
            new_s: [] u8 = ---;
            new_s.count = i;
            new_s.data = *trimmed.data[j - i];
            array_add(*parts, string_to_int(cast(string) new_s));
            i = 0;
        }
    }
    
    new_s: string = ---;
    new_s.count = i;
    new_s.data = *trimmed.data[trimmed.count - i];
    array_add(*parts, string_to_int(new_s));
    return parts;
}

split_ignore_spaces_to_int :: (s: string) -> int {
    trimmed := trim(s);
    parts: [..] u8;
    log(trimmed);
    for j: 0..trimmed.count - 1 {
        c := trimmed[j];
        if c != #char " " {
            array_add(*parts, c);
        }
    }
    
    return string_to_int(cast(string) parts);
    /*new_s: string = ---;
    new_s.count = parts.count;
    new_s.data = parts.data;
    array_add(*parts, string_to_int(new_s));
    return parts;*/
}
