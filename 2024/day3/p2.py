def main():
  filename = "input.txt"
  #filename = "input-sample.txt"
  with open(f"2024/day3/{filename}", "r") as f:
    lines = [x for x in f.readlines()]
    print(solve(lines[:]))

def handle_line(line):
  state = 0
  muls = 0
  left = []
  right = []
  enabled = True

  i = 0
  while i < len(line):
    if not enabled:
      ca = line[i:i+4]
      if ca == "do()":
        enabled = True
        i += 4
        continue
      else:
        i += 1
        continue
    else:
      if i < len(line) - 7 and line[i:i+7] == "don't()":
        enabled = False
        i += 7
        continue

    if state == 0:
      candidate = line[i:i+4]
      if candidate == 'mul(': # )
        print("opening")
        state = 1
        i += 4
        continue
      else:
        i += 1
    elif state == 1:
      c = line[i]
      if c.isdigit():
        print("l digit")
        left.append(c)
        state = 2
      else:
        state = 0
        left = []
        right = []
      i += 1
    elif state == 2:
      c = line[i]
      if c.isdigit():
        print("l digit 2")
        left.append(c)
      elif c == ',':
        print("comma")
        state = 3
      else:
        state = 0
        left = []
        right = []
      i += 1
    elif state == 3:
      c = line[i]
      if c.isdigit():
        right.append(c)
        state = 4
        print("r digit")
      else:
        state = 0
        left = []
        right = []
      i += 1
    elif state == 4:
      c = line[i]
      if c.isdigit():
        right.append(c)
        print("r digit 2")
      elif c == ')':
        ll = int("".join(left))
        rr = int("".join(right))
        print(f"found {ll} and {rr}")
        muls += ll * rr
        state = 0
        left = []
        right = []
      else:
        state = 0
        left = []
        right = []
      i += 1
  return muls


def solve(lines):
  #line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
  s = 0
  line = "".join([l.strip() for l in lines])
  s += handle_line(line)
  return s


if __name__ == "__main__":
  main()

OPENING = "mul("

