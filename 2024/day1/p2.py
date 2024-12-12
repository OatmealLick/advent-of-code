from collections import defaultdict, Counter


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

  c = Counter(right)

  diffs = 0
  for i in range(len(left)):
    diffs += c[left[i]] * left[i]

  return diffs

if __name__ == "__main__":
    main()
