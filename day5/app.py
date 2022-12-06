def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    stacks = {}
    with open(f"day5/{filename}", "r") as f:
        lines = [x for x in f.readlines()]
        print(lines)
        parsing_stacks = True
        for line in lines:
            if parsing_stacks:

                if line == "\n":
                    parsing_stacks = False
                    for key in stacks.keys():
                        stacks[key].reverse()
                    print(stacks)
                    continue

                for i in range(0, len(line) - 1, 4):
                    key = i // 4;
                    print(line[i + 1])
                    if line[i + 1] != " " and ord(line[i + 1]) < 65:
                        break
                    if line[i + 1] != " ":
                        if key in stacks:
                            stacks[key].append(line[i + 1])
                        else:
                            stacks[key] = [line[i + 1]]

                print(stacks)
            else:
                parts = line.strip().split(" ")
                what = int(parts[1])
                from_where = int(parts[3]) - 1
                to_where = int(parts[5]) - 1
                print(what, from_where, to_where)
                elements = (stacks[from_where])[-what:]
                # elements.reverse()
                stacks[to_where] += elements
                stacks[from_where] = stacks[from_where][:-what]
                print(stacks)

        keys_sorted = sorted(stacks.keys())
        res = [stacks[k][-1] for k in keys_sorted]
        print("".join(res))


if __name__ == "__main__":
    main()
