#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";
#import "Math";

//FILENAME :: "input.txt";
FILENAME :: "sample.txt";

part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\n");

    result := 0;
    for lines {
        line := trim(it);
        line_parts := split(line, ":");
        numbers := split(trim(line_parts[1]), "|");
        winning_numbers: [..] int;
        for split(trim(numbers[0]), " ") {
            trimmed := trim(it);
            if trimmed.count == 0 continue;
            num := string_to_int(trimmed);
            array_add(*winning_numbers, num);
        }
        card_result := -1;
        for split(trim(numbers[1]), " ") {
            trimmed := trim(it);
            if trimmed.count == 0 continue;
            num := string_to_int(trimmed);
            ok := array_find(winning_numbers, num);
            if ok {
                card_result += 1;
            }
        }
        if result != -1 {
            result += cast(int) pow(2, cast(float) card_result);
        }
    }

    log("Res %", result);
}


part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\n");
    copies: Table(int, int);

    result := 0;
    for lines {
        line := trim(it);
        line_parts := split(line, ":");

        card_number := string_to_int(trim(split(trim(line_parts[0]), "Card ")[1]));
        log("Card %", card_number);

        numbers := split(trim(line_parts[1]), "|");
        winning_numbers: [..] int;
        for split(trim(numbers[0]), " ") {
            trimmed := trim(it);
            if trimmed.count == 0 continue;
            num := string_to_int(trimmed);
            array_add(*winning_numbers, num);
        }
        print("winning num: ");
        for winning_numbers print("% ", it);
        print("\n");
        card_result := -1;
        print("num: ");
        for split(trim(numbers[1]), " ") {
            trimmed := trim(it);
            if trimmed.count == 0 continue;
            num := string_to_int(trimmed);
            print("% ", num);
            ok := array_find(winning_numbers, num);
            if ok {
                card_result += 1;
            }
        }
        current_copies, current_ok := table_find(*copies, card_number);
        if !current_ok then current_copies = 1;
        for i: 1..card_result {
            card_number_to_increase := card_number + i;
            copies_number, ok := table_find(*copies, card_number_to_increase);
            new_copies_number := ifx ok then copies_number + current_copies else current_copies;
            table_set(*copies, card_number_to_increase, new_copies_number);
        }
    }

    for v, k: copies {
        log("k %, v %", k, v);
    }

    log("Res %", result);
}



main :: () {
    log("============ Part 1 ============");
    part1();
    log("============ Part 2 ============");
    part2();
}
