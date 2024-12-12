from collections import defaultdict


def main():
    filename = "input.txt"
    #filename = "input-sample.txt"
    with open(f"2024/day2/{filename}", "r") as f:
        lines = [x for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
  reports = []
  for line in lines:
    levels = [int(x) for x in line.split(" ")]
    reports.append(levels)

  def is_safe(level: list[int]) -> bool:
    should_increasing = level[0] < level[1]
    for i in range(0, len(level) - 1):
      x = level[i]
      nx = level[i + 1]
      if x > nx and should_increasing:
        return False
      if x < nx and not should_increasing:
        return False
      diff = abs(x - nx)
      if diff > 3 or diff < 1:
        return False
    return True
      
  c = 0
  for x in reports:
    safe = is_safe(x)
    print(f"Report {x} is safe: {safe}")
    if safe:
      c += 1
  # safe_levels = [x for x in reports if is_safe(x)]
  return c

if __name__ == "__main__":
    main()
