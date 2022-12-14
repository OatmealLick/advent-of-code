import functools


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day13/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        part1_result = part1(lines[:])
        print(part1_result)
        part2_result = part2(lines[:])
        print(part2_result)


def part1(lines):
    counter = 1
    result = 0
    for i in range(0, len(lines), 3):
        left = eval(lines[i])
        right = eval(lines[i+1])
        if_are = are_inputs_in_right_order(left, right)
        if if_are:
            print(f"Right order: {counter}")
            result += counter
        counter += 1
    return result


def are_inputs_in_right_order(left, right):
    if left and not right:  # left has items but right not
        return False
    elif not left and right:  # left has no items but right has
        return True
    elif not left and not right:
        return None

    for i in range(max(len(left), len(right))):
        if i >= len(left):
            return True
        elif i >= len(right):
            return False

        l = left[i]
        r = right[i]

        if type(l) == list and type(r) == list:
            subcall = are_inputs_in_right_order(l, r)
            if subcall is not None:
                return subcall
        elif type(l) == list and type(r) != list:
            subcall = are_inputs_in_right_order(l, [r])
            if subcall is not None:
                return subcall
        elif type(l) != list and type(r) == list:
            subcall = are_inputs_in_right_order([l], r)
            if subcall is not None:
                return subcall
        else:
            if l < r:
                return True
            elif l > r:
                return False
    return None


def part2(lines):
    counter = 1
    result = 0
    packets = [[[2]], [[6]]]
    for i in range(0, len(lines), 3):
        left = eval(lines[i])
        right = eval(lines[i+1])
        packets.append(left)
        packets.append(right)
    packets.sort(key=functools.cmp_to_key(custom_sort))
    i2 = packets.index([[2]]) + 1
    i6 = packets.index([[6]]) + 1
    print(i2, i6)
    return i2 * i6


def custom_sort(left, right):
    order = are_inputs_in_right_order(left, right)
    if order is None:
        return 0
    elif order:
        return -1
    else:
        return 1


if __name__ == "__main__":
    main()
