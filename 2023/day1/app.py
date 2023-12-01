import os
import sys

str2num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5, 
    "six": 6, 
    "seven": 7,
    "eight": 8, 
    "nine": 9,
}

def main():
    with open("first-input.txt", "r") as input:
        lines = [x.strip() for x in input.readlines()]
        nums = []
        for line in lines:
            first = -1
            last = -1
            for i, c in enumerate(line):
                (ok, value) = is_num("".join(line[i:]))
                if c.isdigit():
                    ascii = int(c)
                    if first == -1:
                        first = ascii
                    last = ascii
                elif ok:
                    ascii = value
                    if first == -1:
                        first = ascii
                    last = ascii
            
            number = 10 * first + last
            nums.append(number)
        print(nums)
        print(sum(nums))

def is_num(s):
    for k, v in str2num.items():
        if s.startswith(k):
            print(k)
            return (True, v)
    return (False, -1)



if __name__ == "__main__":
    main()
