#import "Basic";
#import "String";
#import "File";

RED_ALLOWED :: 12;
GREEN_ALLOWED :: 13;
BLUE_ALLOWED :: 14;

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";

part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\n");
    valid_game_ids: [..] int;
    for lines {
        line := trim(it);
        line_parts := split(line, ":");
        game_id_str := split(line_parts[0], "Game ")[1];
        log("%", game_id_str);
        game_id := string_to_int(game_id_str);

        sets := split(line_parts[1], ";");
        valid := true;
        for set: sets {
            moves := split(trim(set), ",");
            for move: moves {
                parts := split(trim(move), " ");
                num := string_to_int(parts[0]);
                if parts[1] == "red" {
                    if num > RED_ALLOWED {
                        valid = false;
                        break;
                    }
                } else if (parts[1] == "green") {
                    if num > GREEN_ALLOWED {
                        valid = false;
                        break;
                    }
                } else if (parts[1] == "blue") {
                    if num > BLUE_ALLOWED {
                        valid = false;
                        break;
                    }
                }
            }
        }

        if valid array_add(*valid_game_ids, game_id);
    }
    sum := 0;
    for valid_game_ids sum += it;
    log("res %", sum);
}

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\n");
    valid_game_ids: [..] int;
    for lines {
        max_red := 0;
        max_green := 0;
        max_blue := 0;
        
        line := trim(it);
        line_parts := split(line, ":");
        game_id_str := split(line_parts[0], "Game ")[1];
        log("%", game_id_str);
        game_id := string_to_int(game_id_str);

        sets := split(line_parts[1], ";");
        for set: sets {
            moves := split(trim(set), ",");
            for move: moves {
                parts := split(trim(move), " ");
                num := string_to_int(parts[0]);
                if parts[1] == "red" {
                    max_red = max(max_red, num);
                } else if (parts[1] == "green") {
                    max_green = max(max_green, num);
                } else if (parts[1] == "blue") {
                    max_blue = max(max_blue, num);
                }
            }
        }

        power := max_red * max_green * max_blue;
        array_add(*valid_game_ids, power);
        log("power %", power);
    }
    sum := 0;
    for valid_game_ids sum += it;
    log("res %", sum);
}

main :: () {
    part1();
    part2();
}
