from collections import defaultdict


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2024/day1/{filename}", "r") as f:
        lines = [x for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
  left = []
  right = []
  for line in lines:
    l, r = line.split("   ")
    left.append(int(l.strip()))
    right.append(int(r.strip()))

  left.sort()
  right.sort()

  diffs = 0
  for i in range(len(left)):
    diffs += abs(left[i] - right[i])

  return diffs

if __name__ == "__main__":
    main()
