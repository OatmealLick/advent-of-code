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

    lines := split(file_contents, "\r\n\r\n");
    seeds_strings := split(trim(split(trim(lines[0]), ":")[1]), " ");
    seeds := NewArray(seeds_strings.count, int);
    for seeds_strings {
        seeds[it_index] = string_to_int(it);
    }

    for i: 1..lines.count - 1 {
        mapping_lines := split(trim(lines[i]), "\r\n");
        mapping_ranges: [..] MappingRange;
        for j: 1..mapping_lines.count - 1 {
            mapping_line := split(trim(mapping_lines[j]), " ");
            array_add(*mapping_ranges, .{
                string_to_int(mapping_line[0]), 
                string_to_int(mapping_line[1]), 
                string_to_int(mapping_line[2])
            });
        }

        quick_sort(mapping_ranges, compare_mapping_ranges);

        for seeds {
            mapping_range_index := 0;
            while it >= mapping_ranges[mapping_range_index].src {
                mapping_range_index += 1;
                if mapping_range_index == mapping_ranges.count {
                    break;
                }
            }
            if mapping_range_index == 0 {
                continue;
            }
            mapping_range_to_use := mapping_ranges[mapping_range_index - 1];
            if it >= mapping_range_to_use.src + mapping_range_to_use.len {
                continue;
            }
            offset := it - mapping_range_to_use.src;
            seeds[it_index] = mapping_range_to_use.dest + offset;
        }
    }


    res := 999_999_999;
    for seeds res = min(res, it);
    log("Res: %", res);
}

compare_mapping_ranges :: (a: MappingRange, b: MappingRange) -> s64 {
    delta := a.src - b.src;
    if delta < 0 return -1;
    if delta > 0 return  1;
    return 0;
}

compare_mapping_ranges_dest :: (a: MappingRange, b: MappingRange) -> s64 {
    delta := a.dest - b.dest;
    if delta < 0 return -1;
    if delta > 0 return  1;
    return 0;
}

Map :: struct {
    ranges: [] MappingRange;
}

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(file_contents, "\r\n\r\n");
    seeds_strings := split(trim(split(trim(lines[0]), ":")[1]), " ");
    seed_ranges: [..] SeedRange;
    i := 0;
    while i < seeds_strings.count {
        start := string_to_int(seeds_strings[i]);
        length := string_to_int(seeds_strings[i + 1]);
        array_add(*seed_ranges, .{start, length});
        i += 2;
    }
    quick_sort(seed_ranges, compare_seed_ranges);


    maps: [..] Map;
    
    for < i: lines.count - 1..1 {
        log("i %", i);
        mapping_lines := split(trim(lines[i]), "\r\n");
        mapping_ranges: [..] MappingRange;
        for j: 1..mapping_lines.count - 1 {
            mapping_line := split(trim(mapping_lines[j]), " ");
            array_add(*mapping_ranges, .{
                string_to_int(mapping_line[0]), 
                string_to_int(mapping_line[1]), 
                string_to_int(mapping_line[2])
            });
        }

        quick_sort(mapping_ranges, compare_mapping_ranges_dest);
        map: Map = ---;
        map.ranges = mapping_ranges;
        array_add(*maps, map);
        print_array("Map", map.ranges);
    }

    print_array("Maps", maps);
    starting_map := maps[0];
    for starting_map.ranges {
        for location: it.dest..it.dest + it.len - 1 {
            // location - sorted by asc
            value := location;
            //if location % 100_000 == 0 log("Checking location %", location);
            for map_index: 0..maps.count - 1 {
                map := maps[map_index];
                mapping_range_index := 0;
                while value >= map.ranges[mapping_range_index].dest {
                    mapping_range_index += 1;
                    if mapping_range_index == map.ranges.count {
                        break;
                    }
                }
                if mapping_range_index == 0 {
                    continue;
                }
                mapping_range_to_use := map.ranges[mapping_range_index - 1];
                if value >= mapping_range_to_use.dest + mapping_range_to_use.len {
                    continue;
                }
                offset := value - mapping_range_to_use.dest;
                value = mapping_range_to_use.src + offset;
                //log("After map % ended up with value % (used range %)", map_index, value, mapping_range_to_use);
            }
            found := seed_find(seed_ranges, value);
            if found {
                log("Found matching seed % for location %", value, location);
                return;
            }
        }
    }
    
    res := 999_999_999;
    //for seeds res = min(res, it);
    log("Res: %", res);
}

SeedRange :: struct {
    start: int;
    length: int;
}

compare_seed_ranges :: (a: SeedRange, b: SeedRange) -> s64 {
    delta := a.start - b.start;
    if delta < 0 return -1;
    if delta > 0 return  1;
    return 0;
}

seed_find :: (seed_ranges: [] SeedRange, seed: int) -> bool {
    // should be sorted by start
    for seed_ranges {
        if seed >= it.start && seed < it.start + it.length return true;
    }
    return false;
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