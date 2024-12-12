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


  def do_is_safe(level: list[int]) -> bool:
    print(f"{level}")
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
  
  def is_safe(level: list[int]) -> bool:
    for i in range(len(level)):
      new_level = level[:i] + level[i + 1:]
      print(f"  {new_level}")
      safe = do_is_safe(new_level)
      if safe:
        return True
    return False

  c = 0
  #for x in reports[:3]:
  for x in reports:
    safe = is_safe(x)
    print(f"Report {x} is safe: {safe}")
    if safe:
      c += 1
  return c

if __name__ == "__main__":
    main()
