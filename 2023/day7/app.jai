#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";
#import "Math";
#import "Sort";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";


part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");
    hands_and_bets := NewArray(lines.count, HandAndBet);
    for lines {
        parts := split(trim(it), " ");
        hand := trim(parts[0]);
        hand_type := get_hand_type(hand);
        bet := string_to_int(trim(parts[1]));
        hands_and_bets[it_index] = .{hand, hand_type, bet };
    }

    quick_sort(hands_and_bets, compare_hands);
    
    result := 0;
    for i: 0..hands_and_bets.count - 1 {
        h := hands_and_bets[i];
        multiplier := hands_and_bets.count - i;
        hand_score := h.bet * multiplier;
        result += hand_score;
    }
    log("Res %", result);
}

HandAndBet :: struct {
    hand: string;
    hand_type: HandType;
    bet: int;
}

HandType :: enum {
    HIGH_CARD :: 0;
    ONE_PAIR :: 1;
    TWO_PAIR :: 2;
    THREE_OF_KIND :: 3;
    FULL_HOUSE :: 4;
    FOUR_OF_KIND :: 5;
    FIVE_OF_KIND :: 6;
}

card_priority_table: Table(u8, int);

get_hand_type :: (hand: string) -> HandType {
    counts: Table(u8, int);
    defer deinit(*counts);
    for i: 0..hand.count - 1 {
        c := hand[i];
        add_one_or_set_one(*counts, c);
    }

    //quick_sort(counts.entries, compare_entries);
    values: [..] int;
    for v, k: counts array_add(*values, v);
    quick_sort(values, compare_ints);
    
    if values[0] == 3 && values[1] == 2 return HandType.FULL_HOUSE;
    else if values[0] == 5 return HandType.FIVE_OF_KIND;
    else if values[0] == 4 return HandType.FOUR_OF_KIND;
    else if values[0] == 3 return HandType.THREE_OF_KIND;
    else if values[0] == 2 && values[1] == 2 return HandType.TWO_PAIR;
    else if values[0] == 2 return HandType.ONE_PAIR;
    else return HandType.HIGH_CARD;
}

get_hand_type_p2 :: (hand: string) -> HandType {
    counts: Table(u8, int);
    defer deinit(*counts);
    for i: 0..hand.count - 1 {
        c := hand[i];
        add_one_or_set_one(*counts, c);
    }

    jokers, ok := table_find(*counts, #char "J");
    if ok {
        to_joke: u8 = #char "2";
        to_joke_number := 0;
        for v, k: counts {
            if k != #char "J" {
                if v > to_joke_number {
                    to_joke_number = v;
                    to_joke = k;
                } 
            }
        }

        if to_joke_number != 0 {
            v, _ := table_find(*counts, to_joke);
            table_set(*counts, to_joke, v + jokers);
            table_remove(*counts, #char "J");
        }
    }

    //quick_sort(counts.entries, compare_entries);
    values: [..] int;
    for v, k: counts array_add(*values, v);
    quick_sort(values, compare_ints);
    
    if values[0] == 3 && values[1] == 2 return HandType.FULL_HOUSE;
    else if values[0] == 5 return HandType.FIVE_OF_KIND;
    else if values[0] == 4 return HandType.FOUR_OF_KIND;
    else if values[0] == 3 return HandType.THREE_OF_KIND;
    else if values[0] == 2 && values[1] == 2 return HandType.TWO_PAIR;
    else if values[0] == 2 return HandType.ONE_PAIR;
    else return HandType.HIGH_CARD;
}

// todo why not working?
/*compare_entries :: (a: Table.Entry, b: Table.Entry) -> s32 {
    delta := b.value - a.value;
    if delta > 0 return 1;
    if delta < 0 return -1;
    return 0;
}*/
compare_ints :: (a: int, b: int) -> s32 {
    return cast(s32)b - cast(s32)a;
}

compare_hands :: (a: HandAndBet, b: HandAndBet) -> s32 {
    delta := b.hand_type - a.hand_type;
    if delta != 0 {
        return cast(s32) delta;
    }

    for i: 0..a.hand.count - 1 {
        va, _ := table_find(*card_priority_table, a.hand[i]);
        vb, _ := table_find(*card_priority_table, b.hand[i]);
        if vb - va != 0 {
            return cast(s32)(vb - va);
        }
    }
    return 0;
}

add_one_or_set_one :: (table: *Table, key: u8) {
    value, ok := table_find(table, key);
    new_value := ifx ok then value + 1 else 1;
    table_set(table, key, new_value);
}

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n");
    hands_and_bets := NewArray(lines.count, HandAndBet);
    for lines {
        parts := split(trim(it), " ");
        hand := trim(parts[0]);
        hand_type := get_hand_type_p2(hand);
        bet := string_to_int(trim(parts[1]));
        hands_and_bets[it_index] = .{hand, hand_type, bet };
    }

    quick_sort(hands_and_bets, compare_hands);
    print_array("asfd", hands_and_bets);
    
    result := 0;
    for i: 0..hands_and_bets.count - 1 {
        h := hands_and_bets[i];
        multiplier := hands_and_bets.count - i;
        hand_score := h.bet * multiplier;
        log("Hand % score %", h, hand_score);
        result += hand_score;
    }
    log("Res %", result);

}

init_card_priority_table :: () {
    table_set(*card_priority_table, #char "A", 15);
    table_set(*card_priority_table, #char "K", 14);
    table_set(*card_priority_table, #char "Q", 13);
    table_set(*card_priority_table, #char "J", 12);
    table_set(*card_priority_table, #char "T", 11);
    table_set(*card_priority_table, #char "9", 9);
    table_set(*card_priority_table, #char "8", 8);
    table_set(*card_priority_table, #char "7", 7);
    table_set(*card_priority_table, #char "6", 6);
    table_set(*card_priority_table, #char "5", 5);
    table_set(*card_priority_table, #char "4", 4);
    table_set(*card_priority_table, #char "3", 3);
    table_set(*card_priority_table, #char "2", 2);
}

print_array :: (header: string, a: [] $T) {
    print("%: ", header);
    for a {
        print("% ", it);
    }
    print("\n");
}

main :: () {
    init_card_priority_table();
    log("============ Part 1 ============");
    part1();
    table_set(*card_priority_table, #char "J", 1);
    log("============ Part 2 ============");
    part2();
}