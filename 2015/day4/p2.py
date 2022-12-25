from functools import reduce
from collections import defaultdict
from hashlib import md5

def main():
    print(solve("iwrupvqb"))


def solve(key):
    hashes = [(i, md5(f"{key}{i}".encode()).hexdigest()[:6]) for i in range(9999999)]
    return min(filter(lambda x: x[1] == "000000", hashes))[0]


if __name__ == "__main__":
    main()
