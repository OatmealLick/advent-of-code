#import "Basic";
#import "String";
#import "File";
#import "Math";
#import "Sort";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";

Vector2i :: struct {
    x: int;
    y: int;
}

operator == :: (a: [] Vector2i, b: [] Vector2i) -> bool {
    if a.count != b.count return false;
    for a if a[it_index] != b[it_index] return false;
    return true;
}

operator == :: (a: Vector2i, b: Vector2i) -> bool {
    return a.x == b.x && a.y == b.y;
}

operator == :: (a: Range, b: Range) -> bool {
    return a.from == b.from && a.to == b.to;
}

operator == :: (a: [] Range, b: [] Range) -> bool {
    if a.count != b.count return false;
    for a if !compare_ranges(a[it_index], b[it_index]) return false;
    return true;
}
compare_ranges :: (a: Range, b: Range) -> int {
    return a.from.x - b.from.x;
}


hex_char_to_u32 :: (c : u8) -> u32 {
    if c >= #char "a" return xx(c - #char "a" + 0xa);
    if c >= #char "0" return xx(c - #char "0");
    return 1;
}

Range :: struct {
    from: Vector2i;
    to: Vector2i;
}

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(trim(file_contents), "\r\n");

    position := Vector2i.{0, 0};
    edges: [..] Range;

    for lines {
        parts := split(it, " ");
        hex := parts[2];
        hex.data += 2;
        hex.count -= 3;
        distance := (hex_char_to_u32(hex[0]) << 16) | (hex_char_to_u32(hex[1]) << 12) | (hex_char_to_u32(hex[2]) << 8) | (hex_char_to_u32(hex[3]) << 4) | (hex_char_to_u32(hex[4]));
        direction := (hex_char_to_u32(hex[5]));
        new_position: Vector2i;
        if direction == 3 {
            new_position = Vector2i.{position.x, position.y - distance};
        } else if direction == 1 {
            new_position = Vector2i.{position.x, position.y + distance};
        } else if direction == 0 {
            new_position = Vector2i.{position.x + distance, position.y};
        } else {
            new_position = Vector2i.{position.x - distance, position.y};
        }
        //new_position: Vector2i;
        //direction := parts[0][0];
        //distance := string_to_int(parts[1]);
        //for 0..distance - 1 {
        //    if direction == #char "U" {
        //        new_position = Vector2i.{position.x, position.y - distance};
        //    } else if direction == #char "D" {
        //        new_position = Vector2i.{position.x, position.y + distance};
        //    } else if direction == #char "R" {
        //        new_position = Vector2i.{position.x + distance, position.y};
        //    } else {
        //        new_position = Vector2i.{position.x - distance, position.y};
        //    }
        //}

        array_add(*edges, .{position, new_position});
        position = new_position;
    }

    // ideas
    // 1. Divide the space to rectangles (how doe?) and count a * b, and subtract overlapping
    // 2. Traverse from one side to another with a line, eg. from min south to top north. Maintain ranges that are 'active' and count all the 'active' rects in a line.
    // 3. BFS obviosuly does not scale (but also tries to be too general)

    // 2.
    min_y: int;
    max_y: int;
    horizontal_edges: [..] Range;

    for edges {
        min_y = min(min_y, min(it.from.y, it.to.y));
        max_y = max(max_y, max(it.from.y, it.to.y));

        if it.from.y == it.to.y {
            to_add := it;
            if it.from.x > it.to.x {
                to_add = .{from=.{it.to.x, it.from.y}, to=.{it.from.x, it.from.y}};
            }
            array_add(*horizontal_edges, to_add);
        }
    }
    quick_sort(horizontal_edges, compare_ranges);
    log("min %, max %", min_y, max_y);

    y_milestones: [..] int;
    for horizontal_edges array_add_if_unique(*y_milestones, it.from.y);
    compare_ints :: (a: int, b: int) -> int { return a - b; }
    quick_sort(y_milestones, compare_ints);

    area :u64= 0;
    current_horizontal_ranges: [] Vector2i;
    start_edges := get_edges(y_milestones[0], horizontal_edges);
    for start_edges current_horizontal_ranges = merge_new_range(current_horizontal_ranges, it);
    prev_j := y_milestones[0];
    area += line_value(current_horizontal_ranges, start_edges);
    log("[%] line value % of total %", 0, area, area);
    for i: 1..y_milestones.count - 1 {
        j := y_milestones[i];
        line_area: u64 = 0;
        for current_horizontal_ranges {
            height := j - prev_j - 1;
            line_area += (cast(u64)((it.y) - (it.x)) + 1) * cast(u64)height;
            //log("y milestone %, prev %, height %, for range %, line area %", j, prev_j, height, it, line_area);
        }
        area += line_area;
        //log("[%] running for line % with prev %", i, j, prev_j);
        prev_j = j;
        
        this_line_edges := get_edges(j, horizontal_edges);
        line_value_area := line_value(current_horizontal_ranges, this_line_edges);
        area += line_value_area;
        //log("[%] line area from last % and line value % of total %", i, line_area, line_value_area, area);

        for this_line_edges {
            current_horizontal_ranges = merge_new_range(current_horizontal_ranges, it);
            // leaking mem, !
        }

        //log("Milestone % / %", i, y_milestones.count - 1);
        //log("ranges count %", current_horizontal_ranges.count);
        //for current_horizontal_ranges print("% ", it);
        //log("\n");
        //if i > 18 break;
    }
    
    log("res: %", area);
}

