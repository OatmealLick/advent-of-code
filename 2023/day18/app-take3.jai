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

hex_char_to_u32 :: (c : u8) -> u32 {
    if c >= #char "a" return xx(c - #char "a" + 0xa);
    if c >= #char "0" return xx(c - #char "0");
    return 1;
}

polygon_area :: (p: [] Vector2i) -> int {
    res: int = 0;
    for p {
        x_next := p[(it_index + 1) % p.count].x;
        y_next := p[(it_index + 1) % p.count].y;

        res += (cast(int) (it.x) * cast(int) y_next) - (cast(int) (it.y) * cast(int) x_next);
    }

    return xx (res / 2);
}

boundary_points :: (p: [] Vector2i) -> int {
    res: = 0;
    for p {
        x_next := p[(it_index + 1) % p.count].x;
        y_next := p[(it_index + 1) % p.count].y;

        if it.x == x_next {
            res += abs(it.y - y_next);
        } else {
            res += abs(it.x - x_next);
        }
    }
    return res;
}

inside_points :: (boundary_points: int, area: int) -> int {
    return area - (boundary_points / 2) + 1;
}

part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    lines := split(trim(file_contents), "\r\n");

    position := Vector2i.{0, 0};
    points: [..] Vector2i;

    for lines {
        array_add(*points, position);
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
        
        position = new_position;
    }

    // APPARENTLY by having a list of coordinates of polygon you can compute its area (Shoelace formula)
    // MIND YOU it's not what we want though. Area != number of points in and out covered by polygon
    // IT SO HAPPENS that there is also Pick theorem that from boundary points and inside points number can COMPUTE area
    // TRIVIALLY, what follows is some algebraic machinations to use area you have from shoelace and boom, that's it.
    area := polygon_area(points);
    b_points := boundary_points(points);
    i_points := inside_points(b_points, area);
    res := b_points + i_points;
    log("Res: %", res);
}


main :: () {
    log("============ Tests =============");
    // Leaving it here as the testament of frustration building up 
    p: [] Vector2i = .[.{0, 0}, .{5, 0}, .{5, 6}, .{0, 6}];
    a := polygon_area(p);
    log("AKSJDLAKJSD %", a);
    log("============ Part 2 ============");

    part2();
}