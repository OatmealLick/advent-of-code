#import "Basic";
#import "String";
#import "File";
#import "Hash_Table";
#import "Math";
#import "Sort";
#import "Hash";

FILENAME :: "input.txt";
//FILENAME :: "sample.txt";

Vector2i :: struct {
    x: int;
    y: int;
}

hash_function :: (a: Vector2i) -> u32 {
    ax := a.x + 2;
    ay := a.y + 2;
    return cast(u32) (31 * ax + ay);
}

compare_function :: (a: Vector2i, b: Vector2i) -> bool {
    return a.x == b.x && a.y == b.y;
}

Ray :: struct {
    position: Vector2i;
    direction: Vector2i;
}

ray_hash_function :: (a: Ray) -> u32 {

    return cast(u32) (hash_function(a.direction) * 17 + hash_function(a.position));
}

ray_compare_function :: (a: Ray, b: Ray) -> bool {
    return compare_function(a.direction, b.direction) && compare_function(a.position, b.position);
}

part1 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(trim(file_contents), "\r\n");
    width := lines[0].count;
    height := lines.count;

    direction := Vector2i.{1, 0};
    position := Vector2i.{-1, 0};
    energized: Table(Vector2i, bool, given_hash_function=hash_function, given_compare_function=compare_function);

    rays: [..] Ray;
    array_add(*rays, .{position, direction});

    steps_to_stop_after_if_no_change := 100;
    steps := 0;
    current_energized := 0;

    cache: Table(Ray, bool, given_hash_function=ray_hash_function, given_compare_function=ray_compare_function);

    while rays.count != 0 {
        to_remove_indices: [..] int;
        to_add_rays: [..] Ray;
        for i: 0..rays.count - 1 {
            using ray := *rays[i];
            position.x += direction.x;
            position.y += direction.y;
            if position.x < 0 || position.x >= width || position.y < 0 || position.y >= height {
                array_add(*to_remove_indices, i);
                continue;
            }

            table_set(*energized, position, true);
            if table_contains(*cache, ray) {
                array_add(*to_remove_indices, i);
                continue;
            } else {
                table_set(*cache, ray, true);
            }

            is_split, new_direction, split_direction := to_direction(lines[position.y][position.x], direction);
            ray.direction = new_direction;
            if is_split array_add(*to_add_rays, .{position, split_direction});
        }

        for < to_remove_indices {
            array_ordered_remove_by_index(*rays, it);
        }

        for to_add_rays {
            array_add(*rays, it);
        }

        new_current_energized := energized.count;
        if new_current_energized == current_energized {
            steps += 1;
            if steps >= steps_to_stop_after_if_no_change {
                break;
            }
        } else {
            steps = 0;
            current_energized = new_current_energized;
        }
    }

    log("res: %", energized.count);
}

print_energized :: (energized: *Table, width: int, height: int) {
    for y: 0..height - 1 {
        for x: 0..width - 1 {
            if table_contains(energized, .{x, y}) {
                print("#");
            } else {
                print(".");
            }
        }
        print("\n");
    }
}

// if true then split and should consider second direction
to_direction :: (c: u8, old_direction: Vector2i) -> bool, Vector2i, Vector2i {
    if c == #char "." return false, old_direction, .{};
    if c == #char "/" {
        if old_direction.x == 1 return false, .{0, -1}, .{};
        if old_direction.x == -1 return false, .{0, 1}, .{};
        if old_direction.y == 1 return false, .{-1, 0}, .{};
        return false, .{1, 0}, .{};
    }
    if c == #char "\\" {
        if old_direction.x == 1 return false, .{0, 1}, .{};
        if old_direction.x == -1 return false, .{0, -1}, .{};
        if old_direction.y == 1 return false, .{1, 0}, .{};
        return false, .{-1, 0}, .{};
    }
    if c == #char "-" {
        if old_direction.x == 1 || old_direction.x == -1 return false, old_direction, .{};
        return true, .{1, 0}, .{-1, 0};
    }
    //if c == #char "|" {
    else {
        if old_direction.y == 1 || old_direction.y == -1 return false, old_direction, .{};
        return true, .{0, 1}, .{0, -1};
    }
}

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(trim(file_contents), "\r\n");
    width := lines[0].count;
    height := lines.count;

    starting_rays: [..] Ray;
    for 0..height - 1 array_add(*starting_rays, .{direction=.{1, 0}, position=.{-1, it}});
    for 0..height - 1 array_add(*starting_rays, .{direction=.{-1, 0}, position=.{width, it}});
    for 0..width - 1 array_add(*starting_rays, .{direction=.{0, 1}, position=.{it, -1}});
    for 0..width - 1 array_add(*starting_rays, .{direction=.{0, -1}, position=.{it, height}});

    max_energized := 0;
    for starting_rays {
        direction := it.direction;
        position := it.position;
        energized: Table(Vector2i, bool, given_hash_function=hash_function, given_compare_function=compare_function);

        rays: [..] Ray;
        array_add(*rays, .{position, direction});

        steps_to_stop_after_if_no_change := 100;
        steps := 0;
        current_energized := 0;

        cache: Table(Ray, bool, given_hash_function=ray_hash_function, given_compare_function=ray_compare_function);

        while rays.count != 0 {
            to_remove_indices: [..] int;
            to_add_rays: [..] Ray;
            for i: 0..rays.count - 1 {
                using ray := *rays[i];
                position.x += direction.x;
                position.y += direction.y;
                if position.x < 0 || position.x >= width || position.y < 0 || position.y >= height {
                    array_add(*to_remove_indices, i);
                    continue;
                }

                table_set(*energized, position, true);
                if table_contains(*cache, ray) {
                    array_add(*to_remove_indices, i);
                    continue;
                } else {
                    table_set(*cache, ray, true);
                }

                is_split, new_direction, split_direction := to_direction(lines[position.y][position.x], direction);
                ray.direction = new_direction;
                if is_split array_add(*to_add_rays, .{position, split_direction});
            }

            for < to_remove_indices {
                array_ordered_remove_by_index(*rays, it);
            }

            for to_add_rays {
                array_add(*rays, it);
            }

            new_current_energized := energized.count;
            if new_current_energized == current_energized {
                steps += 1;
                if steps >= steps_to_stop_after_if_no_change {
                    break;
                }
            } else {
                steps = 0;
                current_energized = new_current_energized;
            }
        }

        log("[%] current %, max %", it_index, current_energized, max_energized);
        max_energized = max(max_energized, current_energized);

    }

    log("res: %", max_energized);
}


main :: () {
    log("============ Part 1 ============");
    part1();
    log("============ Part 2 ============");
    part2();
}