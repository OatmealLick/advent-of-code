#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";
#import "Math";
#import "Sort";
#import "Hash";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";

part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");
    result := 0;
    for lines {
        strings := split(trim(it), " ");
        numbers := NewArray(strings.count, int);
        for strings {
            numbers[it_index] = string_to_int(strings[it_index]);
        }
        prediction := predict1(numbers);
        //log("[%] prediction: % for line %", it_index, prediction, numbers);
        result += prediction;
    }

    log("res %", result);
}

predict1 :: (line: [] int) -> int {
    same := true;
    for i: 0..line.count - 2 {
        if line[i] != line[i + 1] {
            same = false;
            break;
        }
    }

    if same {
        return line[line.count - 1];
    } else {
        new_line := NewArray(line.count - 1, int);
        for i: 0..line.count - 2 {
            new_line[i] = line[i + 1] - line[i];
        }
        prediction := predict1(new_line);
        return prediction + line[line.count - 1];
    }
}

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");
    result := 0;
    for lines {
        strings := split(trim(it), " ");
        numbers := NewArray(strings.count, int);
        for strings {
            numbers[it_index] = string_to_int(strings[it_index]);
        }
        prediction := predict2(numbers);
        //log("[%] prediction: % for line %", it_index, prediction, numbers);
        result += prediction;
    }

    log("res %", result);
}

predict2 :: (line: [] int) -> int {
    same := true;
    for i: 0..line.count - 2 {
        if line[i] != line[i + 1] {
            same = false;
            break;
        }
    }

    if same {
        return line[line.count - 1];
    } else {
        new_line := NewArray(line.count - 1, int);
        for i: 0..line.count - 2 {
            new_line[i] = line[i + 1] - line[i];
        }
        prediction := predict2(new_line);
        //return prediction + line[line.count - 1];
        return line[0] - prediction;
    }
}

main :: () {
    log("============ Part 1 ============");
    part1();
    log("============ Part 2 ============");
    part2();
}