import math
from collections import defaultdict
from itertools import permutations

def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day19/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    res = 0
    for l in lines:
        ps = [int(s) for s in l.split() if s.isdigit()]
        # ints
        _, or_cost, cr_cost, obsr_o_cost, obsr_c_cost, geor_o_cost, geor_obs_cost = ps
        b_res = analyze_blueprint(or_cost, cr_cost, obsr_o_cost, obsr_c_cost, geor_o_cost, geor_obs_cost)
        # modify res somehow
        res = b_res
    return res

def analyze_blueprint(or_cost, cr_cost, obsr_o_cost, obsr_c_cost, geor_o_cost, geor_obs_cost):
    res = 0
    time = 24

    ors = 0
    crs = 0
    obsrs = 0
    geors = 0

    o = 0
    c = 0
    obs = 0
    geo = 0

    while time > 0:
        # if can build geo
            #build geo
        # else
            # is wait for geo shorter than build obs?
                # wait for geo
            # try to make obs 
                # can build obs?
                    # build obs
                # else
                    # is wait for obs shorter than build clay?
                        # wait for obs
                    # try to make clay
                        # can build clay?
                            # build clay
            

        time -= 1
    return geo

def neighbours(c, cubes):
    cx, cy, cz = c
    candidates = [
        (cx + 1, cy, cz),
        (cx - 1, cy, cz),
        (cx, cy + 1, cz),
        (cx, cy - 1, cz),
        (cx, cy, cz + 1),
        (cx, cy, cz - 1),
    ]
    return [ca for ca in candidates if ca in cubes]


if __name__ == "__main__":
    main()
