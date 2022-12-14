
def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"day2/{filename}", "r") as f:
        measurements = [x.strip() for x in f.readlines()]
        print(measurements)
        result = 0
        for m in measurements:
            parts = m.split(" ")
            op = ord(parts[0]) - 65
            you = ord(parts[1]) - 88
            print(op, you)
            
            # update your score to match the expected result (added in part2)
            if you == 0:
                if op == 0:
                    you = 2
                else:
                    you = op - 1
            elif you == 1:
                you = op
            else:
                if op == 2:
                    you = 0
                else:
                    you = op + 1

            # count the result in proper way (part 1)
            if op == you:
                result += you + 1 + 3
            elif (op == 0 and you == 2) or (op - you == 1):
                result += you + 1
            else:
                result += you + 1 + 6
            print(result)
        print(result)


if __name__ == "__main__":
    main()
