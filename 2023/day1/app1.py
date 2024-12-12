import os
import sys

def main():
    with open("first-input.txt", "r") as input:
        lines = [x.strip() for x in input.readlines()]
        nums = []
        for line in lines:
            first = -1
            last = -1
            for c in line:
                if not c.isdigit():
                    continue
                ascii = int(c)
                if first == -1:
                    first = ascii
                    last = ascii
                else:
                    last = ascii

            number = 10 * first + last
            nums.append(number)
        print(nums)
        print(sum(nums))



if __name__ == "__main__":
    main()
