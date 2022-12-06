def parse_input_file(file_path):
    with open(file_path, "r") as input_file:
        # Read the file line by line
        lines = input_file.readlines()
        return parse_input(lines)


def parse_input(input):
  elves = []
  current_elf_calories = []
  for line in input:
    if line.strip() == '':
      # Add the current elf's calories to the list of elves
      elves.append(current_elf_calories)
      current_elf_calories = []
    else:
      # Parse the calorie count and add it to the current elf's list of calories
      current_elf_calories.append(int(line))
  # Add the last elf's calories to the list of elves
  elves.append(current_elf_calories)

  return elves

def find_elf_with_most_calories(elves):
  max_calories = 0
  max_calorie_elf = None
  for elf in elves:
    # Calculate the total number of calories for the current elf
    total_calories = sum(elf)
    if total_calories > max_calories:
      # Update the max calories and the elf with the most calories
      max_calories = total_calories
      max_calorie_elf = elf

  return max_calories


file_input = parse_input_file("/Users/lukaszsciga/projects/advent-of-code-2022/day1/first-input.txt")
a = find_elf_with_most_calories(file_input)
print(a)