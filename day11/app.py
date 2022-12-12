import math
from collections import defaultdict

class Monkey:
    def __init__(self, items, operation, test, mod=-1) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.mod = mod
    
    def __str__(self) -> str:
        return f"{self.items}"
    
    def __repr__(self) -> str:
        return str(self)

def main():
    part1_result = part1(create_monkeys())
    print(part1_result)
    part2_result = part2(create_monkeys())
    print(part2_result)

def create_monkeys_sample():
    monkeys = {}
    monkeys[0] = Monkey([79, 98], lambda x: x * 19, lambda x: 2 if x % 23 == 0 else 3, 23)
    monkeys[1] = Monkey([54, 65, 75, 74], lambda x: x + 6, lambda x: 2 if x % 19 == 0 else 0, 19)
    monkeys[2] = Monkey([79, 60, 97], lambda x: x * x, lambda x: 1 if x % 13 == 0 else 3, 13)
    monkeys[3] = Monkey([74], lambda x: x + 3, lambda x: 0 if x % 17 == 0 else 1, 17)
    return monkeys

def create_monkeys():
    monkeys = {}
    monkeys[0] = Monkey([66, 59, 64, 51], lambda x: x * 3, lambda x: 1 if x % 2 == 0 else 4, 2)
    monkeys[1] = Monkey([67, 61], lambda x: x * 19, lambda x: 3 if x % 7 == 0 else 5, 7)
    monkeys[2] = Monkey([86, 93, 80, 70, 71, 81, 56], lambda x: x + 2, lambda x: 4 if x % 11 == 0 else 0, 11)
    monkeys[3] = Monkey([94], lambda x: x * x, lambda x: 7 if x % 19 == 0 else 6, 19)
    monkeys[4] = Monkey([71, 92, 64], lambda x: x + 8, lambda x: 5 if x % 3 == 0 else 1, 3)
    monkeys[5] = Monkey([58, 81, 92, 75, 56], lambda x: x + 6, lambda x: 3 if x % 5 == 0 else 6, 5)
    monkeys[6] = Monkey([82, 98, 77, 94, 86, 81], lambda x: x + 7, lambda x: 7 if x % 17 == 0 else 2, 17)
    monkeys[7] = Monkey([54, 95, 70, 93, 88, 93, 63, 50], lambda x: x + 4, lambda x: 2 if x % 13 == 0 else 0, 13)
    return monkeys
    
def part1(monkeys):
    ROUNDS = 20
    inspections = defaultdict(int)
    for r in range(ROUNDS):
        print(f"Round {r}, monkeys {monkeys}")
        for monkey_num, monkey in monkeys.items():
            for item in monkey.items:
                new_worry = monkey.operation(item)
                inspections[monkey_num] += 1
                lowered_worry = math.floor(new_worry / 3)
                # print(f"Monkey {monkey_num} item {item} {new_worry} {lowered_worry}")
                monkey_to_receive = monkey.test(lowered_worry)
                monkeys[monkey_to_receive].items.append(lowered_worry)
            monkey.items = []
    inspections_sorted = sorted(inspections.values())
    print(inspections_sorted)
    return inspections_sorted[-1] * inspections_sorted[-2]

def part2(monkeys):
    ROUNDS = 10000
    MAX_NEEDED = 2 * 7 * 11 * 19 * 3 * 5 * 17 * 13
    # MAX_NEEDED = 23 * 19 * 13 * 17

    inspections = defaultdict(int)
    for _ in range(ROUNDS):
        for monkey_num, monkey in monkeys.items():
            for item in monkey.items:
                new_worry = monkey.operation(item)
                inspections[monkey_num] += 1
                rest = new_worry % MAX_NEEDED
                lowered_worry = rest
                monkey_to_receive = monkey.test(lowered_worry)
                monkeys[monkey_to_receive].items.append(lowered_worry)
            monkey.items = []
    inspections_sorted = sorted(inspections.values())
    print(inspections_sorted)
    print(sum(inspections_sorted))
    return inspections_sorted[-1] * inspections_sorted[-2]


if __name__ == "__main__":
    main()
