from pathlib import Path

GEAR_SYMBOL = "*"


def read_file(filename: str):
    """Read the provided filename and return a list of lines"""
    path = Path(__file__).with_name(filename)
    file = path.open("r")

    return [line.strip() for line in file]


def main():
    print("Advent of code 03")

    filename = "input.txt"
    # filename = "test-1.txt"
    lines = read_file(filename)

    gears = {}
    rows = len(lines)
    cols = len(lines[0])
    max_row_index = rows - 1
    max_col_index = cols - 1

    print(f"Received matrix of: {rows} x {cols}")

    for row, line in enumerate(lines):
        number_indices: list[int] = []
        number = ""

        # Process the subsequent row to be able to add to gears
        if row < max_row_index:
            for col, char in enumerate(lines[row + 1]):
                pos = (row + 1, col)
                if char == GEAR_SYMBOL:
                    gears[pos] = []

        for col, char in enumerate(line):
            # Add numeric characters to number store
            if char.isnumeric():
                number += char
                number_indices.append(col)

            # Process number
            # If not start of line
            # And we encounter a character after some numbers
            # If end of line then process if number store is not empty
            if col == 0:
                continue

            line_ending_number = char.isnumeric() and col == max_col_index
            symbol_encountered = number and not char.isnumeric()
            if line_ending_number or symbol_encountered:
                current_number = int(number)

                row_low = max(0, row - 1)
                col_low = max(0, number_indices[0] - 1)

                row_high = min(max_row_index, row + 1)
                col_high = min(max_col_index, number_indices[-1] + 1)

                for rw in range(row_low, row_high + 1):
                    for cw in range(col_low, col_high + 1):
                        pos = (rw, cw)
                        if pos in gears:
                            gears[pos].append(current_number)
                            break

                # Reset state
                number = ""
                number_indices = []

    gears_with_two = [v for v in gears.values() if len(v) == 2]
    gear_products = [v[0] * v[1] for v in gears_with_two]
    gear_sum = sum(gear_products)

    # print("Gears:", gears)
    # print("Valued Gears:", gears_with_two)
    # print("Gear Products:", gear_products)
    print(f"Gear Product Sum: {gear_sum}")


if __name__ == "__main__":
    main()
