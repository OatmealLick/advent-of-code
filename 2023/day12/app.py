def count_valid(line, nums, index_line=0, aggregating_damaged=False, damaged=0, index_nums=0):
    # print(line, index_line)
    if index_line == len(line):
        return 1
    current_char = line[index_line]
    if current_char in [".", "#"]:
        valid, aggregating_damaged, damaged, index_nums = validate_current(line, nums, index_line, aggregating_damaged, damaged, index_nums)
        if not valid:
            return 0
        else:
            return count_valid(line, nums, index_line + 1, aggregating_damaged, damaged, index_nums)
    else:
        a = line[:index_line] + "." + line[index_line + 1:]
        a_result = count_valid(a, nums, index_line, aggregating_damaged, damaged, index_nums)
        b = line[:index_line] + "#" + line[index_line + 1:]
        b_result = count_valid(b, nums, index_line, aggregating_damaged, damaged, index_nums)
        return a_result + b_result


def validate_current(line, nums, index_line, aggregating_damaged, damaged, index_nums):
    # todo optimization - keep the validation process and do not repeat it
    # aggregating_damaged = False
    # damaged = 0
    # index_nums = 0
    for i in range(index_line, index_line + 1):
        current_char = line[i]
        if current_char == "#":
            aggregating_damaged = True
            damaged += 1
        else:
            if aggregating_damaged:
                if index_nums >= len(nums) or damaged != nums[index_nums]:
                    return False, False, -1, -1

                aggregating_damaged = False
                damaged = 0
                index_nums += 1
    
    # if validating full line make sure that all damaged are included
    if index_line == len(line) - 1:
        # handle the case when # is in the end
        if aggregating_damaged:
            if index_nums >= len(nums) or damaged != nums[index_nums]:
                return False, False, -1, -1
            index_nums += 1
        return index_nums == len(nums), False, -1, -1
    
    return True, aggregating_damaged, damaged, index_nums


# come back for part2
# state: 
# optimized greedy / brute force algorithm, keeping the state of the line
# checking only valid combinations and discarding them as soon as possible

# too slow especially for long lines with no '.'

def run():
    # lines = open("sample.txt", "r").readlines()
    # lines = open("sample2.txt", "r").readlines() # no ambiguity
    lines = open("input.txt", "r").readlines()
    result = 0
    part2 = True
    for l in lines:
        parts = l.split(" ")
        line = parts[0]
        nums = [int(n) for n in parts[1].split(",")]
        if part2:
            valid = count_valid(line[:], nums[:])
            valid2 = count_valid_times(line[:], nums[:], 2)
            valid3 = count_valid_times(line[:], nums[:], 3)
            valid4 = count_valid_times(line[:], nums[:], 4)
            times = valid2 // valid
            # if abs(times - (valid_new / valid)) > 0.0001:
            #     print("ERROR", times, valid, valid_new)
            line_result = valid * (times ** 4)
            #print(line, valid, valid_new, times, line_result)
            print(valid, valid2, valid3, valid4, line_result)
            result += line_result

    print(result)

def count_valid_times(line, nums, times):
    # print("line", line, "nums", nums)
    new_line = line
    for i in range(times - 1):
        new_line += "?" + line
    nums = nums * times
    # print("AFTER line", new_line, "nums", nums)
    return count_valid(new_line, nums)


if __name__ == "__main__":
    run()
