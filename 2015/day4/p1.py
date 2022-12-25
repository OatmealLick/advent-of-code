from functools import reduce
from collections import defaultdict
from hashlib import md5

def main():
    print(solve("iwrupvqb"))


def solve(key):
    hashes = [(i, md5(f"{key}{i}".encode()).hexdigest()[:5]) for i in range(999999)]
    return min(filter(lambda x: x[1] == "00000", hashes))[0]


if __name__ == "__main__":
    main()