get_edges :: (y: int, reference_edges: [] Range) -> [] Range {
    edges: [..] Range;
    for reference_edges if it.from.y == y array_add(*edges, it);
    return edges;
}

array_add_if_unique2 :: (array: *[..] Vector2i, item: Vector2i) -> bool, s64 {   // Return true if newly added; also return index.
    for <<array if it == item {
        log("DUPLICATE tried adding % to [%] %", item, array.count, array);
        return false, it_index;
    }

    array_add(array, item);
    return true, array.count-1;
}

// removes range if fully contained, adds if not
merge_new_range :: (current_ranges: [] Vector2i, to_add_range: Range) -> [] Vector2i {
    //log("merge new range, current ranges [%] %", current_ranges.count, current_ranges);
    for current_ranges {
        if to_add_range.from.x >= it.x && to_add_range.to.x <= it.y {
            //log("Remove range % - %", to_add_range.from.x, to_add_range.to.x);
            // it is fully contained!
            // remove and return

            // at this point I'm desperate
            new_current_ranges: [..] Vector2i;
            for current_ranges {
                if to_add_range.from.x >= it.x && to_add_range.to.x <= it.y {
                    if to_add_range.from.x == it.x && to_add_range.to.x == it.y {
                        // fully remove the range, because it is all covered [XXXXXX]
                        continue;
                    } if to_add_range.from.x == it.x || to_add_range.to.x == it.y {
                        // the removing part touches one end - the removal process will produce only one [XXXXX......] or [......XXXX]
                        from := ifx to_add_range.from.x == it.x then to_add_range.to.x else it.x;
                        to := ifx to_add_range.to.x == it.y then to_add_range.from.x else it.y;
                        array_add_if_unique2(*new_current_ranges, .{from, to});
                    } else {
                        // the removing part falls within the range - it will produce two ranges on both ends [...XXXX....]
                        array_add_if_unique2(*new_current_ranges, .{it.x, to_add_range.from.x});
                        array_add_if_unique2(*new_current_ranges, .{to_add_range.to.x, it.y});
                    }

                } else {
                    array_add_if_unique2(*new_current_ranges, it);
                }
            }
            return new_current_ranges;
        }
    }
    //log("Add range % - %", to_add_range.from.x, to_add_range.to.x);

    // current ranges sorted by from.x asc, and have no overlapping ranges
    new_current_ranges: [..] Vector2i;
    if current_ranges.count > 0 {
        if to_add_range.to.x < current_ranges[0].x {
            array_add_if_unique2(*new_current_ranges, .{to_add_range.from.x, to_add_range.to.x});
            for current_ranges array_add_if_unique2(*new_current_ranges, it);
            return new_current_ranges;
        }

        if to_add_range.from.x > current_ranges[current_ranges.count - 1].y {
            for current_ranges array_add_if_unique2(*new_current_ranges, it);
            array_add_if_unique2(*new_current_ranges, .{to_add_range.from.x, to_add_range.to.x});
            return new_current_ranges;
        }

        i := 0;
        new_from := -1; // if its -1 its unset 
        new_to := to_add_range.to.x;
        //new_to := -1;
        added := false;
        //log("Merging % with %", to_add_range, current_ranges);
        while i < current_ranges.count {
            from := current_ranges[i].x;
            to := current_ranges[i].y;
            if to < to_add_range.from.x {
                //log("PRE Current %, new current %", current_ranges[i], new_current_ranges);
                array_add_if_unique2(*new_current_ranges, current_ranges[i]);
            } else {
                //log("PRE Current %, new current %", current_ranges[i], new_current_ranges);
                if added {
                    array_add_if_unique2(*new_current_ranges, current_ranges[i]);
                } else {
                    new_from = min(from, to_add_range.from.x);
                    while i < current_ranges.count && to_add_range.to.x >= current_ranges[i].x {
                        new_to = max(current_ranges[i].y, to_add_range.to.x);
                        i += 1;
                    }

                    array_add_if_unique2(*new_current_ranges, .{new_from, new_to});
                    added = true;
                    if i < current_ranges.count {
                        array_add_if_unique2(*new_current_ranges, current_ranges[i]);
                    }
                }
            }

            i += 1;
        }

    } else {
        array_add_if_unique2(*new_current_ranges, .{to_add_range.from.x, to_add_range.to.x});
    }
    return new_current_ranges;
}

