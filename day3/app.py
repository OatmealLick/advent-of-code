def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"day3/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(lines)
        result = 0
        for i in range(0, len(lines), 3):

            s0 = set(lines[i + 0])
            s1 = set(lines[i + 1])
            s2 = set(lines[i + 2])
            common = s0.intersection(s1).intersection(s2)

            for common_character in common:
                num = ord(common_character)
                if num >= 97:
                    result += num - 96
                else:
                    result += num - 38
        print(result)


if __name__ == "__main__":
    main()
