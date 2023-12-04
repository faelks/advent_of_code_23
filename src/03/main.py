from pathlib import Path


def read_file(filename: str):
    """Read the provided filename and return a list of lines"""
    path = Path(__file__).with_name(filename)
    file = path.open("r")

    return [line.strip() for line in file]


def adjacent_col_indices(col_indices: list[int], max_index: int):
    """Return a list of adjacent indices"""
    first = col_indices[0]
    before_first = max(first - 1, 0)
    last = col_indices[-1]
    after_last = min(last + 1, max_index)

    return [
        [before_first, *col_indices, after_last],
        [before_first, after_last],
        [before_first, *col_indices, after_last],
    ]


def is_symbol(char: str):
    """Return a boolean whether the char is a symbol"""
    return not char.isnumeric() and char != "."


def main():
    print("Advent of code 03")

    filename = "input.txt"
    lines = read_file(filename)

    gears = {}

    max_index = len(lines[0]) - 1
    part_sum = 0
    for row, line in enumerate(lines):
        indices: list[int] = []
        number = ""

        for col, char in enumerate(line):
            if char.isnumeric():
                number += char
                indices.append(col)

            if char == "*":
                gears[(row, col)] = []

            if (
                char.isnumeric()
                and col == len(line) - 1
                or not char.isnumeric()
                and number
            ):
                prev_line = lines[row - 1] if row > 0 else None
                next_line = lines[row + 1] if row < len(lines) - 1 else None

                [prev, cur, next] = adjacent_col_indices(indices, max_index)
                current_number = int(number)

                for col_p in prev:
                    row_col = (row, col_p)
                    if row_col in gears and current_number not in gears[row_col]:
                        gears[row_col].append(current_number)

                for col_c in cur:
                    row_col = (row, col_c)
                    if row_col in gears and current_number not in gears[row_col]:
                        gears[row_col].append(current_number)

                for col_n in next:
                    row_col = (row, col_n)
                    if row_col in gears and current_number not in gears[row_col]:
                        gears[row_col].append(current_number)

                number = ""
                indices = []

                if prev_line and any(is_symbol(prev_line[i]) for i in prev):
                    part_sum += current_number
                    continue

                if next_line and any(is_symbol(next_line[i]) for i in next):
                    part_sum += current_number
                    continue

                if any(is_symbol(line[i]) for i in cur):
                    part_sum += current_number
                    continue

    gears_with_two = [v for v in gears.values() if len(v) == 2]
    gear_products = [v[0] * v[1] for v in gears_with_two]
    gear_sum = sum(gear_products)

    print(gears_with_two)
    print(gear_products)

    print(f"Sum: {part_sum}")
    print(f"Gear sum: {gear_sum}")


if __name__ == "__main__":
    main()
