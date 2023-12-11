from pathlib import Path


def read_file(filename: str):
    """Read the provided filename and return a list of lines"""
    path = Path(__file__).with_name(filename)
    file = path.open("r")

    return [line.strip() for line in file]


def line_to_sets(line: str):
    """Parse line into sets N and M"""
    line = line.split(":")[1]
    [line_n, line_m] = line.split("|")
    N = {int(n) for n in line_n.strip().split()}
    M = {int(m) for m in line_m.strip().split()}

    return N, M


def main():
    print("Advent of code 04")

    filename = "input.txt"
    # filename = "test-1.txt"
    lines = read_file(filename)

    sum = 0
    for line in lines:
        N, M = line_to_sets(line)
        W = N.intersection(M)
        W_len = len(W)

        result = 0 if W_len == 0 else 2 ** (W_len - 1)
        sum += result

    print("Sum:", sum)


if __name__ == "__main__":
    main()
