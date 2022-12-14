def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    buffer = []
    unique_characters_required = 14
    with open(f"day6/{filename}", "r") as f:
        lines = [x for x in f.readlines()][0]
        print(lines)

        for i, char in enumerate(lines):

            if i < unique_characters_required:
                buffer.append(char)
                continue
            else:
                if len(set(buffer)) == unique_characters_required:
                    print(i)
                    break
                else:
                    buffer.pop(0)
                    buffer.append(char)


if __name__ == "__main__":
    main()
