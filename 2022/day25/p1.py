
power_of_fives = {i: pow(5, i) for i in range(25)}

def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2022/day25/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    print(from_snafu("1=-0-2"))
    print(to_snafu("2022"))
    print(to_snafu("1747"))
    print(to_snafu("10"))
    print(to_snafu("8"))

    res = 0
    for l in lines:
        res += from_snafu(l)
    return to_snafu(res)


def to_snafu(x):
    x = int(x)

    parts = {
        -2: "=",
        -1: "-",
        0: "0",
        1: "1",
        2: "2"
    }

    res = []
    add = 0
    while x > 0 or add != 0:
        r = (x % 5) + add
        if r >= 3:
            rr = r - 5
            add = 1
        else:
            rr = r
            add = 0
        res.append(parts[rr])
        x //= 5
    
    return "".join(res[::-1])
        
        #  2 =  2
        #  3 = 1=
        #  4 = 1-
        #  5 = 10
        #  6 = 11
        #  7 = 12
        #  8 = 2=
        #  9 = 2-
        # 10 = 20
        # 11 = 21
        # 12 = 22
        # 13 = 1==

        # 7%5 = 2 . 


        #  4  3  2  1  0
        # -1 -2  


def from_snafu(x):
    res = 0
    for i, x in enumerate(str(x)[::-1]):
        if x == "-":
            digit = -1
        elif x == "=":
            digit = -2
        else:
            digit = int(x)
        res += power_of_fives[i] * digit
    return res





if __name__ == "__main__":
    main()