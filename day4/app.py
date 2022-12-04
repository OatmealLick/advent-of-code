def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    result = 0
    with open(f"day4/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(lines)
        for line in lines:
            ranges = line.split(",")
            range_0_start, range_0_end = _split_range(ranges[0])
            range_1_start, range_1_end = _split_range(ranges[1])
            print(range_0_start, range_0_end, range_1_start, range_1_end)
            if range_0_start <= range_1_end and range_0_end >= range_1_start:
                result += 1

        print(result)


def _split_range(the_range):
    parts = the_range.split("-")
    return int(parts[0]), int(parts[1])


if __name__ == "__main__":
    main()
