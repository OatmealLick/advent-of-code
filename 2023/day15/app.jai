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

    strings := split(trim(file_contents), ",");

    res := 0;
    for strings {
        h := hash(it);
        res += h;
    }
    log("Res %", res);
}

hash :: (s: string) -> int {
    res := 0;
    for i: 0..s.count - 1 {
        res += s[i];
        res *= 17;
        res = res % 256;
    }
    return res;
}

Thing :: struct {
    label: string;
    focal_length: int;
}

operator == :: (a: Thing, b: Thing) -> bool {
    return a.label == b.label && a.focal_length == b.focal_length;
}


part2 :: () {
    file_contents, ok := read_entire_file(FILENAME);
    if !ok {
        log("File % not found", FILENAME);
        return;
    }

    strings := split(trim(file_contents), ",");
    buckets: [256] [..] Thing;

    for strings {
        if contains(it, "=") {
            parts := split(it, "=");
            t := Thing.{parts[0], string_to_int(parts[1])};
            h := hash(parts[0]);
            bucket := buckets[h];
            log("fake: [%] %, %", bucket.count, bucket, bucket.data);
            log("real: [%] %, %", buckets[h].count, buckets[h], buckets[h].data);
            found := false;
            for * buckets[h] if it.label == t.label {
                it.focal_length = t.focal_length;
                //buckets[h] = bucket;
                found = true;
                break;
            }
            if !found {
                array_add(*buckets[h], t);
                //buckets[h] = bucket;
            }
        } else {
            to_remove_label := split(it, "-")[0];
            h := hash(to_remove_label);
            //bucket := buckets[h];
            to_remove: int = -1;
            for buckets[h] if it.label == to_remove_label to_remove = it_index;
            if to_remove != -1 array_ordered_remove_by_index(*buckets[h], to_remove);
            //buckets[h] = bucket;
        }

        //for buckets if it.count != 0 log("Bucket [%] %", it_index, it);
        //log("\n");
    }
    res := 0;
    for bucket_index: 0..buckets.count - 1 {
        bucket := buckets[bucket_index];
        for slot_index: 0..bucket.count - 1 {
            thing := bucket[slot_index];
            line_res := (bucket_index + 1) * (slot_index + 1) * thing.focal_length;
            res += line_res;
        }
    }
    log("Res %", res);
}


main :: () {
    log("============ Part 1 ============");
    part1();
    log("============ Part 2 ============");
    part2();
}