line_value :: (current_ranges: [] Vector2i, edges: [] Range) -> u64 {
    // edge case: for lines when there are removals line value is different then previous or next
    // count it in a special way
    is_range_covered :: (current_ranges: [] Vector2i, r: Range) -> bool, Vector2i {
        for current_ranges if r.from.x >= it.x && r.to.x <= it.y return true, it;
        return false, .{};
    }

    is_range_touching :: (current_ranges: [] Vector2i, r: Range) -> bool, Vector2i {
        for current_ranges {
            if r.from.x == it.y || r.to.x == it.x return true, it;
        }
        return false, .{};
    }
    
    value :u64= 0;
    for current_ranges value += xx (it.y - it.x + 1);

    for edge: edges {
        // if it's covered don't add anything
        // [.......]
        //    [....]
        covered, range := is_range_covered(current_ranges, edge);
        //log("covered %, for % by %", covered, edge, range);
        if covered continue;
        
        touching, touching_range := is_range_touching(current_ranges, edge);
        // if not covered it can only be like this
        // [....]
        //    [.....]
        if touching {
            value += xx(edge.to.x - edge.from.x); // +1 -1
        } else {
            //log("not touching %", edge);
            value += xx(edge.to.x - edge.from.x + 1);
        }

    }
    return value;
}


merge_new_range_tests :: () {
    v :: (a: int, b: int) -> Vector2i {
        return Vector2i.{a, b};
    }

    r :: (from: int, to: int) -> Range {
        return .{.{from, 10}, .{to, 10}};
    }


    // add before overlapping just one
    assert(merge_new_range(.[v(1, 4), v(6, 8)], r(-1, 1)) == .[v(-1, 4), v(6, 8)]);
    assert(merge_new_range(.[v(1, 4), v(6, 8)], r(-1, 2)) == .[v(-1, 4), v(6, 8)]);
    assert(merge_new_range(.[v(1, 4), v(6, 8)], r(-1, 4)) == .[v(-1, 4), v(6, 8)]);
    // add middle overlapping just one
    assert(merge_new_range(.[v(1, 4), v(6, 8), v(10, 12)], r(5, 6)) == .[v(1, 4), v(5, 8), v(10, 12)]);
    assert(merge_new_range(.[v(1, 4), v(6, 8), v(10, 12)], r(5, 7)) == .[v(1, 4), v(5, 8), v(10, 12)]);
    assert(merge_new_range(.[v(1, 4), v(6, 8), v(10, 12)], r(5, 8)) == .[v(1, 4), v(5, 8), v(10, 12)]);
    // add before overlapping whole one, reaching next
    assert(merge_new_range(.[v(1, 4), v(6, 8), v(10, 12)], r(2, 11)) == .[v(1, 12)]);
    // add before non-overlapping
    assert(merge_new_range(.[v(1, 4), v(6, 8)], r(-2, -1)) == .[v(-2, -1), v(1, 4), v(6, 8)]);
    // add after non-overlapping
    assert(merge_new_range(.[v(1, 4), v(6, 8)], r(20, 23)) == .[v(1, 4), v(6, 8), v(20, 23)]);
    
    assert(merge_new_range(.[v(1, 4), v(6, 8), v(10, 12), v(14, 16), v(19, 22), v(25, 27), v(31, 35)], r(10, 22)) == .[v(1, 4), v(6, 8), v(10, 22), v(25, 27), v(31, 35)]);
    assert(merge_new_range(.[v(1, 4), v(6, 8), v(20, 23)], r(1, 8)) == .[v(1, 8), v(20, 23)]);
    // remove fully
    assert(merge_new_range(.[v(1, 4), v(6, 8)], r(1, 4)) == .[v(6, 8)]);
    // remove partial - split to two
    assert(merge_new_range(.[v(1, 7), v(8, 10)], r(2, 4)) == .[v(1, 2), v(4, 7), v(8, 10)]);
    // remove partial - just one
    assert(merge_new_range(.[v(1, 7), v(8, 10)], r(4, 7)) == .[v(1, 4), v(8, 10)]);
    assert(merge_new_range(.[v(1, 7), v(8, 10)], r(1, 2)) == .[v(2, 7), v(8, 10)]);
}

main :: () {
    log("============ Part 2 ============");
    merge_new_range_tests();
    part2();
}