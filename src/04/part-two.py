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

    total_lines = len(lines)
    total_card_count = 0

    copy_stack = [0] * total_lines

    for i, line in enumerate(lines):
        if i >= total_lines:
            break

        card_count = 1 + copy_stack.pop(0)
        total_card_count += card_count

        N, M = line_to_sets(line)
        W = N.intersection(M)
        W_len = len(W)

        if W_len == 0:
            continue

        for i in range(W_len):
            if i == len(copy_stack):
                break
            copy_stack[i] += card_count

    print("Total cards:", total_card_count)


if __name__ == "__main__":
    main()
