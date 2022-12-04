import os
import sys

def main():
    with open("day1/src/first-input.txt", "r") as input:
        measurements = [x.strip() for x in input.readlines()]
        print(measurements)
        results = [0]
        for i in measurements:
            if i == "":
                results.append(0)
            else:
                results[-1] = results[-1] + int(i.strip())
        print(results)
        results = sorted(results)
        print(results[-1] + results[-2] + results[-3])



if __name__ == "__main__":
    main()